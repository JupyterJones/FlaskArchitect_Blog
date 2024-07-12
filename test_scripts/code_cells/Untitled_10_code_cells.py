import sys

sys.path.remove('/home/jack/hidden')

# %load main_dpir_deblur.py
import os.path
import cv2
import logging

import numpy as np
from datetime import datetime
from collections import OrderedDict
import hdf5storage
from scipy import ndimage

import torch

from utils import utils_deblur
from utils import utils_logger
from utils import utils_model
from utils import utils_pnp as pnp
from utils import utils_sisr as sr
from utils import utils_image as util


"""
Spyder (Python 3.7)
PyTorch 1.6.0
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/DPIR
        https://github.com/cszn/IRCNN
        https://github.com/cszn/KAIR
@article{zhang2020plug,
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={arXiv preprint},
  year={2020}
}
% If you have any question, please feel free to contact with me.
% Kai Zhang (e-mail: cskaizhang@gmail.com; homepage: https://cszn.github.io/)
by Kai Zhang (01/August/2020)

# --------------------------------------------
|--model_zoo               # model_zoo
   |--drunet_gray          # model_name, for color images
   |--drunet_color
|--testset                 # testsets
|--results                 # results
# --------------------------------------------
"""

def main():

    # ----------------------------------------
    # Preparation
    # ----------------------------------------

    noise_level_img = 7.65/255.0         # default: 0, noise level for LR image
    noise_level_model = noise_level_img  # noise level of model, default 0
    model_name = 'drunet_gray'           # 'drunet_gray' | 'drunet_color' | 'ircnn_gray' | 'ircnn_color'
    testset_name = 'Set3C'               # test set,  'set5' | 'srbsd68'
    x8 = True                            # default: False, x8 to boost performance
    iter_num = 8                         # number of iterations
    modelSigma1 = 49
    modelSigma2 = noise_level_model*255.

    show_img = False                     # default: False
    save_L = True                        # save LR image
    save_E = True                        # save estimated image
    save_LEH = False                     # save zoomed LR, E and H images
    border = 0

    # --------------------------------
    # load kernel
    # --------------------------------

    kernels = hdf5storage.loadmat(os.path.join('kernels', 'Levin09.mat'))['kernels']

    sf = 1
    task_current = 'deblur'              # 'deblur' for deblurring
    n_channels = 3 if 'color' in  model_name else 1  # fixed
    model_zoo = 'model_zoo'              # fixed
    testsets = 'testsets'                # fixed
    results = 'results'                  # fixed
    result_name = testset_name + '_' + task_current + '_' + model_name
    model_path = os.path.join(model_zoo, model_name+'.pth')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    torch.cuda.empty_cache()

    # ----------------------------------------
    # L_path, E_path, H_path
    # ----------------------------------------

    L_path = os.path.join(testsets, testset_name) # L_path, for Low-quality images
    E_path = os.path.join(results, result_name)   # E_path, for Estimated images
    util.mkdir(E_path)

    logger_name = result_name
    utils_logger.logger_info(logger_name, log_path=os.path.join(E_path, logger_name+'.log'))
    log_path=os.path.join(E_path, logger_name+'.log')
    print(log_path)                      
    logger = logging.getLogger(logger_name)

    # ----------------------------------------
    # load model
    # ----------------------------------------

    if 'drunet' in model_name:
        from models.network_unet import UNetRes as net
        model = net(in_nc=n_channels+1, out_nc=n_channels, nc=[64, 128, 256, 512], nb=4, act_mode='R', downsample_mode="strideconv", upsample_mode="convtranspose")
        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        for _, v in model.named_parameters():
            v.requires_grad = False
        model = model.to(device)
    elif 'ircnn' in model_name:
        from models.network_dncnn import IRCNN as net
        model = net(in_nc=n_channels, out_nc=n_channels, nc=64)
        model25 = torch.load(model_path)
        former_idx = 0

    logger.info('model_name:{}, image sigma:{:.3f}, model sigma:{:.3f}'.format(model_name, noise_level_img, noise_level_model))
    logger.info('Model path: {:s}'.format(model_path))
    logger.info(L_path)
    L_paths = util.get_image_paths(L_path)

    test_results_ave = OrderedDict()
    test_results_ave['psnr'] = []  # record average PSNR for each kernel

    for k_index in range(kernels.shape[1]):

        logger.info('-------k:{:>2d} ---------'.format(k_index))
        test_results = OrderedDict()
        test_results['psnr'] = []
        k = kernels[0, k_index].astype(np.float64)
        util.imshow(k) if show_img else None

        for idx, img in enumerate(L_paths):

            # --------------------------------
            # (1) get img_L
            # --------------------------------

            img_name, ext = os.path.splitext(os.path.basename(img))
            img_H = util.imread_uint(img, n_channels=n_channels)
            img_H = util.modcrop(img_H, 8)  # modcrop

            img_L = ndimage.filters.convolve(img_H, np.expand_dims(k, axis=2), mode='wrap')
            util.imshow(img_L) if show_img else None
            img_L = util.uint2single(img_L)

            np.random.seed(seed=0)  # for reproducibility
            img_L += np.random.normal(0, noise_level_img, img_L.shape) # add AWGN

            # --------------------------------
            # (2) get rhos and sigmas
            # --------------------------------

            rhos, sigmas = pnp.get_rho_sigma(sigma=max(0.255/255., noise_level_model), iter_num=iter_num, modelSigma1=modelSigma1, modelSigma2=modelSigma2, w=1.0)
            rhos, sigmas = torch.tensor(rhos).to(device), torch.tensor(sigmas).to(device)

            # --------------------------------
            # (3) initialize x, and pre-calculation
            # --------------------------------

            x = util.single2tensor4(img_L).to(device)

            img_L_tensor, k_tensor = util.single2tensor4(img_L), util.single2tensor4(np.expand_dims(k, 2))
            [k_tensor, img_L_tensor] = util.todevice([k_tensor, img_L_tensor], device)
            FB, FBC, F2B, FBFy = sr.pre_calculate(img_L_tensor, k_tensor, sf)

            # --------------------------------
            # (4) main iterations
            # --------------------------------

            for i in range(iter_num):

                # --------------------------------
                # step 1, FFT
                # --------------------------------

                tau = rhos[i].float().repeat(1, 1, 1, 1)
                x = sr.data_solution(x, FB, FBC, F2B, FBFy, tau, sf)

                if 'ircnn' in model_name:
                    current_idx = np.int(np.ceil(sigmas[i].cpu().numpy()*255./2.)-1)
        
                    if current_idx != former_idx:
                        model.load_state_dict(model25[str(current_idx)], strict=True)
                        model.eval()
                        for _, v in model.named_parameters():
                            v.requires_grad = False
                        model = model.to(device)
                    former_idx = current_idx

                # --------------------------------
                # step 2, denoiser
                # --------------------------------

                if x8:
                    x = util.augment_img_tensor4(x, i % 8)

                if 'drunet' in model_name:
                    x = torch.cat((x, sigmas[i].float().repeat(1, 1, x.shape[2], x.shape[3])), dim=1)
                    x = utils_model.test_mode(model, x, mode=2, refield=32, min_size=256, modulo=16)
                elif 'ircnn' in model_name:
                    x = model(x)

                if x8:
                    if i % 8 == 3 or i % 8 == 5:
                        x = util.augment_img_tensor4(x, 8 - i % 8)
                    else:
                        x = util.augment_img_tensor4(x, i % 8)

            # --------------------------------
            # (3) img_E
            # --------------------------------

            img_E = util.tensor2uint(x)
            if n_channels == 1:
                img_H = img_H.squeeze()

            if save_E:
                util.imsave(img_E, os.path.join(E_path, img_name+'_k'+str(k_index)+'_'+model_name+'.png'))

            # --------------------------------
            # (4) img_LEH
            # --------------------------------

            if save_LEH:
                img_L = util.single2uint(img_L)
                k_v = k/np.max(k)*1.0
                k_v = util.single2uint(np.tile(k_v[..., np.newaxis], [1, 1, 3]))
                k_v = cv2.resize(k_v, (3*k_v.shape[1], 3*k_v.shape[0]), interpolation=cv2.INTER_NEAREST)
                img_I = cv2.resize(img_L, (sf*img_L.shape[1], sf*img_L.shape[0]), interpolation=cv2.INTER_NEAREST)
                img_I[:k_v.shape[0], -k_v.shape[1]:, :] = k_v
                img_I[:img_L.shape[0], :img_L.shape[1], :] = img_L
                util.imshow(np.concatenate([img_I, img_E, img_H], axis=1), title='LR / Recovered / Ground-truth') if show_img else None
                util.imsave(np.concatenate([img_I, img_E, img_H], axis=1), os.path.join(E_path, img_name+'_k'+str(k_index)+'_LEH.png'))

            if save_L:
                util.imsave(util.single2uint(img_L), os.path.join(E_path, img_name+'_k'+str(k_index)+'_LR.png'))

            psnr = util.calculate_psnr(img_E, img_H, border=border)  # change with your own border
            test_results['psnr'].append(psnr)
            logger.info('{:->4d}--> {:>10s} --k:{:>2d} PSNR: {:.2f}dB'.format(idx+1, img_name+ext, k_index, psnr))


        # --------------------------------
        # Average PSNR
        # --------------------------------

        ave_psnr = sum(test_results['psnr']) / len(test_results['psnr'])
        logger.info('------> Average PSNR of ({}), kernel: ({}) sigma: ({:.2f}): {:.2f} dB'.format(testset_name, k_index, noise_level_model, ave_psnr))
        test_results_ave['psnr'].append(ave_psnr)

if __name__ == '__main__':

    main()


log_path=os.path.join(E_path, logger_name+'.log')
print(log_path)           

# %load main_dpir_denoising.py
import os.path
import logging

import numpy as np
from collections import OrderedDict

import torch

from utils import utils_logger
from utils import utils_model
from utils import utils_image as util


"""
Spyder (Python 3.7)
PyTorch 1.6.0
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/DPIR
        https://github.com/cszn/IRCNN
        https://github.com/cszn/KAIR
@article{zhang2020plug,
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={arXiv preprint},
  year={2020}
}
% If you have any question, please feel free to contact with me.
% Kai Zhang (e-mail: cskaizhang@gmail.com; homepage: https://cszn.github.io/)
by Kai Zhang (01/August/2020)

# --------------------------------------------
|--model_zoo               # model_zoo
   |--drunet_gray          # model_name, for color images
   |--drunet_color
|--testset                 # testsets
   |--set12                # testset_name
   |--bsd68
   |--cbsd68
|--results                 # results
   |--set12_dn_drunet_gray # result_name = testset_name + '_' + 'dn' + model_name
   |--set12_dn_drunet_color
# --------------------------------------------
"""


def main():

    # ----------------------------------------
    # Preparation
    # ----------------------------------------

    noise_level_img = 15                 # set AWGN noise level for noisy image
    noise_level_model = noise_level_img  # set noise level for model
    model_name = 'drunet_gray'           # set denoiser model, 'drunet_gray' | 'drunet_color'
    testset_name = 'bsd68'               # set test set,  'bsd68' | 'cbsd68' | 'set12'
    x8 = False                           # default: False, x8 to boost performance
    show_img = False                     # default: False
    border = 0                           # shave boader to calculate PSNR and SSIM

    if 'color' in model_name:
        n_channels = 3                   # 3 for color image
    else:
        n_channels = 1                   # 1 for grayscale image

    model_pool = 'model_zoo'             # fixed
    testsets = 'testsets'                # fixed
    results = 'results'                  # fixed
    task_current = 'dn'                  # 'dn' for denoising
    result_name = testset_name + '_' + task_current + '_' + model_name

    model_path = os.path.join(model_pool, model_name+'.pth')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    torch.cuda.empty_cache()

    # ----------------------------------------
    # L_path, E_path, H_path
    # ----------------------------------------

    L_path = os.path.join(testsets, testset_name) # L_path, for Low-quality images
    E_path = os.path.join(results, result_name)   # E_path, for Estimated images
    util.mkdir(E_path)

    logger_name = result_name
    utils_logger.logger_info(logger_name, log_path=os.path.join(E_path, logger_name+'.log'))
    logger = logging.getLogger(logger_name)

    # ----------------------------------------
    # load model
    # ----------------------------------------

    from models.network_unet import UNetRes as net
    model = net(in_nc=n_channels+1, out_nc=n_channels, nc=[64, 128, 256, 512], nb=4, act_mode='R', downsample_mode="strideconv", upsample_mode="convtranspose")
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    for k, v in model.named_parameters():
        v.requires_grad = False
    model = model.to(device)
    logger.info('Model path: {:s}'.format(model_path))
    number_parameters = sum(map(lambda x: x.numel(), model.parameters()))
    logger.info('Params number: {}'.format(number_parameters))

    test_results = OrderedDict()
    test_results['psnr'] = []
    test_results['ssim'] = []

    logger.info('model_name:{}, model sigma:{}, image sigma:{}'.format(model_name, noise_level_img, noise_level_model))
    logger.info(L_path)
    L_paths = util.get_image_paths(L_path)

    for idx, img in enumerate(L_paths):

        # ------------------------------------
        # (1) img_L
        # ------------------------------------

        img_name, ext = os.path.splitext(os.path.basename(img))
        # logger.info('{:->4d}--> {:>10s}'.format(idx+1, img_name+ext))
        img_H = util.imread_uint(img, n_channels=n_channels)
        img_L = util.uint2single(img_H)

        # Add noise without clipping
        np.random.seed(seed=0)  # for reproducibility
        img_L += np.random.normal(0, noise_level_img/255., img_L.shape)

        util.imshow(util.single2uint(img_L), title='Noisy image with noise level {}'.format(noise_level_img)) if show_img else None

        img_L = util.single2tensor4(img_L)
        img_L = torch.cat((img_L, torch.FloatTensor([noise_level_model/255.]).repeat(1, 1, img_L.shape[2], img_L.shape[3])), dim=1)
        img_L = img_L.to(device)

        # ------------------------------------
        # (2) img_E
        # ------------------------------------

        if not x8 and img_L.size(2)//8==0 and img_L.size(3)//8==0:
            img_E = model(img_L)
        elif not x8 and (img_L.size(2)//8!=0 or img_L.size(3)//8!=0):
            img_E = utils_model.test_mode(model, img_L, refield=64, mode=5)
        elif x8:
            img_E = utils_model.test_mode(model, img_L, mode=3)

        img_E = util.tensor2uint(img_E)

        # --------------------------------
        # PSNR and SSIM
        # --------------------------------

        if n_channels == 1:
            img_H = img_H.squeeze() 
        psnr = util.calculate_psnr(img_E, img_H, border=border)
        ssim = util.calculate_ssim(img_E, img_H, border=border)
        test_results['psnr'].append(psnr)
        test_results['ssim'].append(ssim)
        logger.info('{:s} - PSNR: {:.2f} dB; SSIM: {:.4f}.'.format(img_name+ext, psnr, ssim))

        # ------------------------------------
        # save results
        # ------------------------------------

        util.imsave(img_E, os.path.join(E_path, img_name+ext))

    ave_psnr = sum(test_results['psnr']) / len(test_results['psnr'])
    ave_ssim = sum(test_results['ssim']) / len(test_results['ssim'])
    logger.info('Average PSNR/SSIM(RGB) - {} - PSNR: {:.2f} dB; SSIM: {:.4f}'.format(result_name, ave_psnr, ave_ssim))


if __name__ == '__main__':

    main()












sys.path.remove('/home/sergey')

sys.path

!mkdir testsets/bsd68

!ls

# /KAIR/master/utils/utils_sisr.py
# -*- coding: utf-8 -*-
from utils import utils_image as util
import random
import cv2
import scipy
import scipy.stats as ss
import scipy.io as io
from scipy import ndimage
from scipy.interpolate import interp2d

import numpy as np
import torch


"""
# --------------------------------------------
# Super-Resolution
# --------------------------------------------
#
# Kai Zhang (cskaizhang@gmail.com)
# https://github.com/cszn
# modified by Kai Zhang (github: https://github.com/cszn)
# 03/03/2020
# --------------------------------------------
"""


"""
# --------------------------------------------
# anisotropic Gaussian kernels
# --------------------------------------------
"""


def anisotropic_Gaussian(ksize=15, theta=np.pi, l1=6, l2=6):
    """ generate an anisotropic Gaussian kernel
    Args:
        ksize : e.g., 15, kernel size
        theta : [0,  pi], rotation angle range
        l1    : [0.1,50], scaling of eigenvalues
        l2    : [0.1,l1], scaling of eigenvalues
        If l1 = l2, will get an isotropic Gaussian kernel.
    Returns:
        k     : kernel
    """

    v = np.dot(np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]), np.array([1., 0.]))
    V = np.array([[v[0], v[1]], [v[1], -v[0]]])
    D = np.array([[l1, 0], [0, l2]])
    Sigma = np.dot(np.dot(V, D), np.linalg.inv(V))
    k = gm_blur_kernel(mean=[0, 0], cov=Sigma, size=ksize)

    return k


def gm_blur_kernel(mean, cov, size=15):
    center = size / 2.0 + 0.5
    k = np.zeros([size, size])
    for y in range(size):
        for x in range(size):
            cy = y - center + 1
            cx = x - center + 1
            k[y, x] = ss.multivariate_normal.pdf([cx, cy], mean=mean, cov=cov)

    k = k / np.sum(k)
    return k


"""
# --------------------------------------------
# calculate PCA projection matrix
# --------------------------------------------
"""


def get_pca_matrix(x, dim_pca=15):
    """
    Args:
        x: 225x10000 matrix
        dim_pca: 15
    Returns:
        pca_matrix: 15x225
    """
    C = np.dot(x, x.T)
    w, v = scipy.linalg.eigh(C)
    pca_matrix = v[:, -dim_pca:].T

    return pca_matrix


def show_pca(x):
    """
    x: PCA projection matrix, e.g., 15x225
    """
    for i in range(x.shape[0]):
        if i % 25 ==0:print(i)
        xc = np.reshape(x[i, :], (int(np.sqrt(x.shape[1])), -1), order="F")
        util.surf(xc)


def cal_pca_matrix(path='PCA_matrix.mat', ksize=15, l_max=12.0, dim_pca=15, num_samples=500):
    kernels = np.zeros([ksize*ksize, num_samples], dtype=np.float32)
    for i in range(num_samples):
        if i % 1000 ==0:print(i)

        theta = np.pi*np.random.rand(1)
        l1    = 0.1+l_max*np.random.rand(1)
        l2    = 0.1+(l1-0.1)*np.random.rand(1)

        k = anisotropic_Gaussian(ksize=ksize, theta=theta[0], l1=l1[0], l2=l2[0])

        # util.imshow(k)

        kernels[:, i] = np.reshape(k, (-1), order="F")  # k.flatten(order='F')

    # io.savemat('k.mat', {'k': kernels})

    pca_matrix = get_pca_matrix(kernels, dim_pca=dim_pca)

    io.savemat(path, {'p': pca_matrix})

    return pca_matrix


"""
# --------------------------------------------
# shifted anisotropic Gaussian kernels
# --------------------------------------------
"""


def shifted_anisotropic_Gaussian(k_size=np.array([15, 15]), scale_factor=np.array([4, 4]), min_var=0.6, max_var=10., noise_level=0):
    """"
    # modified version of https://github.com/assafshocher/BlindSR_dataset_generator
    # Kai Zhang
    # min_var = 0.175 * sf  # variance of the gaussian kernel will be sampled between min_var and max_var
    # max_var = 2.5 * sf
    """
    # Set random eigen-vals (lambdas) and angle (theta) for COV matrix
    lambda_1 = min_var + np.random.rand() * (max_var - min_var)
    lambda_2 = min_var + np.random.rand() * (max_var - min_var)
    theta = np.random.rand() * np.pi  # random theta
    noise = -noise_level + np.random.rand(*k_size) * noise_level * 2

    # Set COV matrix using Lambdas and Theta
    LAMBDA = np.diag([lambda_1, lambda_2])
    Q = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    SIGMA = Q @ LAMBDA @ Q.T
    INV_SIGMA = np.linalg.inv(SIGMA)[None, None, :, :]

    # Set expectation position (shifting kernel for aligned image)
    MU = k_size // 2 - 0.5*(scale_factor - 1) # - 0.5 * (scale_factor - k_size % 2)
    MU = MU[None, None, :, None]

    # Create meshgrid for Gaussian
    [X,Y] = np.meshgrid(range(k_size[0]), range(k_size[1]))
    Z = np.stack([X, Y], 2)[:, :, :, None]

    # Calcualte Gaussian for every pixel of the kernel
    ZZ = Z-MU
    ZZ_t = ZZ.transpose(0,1,3,2)
    raw_kernel = np.exp(-0.5 * np.squeeze(ZZ_t @ INV_SIGMA @ ZZ)) * (1 + noise)

    # shift the kernel so it will be centered
    #raw_kernel_centered = kernel_shift(raw_kernel, scale_factor)

    # Normalize the kernel and return
    #kernel = raw_kernel_centered / np.sum(raw_kernel_centered)
    kernel = raw_kernel / np.sum(raw_kernel)
    return kernel


def gen_kernel(k_size=np.array([25, 25]), scale_factor=np.array([4, 4]), min_var=0.6, max_var=12., noise_level=0):
    """"
    # modified version of https://github.com/assafshocher/BlindSR_dataset_generator
    # Kai Zhang
    # min_var = 0.175 * sf  # variance of the gaussian kernel will be sampled between min_var and max_var
    # max_var = 2.5 * sf
    """
    sf = random.choice([1, 2, 3, 4])
    scale_factor = np.array([sf, sf])
    # Set random eigen-vals (lambdas) and angle (theta) for COV matrix
    lambda_1 = min_var + np.random.rand() * (max_var - min_var)
    lambda_2 = min_var + np.random.rand() * (max_var - min_var)
    theta = np.random.rand() * np.pi  # random theta
    noise = 0#-noise_level + np.random.rand(*k_size) * noise_level * 2

    # Set COV matrix using Lambdas and Theta
    LAMBDA = np.diag([lambda_1, lambda_2])
    Q = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    SIGMA = Q @ LAMBDA @ Q.T
    INV_SIGMA = np.linalg.inv(SIGMA)[None, None, :, :]

    # Set expectation position (shifting kernel for aligned image)
    MU = k_size // 2 - 0.5*(scale_factor - 1) # - 0.5 * (scale_factor - k_size % 2)
    MU = MU[None, None, :, None]

    # Create meshgrid for Gaussian
    [X,Y] = np.meshgrid(range(k_size[0]), range(k_size[1]))
    Z = np.stack([X, Y], 2)[:, :, :, None]

    # Calcualte Gaussian for every pixel of the kernel
    ZZ = Z-MU
    ZZ_t = ZZ.transpose(0,1,3,2)
    raw_kernel = np.exp(-0.5 * np.squeeze(ZZ_t @ INV_SIGMA @ ZZ)) * (1 + noise)

    # shift the kernel so it will be centered
    #raw_kernel_centered = kernel_shift(raw_kernel, scale_factor)

    # Normalize the kernel and return
    #kernel = raw_kernel_centered / np.sum(raw_kernel_centered)
    kernel = raw_kernel / np.sum(raw_kernel)
    return kernel


"""
# --------------------------------------------
# degradation models
# --------------------------------------------
"""


def bicubic_degradation(x, sf=3):
    '''
    Args:
        x: HxWxC image, [0, 1]
        sf: down-scale factor
    Return:
        bicubicly downsampled LR image
    '''
    x = util.imresize_np(x, scale=1/sf)
    return x


def srmd_degradation(x, k, sf=3):
    ''' blur + bicubic downsampling
    Args:
        x: HxWxC image, [0, 1]
        k: hxw, double
        sf: down-scale factor
    Return:
        downsampled LR image
    Reference:
        @inproceedings{zhang2018learning,
          title={Learning a single convolutional super-resolution network for multiple degradations},
          author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
          booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
          pages={3262--3271},
          year={2018}
        }
    '''
    x = ndimage.filters.convolve(x, np.expand_dims(k, axis=2), mode='wrap')  # 'nearest' | 'mirror'
    x = bicubic_degradation(x, sf=sf)
    return x


def dpsr_degradation(x, k, sf=3):

    ''' bicubic downsampling + blur
    Args:
        x: HxWxC image, [0, 1]
        k: hxw, double
        sf: down-scale factor
    Return:
        downsampled LR image
    Reference:
        @inproceedings{zhang2019deep,
          title={Deep Plug-and-Play Super-Resolution for Arbitrary Blur Kernels},
          author={Zhang, Kai and Zuo, Wangmeng and Zhang, Lei},
          booktitle={IEEE Conference on Computer Vision and Pattern Recognition},
          pages={1671--1681},
          year={2019}
        }
    '''
    x = bicubic_degradation(x, sf=sf)
    x = ndimage.filters.convolve(x, np.expand_dims(k, axis=2), mode='wrap')
    return x


def classical_degradation(x, k, sf=3):
    ''' blur + downsampling

    Args:
        x: HxWxC image, [0, 1]/[0, 255]
        k: hxw, double
        sf: down-scale factor

    Return:
        downsampled LR image
    '''
    x = ndimage.filters.convolve(x, np.expand_dims(k, axis=2), mode='wrap')
    #x = filters.correlate(x, np.expand_dims(np.flip(k), axis=2))
    st = 0
    return x[st::sf, st::sf, ...]


def modcrop_np(img, sf):
    '''
    Args:
        img: numpy image, WxH or WxHxC
        sf: scale factor
    Return:
        cropped image
    '''
    w, h = img.shape[:2]
    im = np.copy(img)
    return im[:w - w % sf, :h - h % sf, ...]


'''
# =================
# Numpy
# =================
'''


def shift_pixel(x, sf, upper_left=True):
    """shift pixel for super-resolution with different scale factors
    Args:
        x: WxHxC or WxH, image or kernel
        sf: scale factor
        upper_left: shift direction
    """
    h, w = x.shape[:2]
    shift = (sf-1)*0.5
    xv, yv = np.arange(0, w, 1.0), np.arange(0, h, 1.0)
    if upper_left:
        x1 = xv + shift
        y1 = yv + shift
    else:
        x1 = xv - shift
        y1 = yv - shift

    x1 = np.clip(x1, 0, w-1)
    y1 = np.clip(y1, 0, h-1)

    if x.ndim == 2:
        x = interp2d(xv, yv, x)(x1, y1)
    if x.ndim == 3:
        for i in range(x.shape[-1]):
            x[:, :, i] = interp2d(xv, yv, x[:, :, i])(x1, y1)

    return x


'''
# =================
# pytorch
# =================
'''


def splits(a, sf):
    '''
    a: tensor NxCxWxHx2
    sf: scale factor
    out: tensor NxCx(W/sf)x(H/sf)x2x(sf^2)
    '''
    b = torch.stack(torch.chunk(a, sf, dim=2), dim=5)
    b = torch.cat(torch.chunk(b, sf, dim=3), dim=5)
    return b


def c2c(x):
    return torch.from_numpy(np.stack([np.float32(x.real), np.float32(x.imag)], axis=-1))


def r2c(x):
    return torch.stack([x, torch.zeros_like(x)], -1)


def cdiv(x, y):
    a, b = x[..., 0], x[..., 1]
    c, d = y[..., 0], y[..., 1]
    cd2 = c**2 + d**2
    return torch.stack([(a*c+b*d)/cd2, (b*c-a*d)/cd2], -1)


def csum(x, y):
    return torch.stack([x[..., 0] + y, x[..., 1]], -1)


def cabs(x):
    return torch.pow(x[..., 0]**2+x[..., 1]**2, 0.5)


def cmul(t1, t2):
    '''
    complex multiplication
    t1: NxCxHxWx2
    output: NxCxHxWx2
    '''
    real1, imag1 = t1[..., 0], t1[..., 1]
    real2, imag2 = t2[..., 0], t2[..., 1]
    return torch.stack([real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2], dim=-1)


def cconj(t, inplace=False):
    '''
    # complex's conjugation
    t: NxCxHxWx2
    output: NxCxHxWx2
    '''
    c = t.clone() if not inplace else t
    c[..., 1] *= -1
    return c


def rfft(t):
    return torch.rfft(t, 2, onesided=False)


def irfft(t):
    return torch.irfft(t, 2, onesided=False)


def fft(t):
    return torch.fft(t, 2)


def ifft(t):
    return torch.ifft(t, 2)


def p2o(psf, shape):
    '''
    Args:
        psf: NxCxhxw
        shape: [H,W]

    Returns:
        otf: NxCxHxWx2
    '''
    otf = torch.zeros(psf.shape[:-2] + shape).type_as(psf)
    otf[...,:psf.shape[2],:psf.shape[3]].copy_(psf)
    for axis, axis_size in enumerate(psf.shape[2:]):
        otf = torch.roll(otf, -int(axis_size / 2), dims=axis+2)
    otf = torch.rfft(otf, 2, onesided=False)
    n_ops = torch.sum(torch.tensor(psf.shape).type_as(psf) * torch.log2(torch.tensor(psf.shape).type_as(psf)))
    otf[...,1][torch.abs(otf[...,1])<n_ops*2.22e-16] = torch.tensor(0).type_as(psf)
    return otf


'''
# =================
PyTorch
# =================
'''

def INVLS_pytorch(FB, FBC, F2B, FR, tau, sf=2):
    '''
    FB: NxCxWxHx2
    F2B: NxCxWxHx2

    x1 = FB.*FR;
    FBR = BlockMM(nr,nc,Nb,m,x1);
    invW = BlockMM(nr,nc,Nb,m,F2B);
    invWBR = FBR./(invW + tau*Nb);
    fun = @(block_struct) block_struct.data.*invWBR;
    FCBinvWBR = blockproc(FBC,[nr,nc],fun);
    FX = (FR-FCBinvWBR)/tau;
    Xest = real(ifft2(FX));
    '''
    x1 = cmul(FB, FR)
    FBR = torch.mean(splits(x1, sf), dim=-1, keepdim=False)
    invW = torch.mean(splits(F2B, sf), dim=-1, keepdim=False)
    invWBR = cdiv(FBR, csum(invW, tau))
    FCBinvWBR = cmul(FBC, invWBR.repeat(1,1,sf,sf,1))
    FX = (FR-FCBinvWBR)/tau
    Xest = torch.irfft(FX, 2, onesided=False)
    return Xest


def real2complex(x):
    return torch.stack([x, torch.zeros_like(x)], -1)


def modcrop(img, sf):
    '''
    img: tensor image, NxCxWxH or CxWxH or WxH
    sf: scale factor
    '''
    w, h = img.shape[-2:]
    im = img.clone()
    return im[..., :w - w % sf, :h - h % sf]


def upsample(x, sf=3, center=False):
    '''
    x: tensor image, NxCxWxH
    '''
    st = (sf-1)//2 if center else 0
    z = torch.zeros((x.shape[0], x.shape[1], x.shape[2]*sf, x.shape[3]*sf)).type_as(x)
    z[..., st::sf, st::sf].copy_(x)
    return z


def downsample(x, sf=3, center=False):
    st = (sf-1)//2 if center else 0
    return x[..., st::sf, st::sf]


def circular_pad(x, pad):
    '''
    # x[N, 1, W, H] -> x[N, 1, W + 2 pad, H + 2 pad] (pariodic padding)
    '''
    x = torch.cat([x, x[:, :, 0:pad, :]], dim=2)
    x = torch.cat([x, x[:, :, :, 0:pad]], dim=3)
    x = torch.cat([x[:, :, -2 * pad:-pad, :], x], dim=2)
    x = torch.cat([x[:, :, :, -2 * pad:-pad], x], dim=3)
    return x


def pad_circular(input, padding):
    # type: (Tensor, List[int]) -> Tensor
    """
    Arguments
    :param input: tensor of shape :math:`(N, C_{\text{in}}, H, [W, D]))`
    :param padding: (tuple): m-elem tuple where m is the degree of convolution
    Returns
    :return: tensor of shape :math:`(N, C_{\text{in}}, [D + 2 * padding[0],
                                     H + 2 * padding[1]], W + 2 * padding[2]))`
    """
    offset = 3
    for dimension in range(input.dim() - offset + 1):
        input = dim_pad_circular(input, padding[dimension], dimension + offset)
    return input


def dim_pad_circular(input, padding, dimension):
    # type: (Tensor, int, int) -> Tensor
    input = torch.cat([input, input[[slice(None)] * (dimension - 1) +
                      [slice(0, padding)]]], dim=dimension - 1)
    input = torch.cat([input[[slice(None)] * (dimension - 1) +
                      [slice(-2 * padding, -padding)]], input], dim=dimension - 1)
    return input


def imfilter(x, k):
    '''
    x: image, NxcxHxW
    k: kernel, cx1xhxw
    '''
    x = pad_circular(x, padding=((k.shape[-2]-1)//2, (k.shape[-1]-1)//2))
    x = torch.nn.functional.conv2d(x, k, groups=x.shape[1])
    return x


def G(x, k, sf=3, center=False):
    '''
    x: image, NxcxHxW
    k: kernel, cx1xhxw
    sf: scale factor
    center: the first one or the moddle one

    Matlab function:
    tmp = imfilter(x,h,'circular');
    y = downsample2(tmp,K);
    '''
    x = downsample(imfilter(x, k), sf=sf, center=center)
    return x


def Gt(x, k, sf=3, center=False):
    '''
    x: image, NxcxHxW
    k: kernel, cx1xhxw
    sf: scale factor
    center: the first one or the moddle one

    Matlab function:
    tmp = upsample2(x,K);
    y = imfilter(tmp,h,'circular');
    '''
    x = imfilter(upsample(x, sf=sf, center=center), k)
    return x


def interpolation_down(x, sf, center=False):
    mask = torch.zeros_like(x)
    if center:
        start = torch.tensor((sf-1)//2)
        mask[..., start::sf, start::sf] = torch.tensor(1).type_as(x)
        LR = x[..., start::sf, start::sf]
    else:
        mask[..., ::sf, ::sf] = torch.tensor(1).type_as(x)
        LR = x[..., ::sf, ::sf]
    y = x.mul(mask)

    return LR, y, mask


'''
# =================
Numpy
# =================
'''


def blockproc(im, blocksize, fun):
    xblocks = np.split(im, range(blocksize[0], im.shape[0], blocksize[0]), axis=0)
    xblocks_proc = []
    for xb in xblocks:
        yblocks = np.split(xb, range(blocksize[1], im.shape[1], blocksize[1]), axis=1)
        yblocks_proc = []
        for yb in yblocks:
            yb_proc = fun(yb)
            yblocks_proc.append(yb_proc)
        xblocks_proc.append(np.concatenate(yblocks_proc, axis=1))

    proc = np.concatenate(xblocks_proc, axis=0)

    return proc


def fun_reshape(a):
    return np.reshape(a, (-1,1,a.shape[-1]), order='F')


def fun_mul(a, b):
    return a*b


def BlockMM(nr, nc, Nb, m, x1):
    '''
    myfun = @(block_struct) reshape(block_struct.data,m,1);
    x1 = blockproc(x1,[nr nc],myfun);
    x1 = reshape(x1,m,Nb);
    x1 = sum(x1,2);
    x = reshape(x1,nr,nc);
    '''
    fun = fun_reshape
    x1 = blockproc(x1, blocksize=(nr, nc), fun=fun)
    x1 = np.reshape(x1, (m, Nb, x1.shape[-1]), order='F')
    x1 = np.sum(x1, 1)
    x = np.reshape(x1, (nr, nc, x1.shape[-1]), order='F')
    return x


def INVLS(FB, FBC, F2B, FR, tau, Nb, nr, nc, m):
    '''
    x1 = FB.*FR;
    FBR = BlockMM(nr,nc,Nb,m,x1);
    invW = BlockMM(nr,nc,Nb,m,F2B);
    invWBR = FBR./(invW + tau*Nb);
    fun = @(block_struct) block_struct.data.*invWBR;
    FCBinvWBR = blockproc(FBC,[nr,nc],fun);
    FX = (FR-FCBinvWBR)/tau;
    Xest = real(ifft2(FX));
    '''
    x1 = FB*FR
    FBR = BlockMM(nr, nc, Nb, m, x1)
    invW = BlockMM(nr, nc, Nb, m, F2B)
    invWBR = FBR/(invW + tau*Nb)
    FCBinvWBR = blockproc(FBC, [nr, nc], lambda im: fun_mul(im, invWBR))
    FX = (FR-FCBinvWBR)/tau
    Xest = np.real(np.fft.ifft2(FX, axes=(0, 1)))
    return Xest


def psf2otf(psf, shape=None):
    """
    Convert point-spread function to optical transfer function.
    Compute the Fast Fourier Transform (FFT) of the point-spread
    function (PSF) array and creates the optical transfer function (OTF)
    array that is not influenced by the PSF off-centering.
    By default, the OTF array is the same size as the PSF array.
    To ensure that the OTF is not altered due to PSF off-centering, PSF2OTF
    post-pads the PSF array (down or to the right) with zeros to match
    dimensions specified in OUTSIZE, then circularly shifts the values of
    the PSF array up (or to the left) until the central pixel reaches (1,1)
    position.
    Parameters
    ----------
    psf : `numpy.ndarray`
        PSF array
    shape : int
        Output shape of the OTF array
    Returns
    -------
    otf : `numpy.ndarray`
        OTF array
    Notes
    -----
    Adapted from MATLAB psf2otf function
    """
    if type(shape) == type(None):
        shape = psf.shape
    shape = np.array(shape)
    if np.all(psf == 0):
        # return np.zeros_like(psf)
        return np.zeros(shape)
    if len(psf.shape) == 1:
        psf = psf.reshape((1, psf.shape[0]))
    inshape = psf.shape
    psf = zero_pad(psf, shape, position='corner')
    for axis, axis_size in enumerate(inshape):
        psf = np.roll(psf, -int(axis_size / 2), axis=axis)
    # Compute the OTF
    otf = np.fft.fft2(psf, axes=(0, 1))
    # Estimate the rough number of operations involved in the FFT
    # and discard the PSF imaginary part if within roundoff error
    # roundoff error  = machine epsilon = sys.float_info.epsilon
    # or np.finfo().eps
    n_ops = np.sum(psf.size * np.log2(psf.shape))
    otf = np.real_if_close(otf, tol=n_ops)
    return otf


def zero_pad(image, shape, position='corner'):
    """
    Extends image to a certain size with zeros
    Parameters
    ----------
    image: real 2d `numpy.ndarray`
        Input image
    shape: tuple of int
        Desired output shape of the image
    position : str, optional
        The position of the input image in the output one:
            * 'corner'
                top-left corner (default)
            * 'center'
                centered
    Returns
    -------
    padded_img: real `numpy.ndarray`
        The zero-padded image
    """
    shape = np.asarray(shape, dtype=int)
    imshape = np.asarray(image.shape, dtype=int)
    if np.alltrue(imshape == shape):
        return image
    if np.any(shape <= 0):
        raise ValueError("ZERO_PAD: null or negative shape given")
    dshape = shape - imshape
    if np.any(dshape < 0):
        raise ValueError("ZERO_PAD: target size smaller than source one")
    pad_img = np.zeros(shape, dtype=image.dtype)
    idx, idy = np.indices(imshape)
    if position == 'center':
        if np.any(dshape % 2 != 0):
            raise ValueError("ZERO_PAD: source and target shapes "
                             "have different parity.")
        offx, offy = dshape // 2
    else:
        offx, offy = (0, 0)
    pad_img[idx + offx, idy + offy] = image
    return pad_img


def upsample_np(x, sf=3, center=False):
    st = (sf-1)//2 if center else 0
    z = np.zeros((x.shape[0]*sf, x.shape[1]*sf, x.shape[2]))
    z[st::sf, st::sf, ...] = x
    return z


def downsample_np(x, sf=3, center=False):
    st = (sf-1)//2 if center else 0
    return x[st::sf, st::sf, ...]


def imfilter_np(x, k):
    '''
    x: image, NxcxHxW
    k: kernel, cx1xhxw
    '''
    x = ndimage.filters.convolve(x, np.expand_dims(k, axis=2), mode='wrap')
    return x


def G_np(x, k, sf=3, center=False):
    '''
    x: image, NxcxHxW
    k: kernel, cx1xhxw

    Matlab function:
    tmp = imfilter(x,h,'circular');
    y = downsample2(tmp,K);
    '''
    x = downsample_np(imfilter_np(x, k), sf=sf, center=center)
    return x


def Gt_np(x, k, sf=3, center=False):
    '''
    x: image, NxcxHxW
    k: kernel, cx1xhxw

    Matlab function:
    tmp = upsample2(x,K);
    y = imfilter(tmp,h,'circular');
    '''
    x = imfilter_np(upsample_np(x, sf=sf, center=center), k)
    return x


if __name__ == '__main__':
    img = util.imread_uint('/home/jack/Desktop/BSRGAN/testsets/RealSRSet_results_x4/queenESRG_1_.png', 3)

    img = util.uint2single(img)
    k = anisotropic_Gaussian(ksize=15, theta=np.pi, l1=6, l2=6)
    util.imshow(k*10)


    for sf in [2, 3, 4]:

        # modcrop
        img = modcrop_np(img, sf=sf)
        cv2.imwrite("results/modcrop_np.png",img)
        # 1) bicubic degradation
        img_b = bicubic_degradation(img, sf=sf)
        print(img_b.shape)
        cv2.imwrite("results/img_b.png", img_b)
        #util.imsave(img_path,img_b)
        # 2) srmd degradation
        img_s = srmd_degradation(img, k, sf=sf)
        print(img_s.shape)
        cv2.imwrite("results/img_s.png",img_s)
        # 3) dpsr degradation
        img_d = dpsr_degradation(img, k, sf=sf)
        print(img_d.shape)
        cv2.imwrite("results/mg_d.png",img_d)
        # 4) classical degradation
        imgimg_d = classical_degradation(img, k, sf=sf)
        print(imgimg_d.shape)
        cv2.imwrite("results/img_d.png",imgimg_d)
    k = anisotropic_Gaussian(ksize=7, theta=0.25*np.pi, l1=0.01, l2=0.01)
    im2wr = k*10
    cv2.imwrite("results/kx10.png",im2wr)
    #print(k)
#    util.imshow(k*10)

    k = shifted_anisotropic_Gaussian(k_size=np.array([15, 15]), scale_factor=np.array([4, 4]), min_var=0.8, max_var=10.8, noise_level=0.0)
    im2wr2 = k*10
    cv2.imwrite("results/kx10.png",im2wr2)
#    util.imshow(k*10)


    # PCA
pca_matrix = cal_pca_matrix(ksize=15, l_max=10.0, dim_pca=15, num_samples=12500)
print(pca_matrix.shape)
show_pca(pca_matrix)
    # run utils/utils_sisr.py
    # run utils_sisr.py
    
    
    
    
    
    
    


shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is between arg 0 with shape (25,) and arg 2 with shape (15, 15).

img_d 

!ls results

# %load main_dpir_sisr_real_applications.py
import os.path
import glob
import cv2
import logging
import time

import numpy as np
from datetime import datetime
from collections import OrderedDict
import hdf5storage

import torch

from utils import utils_deblur
from utils import utils_logger
from utils import utils_model
from utils import utils_pnp as pnp
from utils import utils_sisr as sr
from utils import utils_image as util


"""
Spyder (Python 3.7)
PyTorch 1.6.0
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/DPIR
        https://github.com/cszn/IRCNN
        https://github.com/cszn/KAIR
@article{zhang2020plug,
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={arXiv preprint},
  year={2020}
}
% If you have any question, please feel free to contact with me.
% Kai Zhang (e-mail: cskaizhang@gmail.com; homepage: https://cszn.github.io/)
by Kai Zhang (01/August/2020)

# --------------------------------------------
|--model_zoo               # model_zoo
   |--drunet_gray          # model_name, for color images
   |--drunet_color
|--testset                 # testsets
|--results                 # results
# --------------------------------------------
"""

def main():

    """
    # ----------------------------------------------------------------------------------
    # In real applications, you should set proper 
    # - "noise_level_img": from [3, 25], set 3 for clean image, try 15 for very noisy LR images
    # - "k" (or "kernel_width"): blur kernel is very important!!!  kernel_width from [0.6, 3.0]
    # to get the best performance.
    # ----------------------------------------------------------------------------------
    """
    ##############################################################################

    testset_name = 'Set3C'               # set test set,  'set5' | 'srbsd68'
    noise_level_img = 3                  # set noise level of image, from [3, 25], set 3 for clean image
    model_name = 'drunet_color' # 'ircnn_color'         # set denoiser, | 'drunet_color' | 'ircnn_gray' | 'drunet_gray' | 'ircnn_color'
    sf = 2                               # set scale factor, 1, 2, 3, 4
    iter_num = 24                        # set number of iterations, default: 24 for SISR

    # --------------------------------
    # set blur kernel
    # --------------------------------
    kernel_width_default_x1234 = [0.6, 0.9, 1.7, 2.2] # Gaussian kernel widths for x1, x2, x3, x4
    noise_level_model = noise_level_img/255.  # noise level of model
    kernel_width = kernel_width_default_x1234[sf-1]

    """
    # set your own kernel width !!!!!!!!!!
    """
    # kernel_width = 1.0


    k = utils_deblur.fspecial('gaussian', 25, kernel_width)
    
    # caused error
    #k = sr.shift_pixel(k, sf)  # shift the kernel
    k /= np.sum(k)

    ##############################################################################


    show_img = False
    util.surf(k) if show_img else None
    x8 = True                            # default: False, x8 to boost performance
    modelSigma1 = 49                     # set sigma_1, default: 49
    modelSigma2 = max(sf, noise_level_model*255.)
    classical_degradation = True         # set classical degradation or bicubic degradation

    task_current = 'sr'                  # 'sr' for super-resolution
    n_channels = 1 if 'gray' in model_name else 3  # fixed
    model_zoo = 'model_zoo'              # fixed
    testsets = 'testsets'                # fixed
    results = 'results'                  # fixed
    result_name = testset_name + '_realapplications_' + task_current + '_' + model_name
    model_path = os.path.join(model_zoo, model_name+'.pth')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    torch.cuda.empty_cache()

    # ----------------------------------------
    # L_path, E_path, H_path
    # ----------------------------------------
    L_path = os.path.join(testsets, testset_name) # L_path, for Low-quality images
    E_path = os.path.join(results, result_name)   # E_path, for Estimated images
    util.mkdir(E_path)

    logger_name = result_name
    utils_logger.logger_info(logger_name, log_path=os.path.join(E_path, logger_name+'.log'))
    logger = logging.getLogger(logger_name)

    # ----------------------------------------
    # load model
    # ----------------------------------------
    if 'drunet' in model_name:
        from models.network_unet import UNetRes as net
        model = net(in_nc=n_channels+1, out_nc=n_channels, nc=[64, 128, 256, 512], nb=4, act_mode='R', downsample_mode="strideconv", upsample_mode="convtranspose")
        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        for _, v in model.named_parameters():
            v.requires_grad = False
        model = model.to(device)
    elif 'ircnn' in model_name:
        from models.network_dncnn import IRCNN as net
        model = net(in_nc=n_channels, out_nc=n_channels, nc=64)
        model25 = torch.load(model_path)
        former_idx = 0

    logger.info('model_name:{}, image sigma:{:.3f}, model sigma:{:.3f}'.format(model_name, noise_level_img, noise_level_model))
    logger.info('Model path: {:s}'.format(model_path))
    logger.info(L_path)
    L_paths = util.get_image_paths(L_path)

    for idx, img in enumerate(L_paths):

        # --------------------------------
        # (1) get img_L
        # --------------------------------
        logger.info('Model path: {:s} Image: {:s}'.format(model_path, img))
        img_name, ext = os.path.splitext(os.path.basename(img))
        img_L = util.imread_uint(img, n_channels=n_channels)
        img_L = util.uint2single(img_L)
        img_L = util.modcrop(img_L, 8)  # modcrop

        # --------------------------------
        # (2) get rhos and sigmas
        # --------------------------------
        rhos, sigmas = pnp.get_rho_sigma(sigma=max(0.255/255., noise_level_model), iter_num=iter_num, modelSigma1=modelSigma1, modelSigma2=modelSigma2, w=1)
        rhos, sigmas = torch.tensor(rhos).to(device), torch.tensor(sigmas).to(device)

        # --------------------------------
        # (3) initialize x, and pre-calculation
        # --------------------------------
        x = cv2.resize(img_L, (img_L.shape[1]*sf, img_L.shape[0]*sf), interpolation=cv2.INTER_CUBIC)

        if np.ndim(x)==2:
            x = x[..., None]

        if classical_degradation:
            #x = sr.shift_pixel(x, sf)
            print("shift_pixel: ",x, sf)
        x = util.single2tensor4(x).to(device)

        img_L_tensor, k_tensor = util.single2tensor4(img_L), util.single2tensor4(np.expand_dims(k, 2))
        [k_tensor, img_L_tensor] = util.todevice([k_tensor, img_L_tensor], device)
        FB, FBC, F2B, FBFy = sr.pre_calculate(img_L_tensor, k_tensor, sf)

        # --------------------------------
        # (4) main iterations
        # --------------------------------
        for i in range(iter_num):

            print('Iter: {} / {}'.format(i, iter_num))

            # --------------------------------
            # step 1, FFT
            # --------------------------------
            tau = rhos[i].float().repeat(1, 1, 1, 1)
            x = sr.data_solution(x, FB, FBC, F2B, FBFy, tau, sf)

            if 'ircnn' in model_name:
                current_idx = np.int(np.ceil(sigmas[i].cpu().numpy()*255./2.)-1)
    
                if current_idx != former_idx:
                    model.load_state_dict(model25[str(current_idx)], strict=True)
                    model.eval()
                    for _, v in model.named_parameters():
                        v.requires_grad = False
                    model = model.to(device)
                former_idx = current_idx

            # --------------------------------
            # step 2, denoiser
            # --------------------------------
            if x8:
                x = util.augment_img_tensor4(x, i % 8)
                
            if 'drunet' in model_name:
                x = torch.cat((x, sigmas[i].repeat(1, 1, x.shape[2], x.shape[3])), dim=1)
                x = utils_model.test_mode(model, x, mode=2, refield=64, min_size=256, modulo=16)
            elif 'ircnn' in model_name:
                x = model(x)

            if x8:
                if i % 8 == 3 or i % 8 == 5:
                    x = util.augment_img_tensor4(x, 8 - i % 8)
                else:
                    x = util.augment_img_tensor4(x, i % 8)

        # --------------------------------
        # (3) img_E
        # --------------------------------
        img_E = util.tensor2uint(x)
        util.imsave(img_E, os.path.join(E_path, img_name+'_x'+str(sf)+'_'+model_name+'NOV.png'))

if __name__ == '__main__':

    main()


!ls ../*.png

img = "../sienfield.png"

im = cv2.imread(img)
n_channels = 3
img_L = util.imread_uint(img, n_channels=n_channels)


img = "../sienfield.png"

im = cv2.imread(img)
n_channels = 3
img_L = util.imread_uint(img, n_channels=n_channels)


# %load main_dpir_sisr.py
import os.path
import glob
import cv2
import logging
import time

import numpy as np
from datetime import datetime
from collections import OrderedDict
import hdf5storage

import torch

from utils import utils_deblur
from utils import utils_logger
from utils import utils_model
from utils import utils_pnp as pnp
from utils import utils_sisr as sr
from utils import utils_image as util


"""
Spyder (Python 3.7)
PyTorch 1.6.0
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/DPIR
        https://github.com/cszn/IRCNN
        https://github.com/cszn/KAIR
@article{zhang2020plug,
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={arXiv preprint},
  year={2020}
}
% If you have any question, please feel free to contact with me.
% Kai Zhang (e-mail: cskaizhang@gmail.com; homepage: https://cszn.github.io/)
by Kai Zhang (01/August/2020)

# --------------------------------------------
|--model_zoo               # model_zoo
   |--drunet_color         # model_name, for color images
   |--drunet_gray
|--testset                 # testsets
|--results                 # results
# --------------------------------------------


How to run:
step 1: download [drunet_gray.pth, drunet_color.pth, ircnn_gray.pth, ircnn_color.pth] from https://drive.google.com/drive/folders/13kfr3qny7S2xwG9h7v95F5mkWs0OmU0D
step 2: set your own testset 'testset_name' and parameter setting such as 'noise_level_img', 'iter_num'. 
step 3: 'python main_dpir_sisr.py'

"""

def main():

    # ----------------------------------------
    # Preparation
    # ----------------------------------------

    noise_level_img = 0/255.0            # set AWGN noise level for LR image, default: 0, 
    noise_level_model = noise_level_img  # setnoise level of model, default 0
    model_name = 'drunet_color'          # set denoiser, | 'drunet_color' | 'ircnn_gray' | 'drunet_gray' | 'ircnn_color'
    testset_name = 'srbsd68'             # set test set,  'set5' | 'srbsd68'
    x8 = True                            # default: False, x8 to boost performance
    test_sf = [2]                        # set scale factor, default: [2, 3, 4], [2], [3], [4]
    iter_num = 24                        # set number of iterations, default: 24 for SISR
    modelSigma1 = 49                     # set sigma_1, default: 49
    classical_degradation = True         # set classical degradation or bicubic degradation

    show_img = False                     # default: False
    save_L = True                        # save LR image
    save_E = True                        # save estimated image
    save_LEH = False                     # save zoomed LR, E and H images

    task_current = 'sr'                  # 'sr' for super-resolution
    n_channels = 1 if 'gray' in model_name else 3  # fixed
    model_zoo = 'model_zoo'              # fixed
    testsets = 'testsets'                # fixed
    results = 'results'                  # fixed
    result_name = testset_name + '_' + task_current + '_' + model_name
    model_path = os.path.join(model_zoo, model_name+'.pth')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    torch.cuda.empty_cache()

    # ----------------------------------------
    # L_path, E_path, H_path
    # ----------------------------------------

    L_path = os.path.join(testsets, testset_name) # L_path, for Low-quality images
    E_path = os.path.join(results, result_name)   # E_path, for Estimated images
    util.mkdir(E_path)

    logger_name = result_name
    utils_logger.logger_info(logger_name, log_path=os.path.join(E_path, logger_name+'.log'))
    logger = logging.getLogger(logger_name)

    # ----------------------------------------
    # load model
    # ----------------------------------------

    if 'drunet' in model_name:
        from models.network_unet import UNetRes as net
        model = net(in_nc=n_channels+1, out_nc=n_channels, nc=[64, 128, 256, 512], nb=4, act_mode='R', downsample_mode="strideconv", upsample_mode="convtranspose")
        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        for _, v in model.named_parameters():
            v.requires_grad = False
        model = model.to(device)
    elif 'ircnn' in model_name:
        from models.network_dncnn import IRCNN as net
        model = net(in_nc=n_channels, out_nc=n_channels, nc=64)
        model25 = torch.load(model_path)
        former_idx = 0

    logger.info('model_name:{}, image sigma:{:.3f}, model sigma:{:.3f}'.format(model_name, noise_level_img, noise_level_model))
    logger.info('Model path: {:s}'.format(model_path))
    logger.info(L_path)
    L_paths = util.get_image_paths(L_path)

    # --------------------------------
    # load kernel
    # --------------------------------

    # kernels = hdf5storage.loadmat(os.path.join('kernels', 'Levin09.mat'))['kernels']
    if classical_degradation:
        kernels = hdf5storage.loadmat(os.path.join('kernels', 'kernels_12.mat'))['kernels']
    else:
        kernels = hdf5storage.loadmat(os.path.join('kernels', 'kernel_bicubicx234.mat'))['kernels']

    test_results_ave = OrderedDict()
    test_results_ave['psnr_sf_k'] = []
    test_results_ave['psnr_y_sf_k'] = []

    for sf in test_sf:
        border = sf
        modelSigma2 = max(sf, noise_level_model*255.)
        k_num = 8 if classical_degradation else 1

        for k_index in range(k_num):
            logger.info('--------- sf:{:>1d} --k:{:>2d} ---------'.format(sf, k_index))
            test_results = OrderedDict()
            test_results['psnr'] = []
            test_results['psnr_y'] = []

            if not classical_degradation:  # for bicubic degradation
                k_index = sf-2
            k = kernels[0, k_index].astype(np.float64)

            util.surf(k) if show_img else None

            for idx, img in enumerate(L_paths):

                # --------------------------------
                # (1) get img_L
                # --------------------------------

                img_name, ext = os.path.splitext(os.path.basename(img))
                img_H = util.imread_uint(img, n_channels=n_channels)
                img_H = util.modcrop(img_H, sf)  # modcrop

                if classical_degradation:
                    #img_L = sr.classical_degradation(img_H, k, sf)
                    img = "../sienfield.png"

                    im = cv2.imread(img)
                    n_channels = 3
                    img_L = util.imread_uint(img, n_channels=n_channels)
                    util.imshow(img_L) if show_img else None
                    img_L = util.uint2single(img_L)
                else:
                    img_L = util.imresize_np(util.uint2single(img_H), 1/sf)

                np.random.seed(seed=0)  # for reproducibility
                img_L += np.random.normal(0, noise_level_img, img_L.shape) # add AWGN

                # --------------------------------
                # (2) get rhos and sigmas
                # --------------------------------

                rhos, sigmas = pnp.get_rho_sigma(sigma=max(0.255/255., noise_level_model), iter_num=iter_num, modelSigma1=modelSigma1, modelSigma2=modelSigma2, w=1)
                rhos, sigmas = torch.tensor(rhos).to(device), torch.tensor(sigmas).to(device)

                # --------------------------------
                # (3) initialize x, and pre-calculation
                # --------------------------------

                x = cv2.resize(img_L, (img_L.shape[1]*sf, img_L.shape[0]*sf), interpolation=cv2.INTER_CUBIC)
                if np.ndim(x)==2:
                    x = x[..., None]

                if classical_degradation:
                    #x = sr.shift_pixel(x, sf)
                    print(x,sf)
                x = util.single2tensor4(x).to(device)

                img_L_tensor, k_tensor = util.single2tensor4(img_L), util.single2tensor4(np.expand_dims(k, 2))
                [k_tensor, img_L_tensor] = util.todevice([k_tensor, img_L_tensor], device)
                FB, FBC, F2B, FBFy = sr.pre_calculate(img_L_tensor, k_tensor, sf)

                # --------------------------------
                # (4) main iterations
                # --------------------------------

                for i in range(iter_num):

                    # --------------------------------
                    # step 1, FFT
                    # --------------------------------

                    tau = rhos[i].float().repeat(1, 1, 1, 1)
                    x = sr.data_solution(x.float(), FB, FBC, F2B, FBFy, tau, sf)

                    if 'ircnn' in model_name:
                        current_idx = np.int(np.ceil(sigmas[i].cpu().numpy()*255./2.)-1)
            
                        if current_idx != former_idx:
                            model.load_state_dict(model25[str(current_idx)], strict=True)
                            model.eval()
                            for _, v in model.named_parameters():
                                v.requires_grad = False
                            model = model.to(device)
                        former_idx = current_idx

                    # --------------------------------
                    # step 2, denoiser
                    # --------------------------------

                    if x8:
                        x = util.augment_img_tensor4(x, i % 8)
                        
                    if 'drunet' in model_name:
                        x = torch.cat((x, sigmas[i].float().repeat(1, 1, x.shape[2], x.shape[3])), dim=1)
                        x = utils_model.test_mode(model, x, mode=2, refield=32, min_size=256, modulo=16)
                    elif 'ircnn' in model_name:
                        x = model(x)

                    if x8:
                        if i % 8 == 3 or i % 8 == 5:
                            x = util.augment_img_tensor4(x, 8 - i % 8)
                        else:
                            x = util.augment_img_tensor4(x, i % 8)

                # --------------------------------
                # (3) img_E
                # --------------------------------

                img_E = util.tensor2uint(x)

                if save_E:
                    util.imsave(img_E, os.path.join(E_path, img_name+'_x'+str(sf)+'_k'+str(k_index)+'_'+model_name+'.png'))

                if n_channels == 1:
                    img_H = img_H.squeeze()

                # --------------------------------
                # (4) img_LEH
                # --------------------------------

                img_L = util.single2uint(img_L).squeeze()

                if save_LEH:
                    k_v = k/np.max(k)*1.0
                    if n_channels==1:
                        k_v = util.single2uint(k_v)
                    else:
                        k_v = util.single2uint(np.tile(k_v[..., np.newaxis], [1, 1, n_channels]))
                    k_v = cv2.resize(k_v, (3*k_v.shape[1], 3*k_v.shape[0]), interpolation=cv2.INTER_NEAREST)
                    img_I = cv2.resize(img_L, (sf*img_L.shape[1], sf*img_L.shape[0]), interpolation=cv2.INTER_NEAREST)
                    img_I[:k_v.shape[0], -k_v.shape[1]:, ...] = k_v
                    img_I[:img_L.shape[0], :img_L.shape[1], ...] = img_L
                    util.imshow(np.concatenate([img_I, img_E, img_H], axis=1), title='LR / Recovered / Ground-truth') if show_img else None
                    util.imsave(np.concatenate([img_I, img_E, img_H], axis=1), os.path.join(E_path, img_name+'_x'+str(sf)+'_k'+str(k_index)+'_LEH.png'))

                if save_L:
                    util.imsave(img_L, os.path.join(E_path, img_name+'_x'+str(sf)+'_k'+str(k_index)+'_LR.png'))

                psnr = util.calculate_psnr(img_E, img_H, border=border)
                test_results['psnr'].append(psnr)
                logger.info('{:->4d}--> {:>10s} -- sf:{:>1d} --k:{:>2d} PSNR: {:.2f}dB'.format(idx+1, img_name+ext, sf, k_index, psnr))

                if n_channels == 3:
                    img_E_y = util.rgb2ycbcr(img_E, only_y=True)
                    img_H_y = util.rgb2ycbcr(img_H, only_y=True)
                    psnr_y = util.calculate_psnr(img_E_y, img_H_y, border=border)
                    test_results['psnr_y'].append(psnr_y)

            # --------------------------------
            # Average PSNR for all kernels
            # --------------------------------

            ave_psnr_k = sum(test_results['psnr']) / len(test_results['psnr'])
            logger.info('------> Average PSNR(RGB) of ({}) scale factor: ({}), kernel: ({}) sigma: ({:.2f}): {:.2f} dB'.format(testset_name, sf, k_index, noise_level_model, ave_psnr_k))
            test_results_ave['psnr_sf_k'].append(ave_psnr_k)

            if n_channels == 3:  # RGB image
                ave_psnr_y_k = sum(test_results['psnr_y']) / len(test_results['psnr_y'])
                logger.info('------> Average PSNR(Y) of ({}) scale factor: ({}), kernel: ({}) sigma: ({:.2f}): {:.2f} dB'.format(testset_name, sf, k_index, noise_level_model, ave_psnr_y_k))
                test_results_ave['psnr_y_sf_k'].append(ave_psnr_y_k)

    # ---------------------------------------
    # Average PSNR for all sf and kernels
    # ---------------------------------------

    ave_psnr_sf_k = sum(test_results_ave['psnr_sf_k']) / len(test_results_ave['psnr_sf_k'])
    logger.info('------> Average PSNR of ({}) {:.2f} dB'.format(testset_name, ave_psnr_sf_k))
    if n_channels == 3:
        ave_psnr_y_sf_k = sum(test_results_ave['psnr_y_sf_k']) / len(test_results_ave['psnr_y_sf_k'])
        logger.info('------> Average PSNR of ({}) {:.2f} dB'.format(testset_name, ave_psnr_y_sf_k))

if __name__ == '__main__':

    main()


img_I = cv2.resize(img_L, (sf*img_L.shape[1], sf*img_L.shape[0]), interpolation=cv2.INTER_NEAREST)
img_I[:k_v.shape[0], -k_v.shape[1]:, ...] = k_v
img_I[:img_L.shape[0], :img_L.shape[1], ...] = img_L
util.imshow(np.concatenate([img_I, img_E, img_H], axis=1), title='LR / Recovered / Ground-truth') 

!mkdir testsets/srbsd68

import utils
print(utils.__file__)

#main_dpir_sisr.py
import os.path
import glob
import cv2
import logging
import time

import numpy as np
from datetime import datetime
from collections import OrderedDict
import hdf5storage

import torch

from utils import utils_deblur
from utils import utils_logger
from utils import utils_model
from utils import utils_pnp as pnp
from utils import utils_sisr as sr
from utils import utils_image as util


"""
Spyder (Python 3.7)
PyTorch 1.6.0
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/DPIR
        https://github.com/cszn/IRCNN
        https://github.com/cszn/KAIR
@article{zhang2020plug,
  title={Plug-and-Play Image Restoration with Deep Denoiser Prior},
  author={Zhang, Kai and Li, Yawei and Zuo, Wangmeng and Zhang, Lei and Van Gool, Luc and Timofte, Radu},
  journal={arXiv preprint},
  year={2020}
}
% If you have any question, please feel free to contact with me.
% Kai Zhang (e-mail: cskaizhang@gmail.com; homepage: https://cszn.github.io/)
by Kai Zhang (01/August/2020)

# --------------------------------------------
|--model_zoo               # model_zoo
   |--drunet_color         # model_name, for color images
   |--drunet_gray
|--testset                 # testsets
|--results                 # results
# --------------------------------------------


How to run:
step 1: download [drunet_gray.pth, drunet_color.pth, ircnn_gray.pth, ircnn_color.pth] from https://drive.google.com/drive/folders/13kfr3qny7S2xwG9h7v95F5mkWs0OmU0D
step 2: set your own testset 'testset_name' and parameter setting such as 'noise_level_img', 'iter_num'. 
step 3: 'python main_dpir_sisr.py'

"""

def main():

    # ----------------------------------------
    # Preparation
    # ----------------------------------------

    noise_level_img = 0/255.0            # set AWGN noise level for LR image, default: 0, 
    noise_level_model = noise_level_img  # setnoise level of model, default 0
    model_name = 'drunet_color'          # set denoiser, | 'drunet_color' | 'ircnn_gray' | 'drunet_gray' | 'ircnn_color'
    testset_name = 'srbsd68'             # set test set,  'set5' | 'srbsd68'
    x8 = True                            # default: False, x8 to boost performance
    test_sf = [2]                        # set scale factor, default: [2, 3, 4], [2], [3], [4]
    iter_num = 24                        # set number of iterations, default: 24 for SISR
    modelSigma1 = 49                     # set sigma_1, default: 49
    classical_degradation = True         # set classical degradation or bicubic degradation

    show_img = False                     # default: False
    save_L = True                        # save LR image
    save_E = True                        # save estimated image
    save_LEH = False                     # save zoomed LR, E and H images

    task_current = 'sr'                  # 'sr' for super-resolution
    n_channels = 1 if 'gray' in model_name else 3  # fixed
    model_zoo = 'model_zoo'              # fixed
    testsets = 'testsets'                # fixed
    results = 'results'                  # fixed
    result_name = testset_name + '_' + task_current + '_' + model_name
    model_path = os.path.join(model_zoo, model_name+'.pth')
    device = torch.device('cpu')#' if torch.cuda.is_available() else 'cpu')
    torch.cuda.empty_cache()

    # ----------------------------------------
    # L_path, E_path, H_path
    # ----------------------------------------

    L_path = os.path.join(testsets, testset_name) # L_path, for Low-quality images
    E_path = os.path.join(results, result_name)   # E_path, for Estimated images
    util.mkdir(E_path)

    logger_name = result_name
    utils_logger.logger_info(logger_name, log_path=os.path.join(E_path, logger_name+'.log'))
    logger = logging.getLogger(logger_name)

    # ----------------------------------------
    # load model
    # ----------------------------------------

    if 'drunet' in model_name:
        from models.network_unet import UNetRes as net
        model = net(in_nc=n_channels+1, out_nc=n_channels, nc=[64, 128, 256, 512], nb=4, act_mode='R', downsample_mode="strideconv", upsample_mode="convtranspose")
        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        for _, v in model.named_parameters():
            v.requires_grad = False
        model = model.to(device)
    elif 'ircnn' in model_name:
        from models.network_dncnn import IRCNN as net
        model = net(in_nc=n_channels, out_nc=n_channels, nc=64)
        model25 = torch.load(model_path)
        former_idx = 0

    logger.info('model_name:{}, image sigma:{:.3f}, model sigma:{:.3f}'.format(model_name, noise_level_img, noise_level_model))
    logger.info('Model path: {:s}'.format(model_path))
    logger.info(L_path)
    L_paths = util.get_image_paths(L_path)

    # --------------------------------
    # load kernel
    # --------------------------------

    # kernels = hdf5storage.loadmat(os.path.join('kernels', 'Levin09.mat'))['kernels']
    if classical_degradation:
        kernels = hdf5storage.loadmat(os.path.join('kernels', 'kernels_12.mat'))['kernels']
    else:
        kernels = hdf5storage.loadmat(os.path.join('kernels', 'kernel_bicubicx234.mat'))['kernels']

    test_results_ave = OrderedDict()
    test_results_ave['psnr_sf_k'] = []
    test_results_ave['psnr_y_sf_k'] = []

    for sf in test_sf:
        border = sf
        modelSigma2 = max(sf, noise_level_model*255.)
        k_num = 8 if classical_degradation else 1

        for k_index in range(k_num):
            logger.info('--------- sf:{:>1d} --k:{:>2d} ---------'.format(sf, k_index))
            test_results = OrderedDict()
            test_results['psnr'] = []
            test_results['psnr_y'] = []

            if not classical_degradation:  # for bicubic degradation
                k_index = sf-2
            k = kernels[0, k_index].astype(np.float64)

            util.surf(k) if show_img else None

            for idx, img in enumerate(L_paths):

                # --------------------------------
                # (1) get img_L
                # --------------------------------

                img_name, ext = os.path.splitext(os.path.basename(img))
                img_H = util.imread_uint(img, n_channels=n_channels)
                img_H = util.modcrop(img_H, sf)  # modcrop

                if classical_degradation:
                    img_L = sr.classical_degradation(img_H, k, sf)
                    util.imshow(img_L) if show_img else None
                    img_L = util.uint2single(img_L)
                else:
                    img_L = util.imresize_np(util.uint2single(img_H), 1/sf)

                np.random.seed(seed=0)  # for reproducibility
                img_L += np.random.normal(0, noise_level_img, img_L.shape) # add AWGN

                # --------------------------------
                # (2) get rhos and sigmas
                # --------------------------------

                rhos, sigmas = pnp.get_rho_sigma(sigma=max(0.255/255., noise_level_model), iter_num=iter_num, modelSigma1=modelSigma1, modelSigma2=modelSigma2, w=1)
                rhos, sigmas = torch.tensor(rhos).to(device), torch.tensor(sigmas).to(device)

                # --------------------------------
                # (3) initialize x, and pre-calculation
                # --------------------------------

                x = cv2.resize(img_L, (img_L.shape[1]*sf, img_L.shape[0]*sf), interpolation=cv2.INTER_CUBIC)
                if np.ndim(x)==2:
                    x = x[..., None]

                if classical_degradation:
                    x = sr.shift_pixel(x, sf)
                x = util.single2tensor4(x).to(device)

                img_L_tensor, k_tensor = util.single2tensor4(img_L), util.single2tensor4(np.expand_dims(k, 2))
                [k_tensor, img_L_tensor] = util.todevice([k_tensor, img_L_tensor], device)
                FB, FBC, F2B, FBFy = sr.pre_calculate(img_L_tensor, k_tensor, sf)

                # --------------------------------
                # (4) main iterations
                # --------------------------------

                for i in range(iter_num):

                    # --------------------------------
                    # step 1, FFT
                    # --------------------------------

                    tau = rhos[i].float().repeat(1, 1, 1, 1)
                    x = sr.data_solution(x.float(), FB, FBC, F2B, FBFy, tau, sf)

                    if 'ircnn' in model_name:
                        current_idx = np.int(np.ceil(sigmas[i].cpu().numpy()*255./2.)-1)
            
                        if current_idx != former_idx:
                            model.load_state_dict(model25[str(current_idx)], strict=True)
                            model.eval()
                            for _, v in model.named_parameters():
                                v.requires_grad = False
                            model = model.to(device)
                        former_idx = current_idx

                    # --------------------------------
                    # step 2, denoiser
                    # --------------------------------

                    if x8:
                        x = util.augment_img_tensor4(x, i % 8)
                        
                    if 'drunet' in model_name:
                        x = torch.cat((x, sigmas[i].float().repeat(1, 1, x.shape[2], x.shape[3])), dim=1)
                        x = utils_model.test_mode(model, x, mode=2, refield=32, min_size=256, modulo=16)
                    elif 'ircnn' in model_name:
                        x = model(x)

                    if x8:
                        if i % 8 == 3 or i % 8 == 5:
                            x = util.augment_img_tensor4(x, 8 - i % 8)
                        else:
                            x = util.augment_img_tensor4(x, i % 8)

                # --------------------------------
                # (3) img_E
                # --------------------------------

                img_E = util.tensor2uint(x)

                if save_E:
                    util.imsave(img_E, os.path.join(E_path, img_name+'_x'+str(sf)+'_k'+str(k_index)+'_'+model_name+'.png'))

                if n_channels == 1:
                    img_H = img_H.squeeze()

                # --------------------------------
                # (4) img_LEH
                # --------------------------------

                img_L = util.single2uint(img_L).squeeze()

                if save_LEH:
                    k_v = k/np.max(k)*1.0
                    if n_channels==1:
                        k_v = util.single2uint(k_v)
                    else:
                        k_v = util.single2uint(np.tile(k_v[..., np.newaxis], [1, 1, n_channels]))
                    k_v = cv2.resize(k_v, (3*k_v.shape[1], 3*k_v.shape[0]), interpolation=cv2.INTER_NEAREST)
                    img_I = cv2.resize(img_L, (sf*img_L.shape[1], sf*img_L.shape[0]), interpolation=cv2.INTER_NEAREST)
                    img_I[:k_v.shape[0], -k_v.shape[1]:, ...] = k_v
                    img_I[:img_L.shape[0], :img_L.shape[1], ...] = img_L
                    util.imshow(np.concatenate([img_I, img_E, img_H], axis=1), title='LR / Recovered / Ground-truth') if show_img else None
                    util.imsave(np.concatenate([img_I, img_E, img_H], axis=1), os.path.join(E_path, img_name+'_x'+str(sf)+'_k'+str(k_index)+'_LEH.png'))

                if save_L:
                    util.imsave(img_L, os.path.join(E_path, img_name+'_x'+str(sf)+'_k'+str(k_index)+'_LR.png'))

                psnr = util.calculate_psnr(img_E, img_H, border=border)
                test_results['psnr'].append(psnr)
                logger.info('{:->4d}--> {:>10s} -- sf:{:>1d} --k:{:>2d} PSNR: {:.2f}dB'.format(idx+1, img_name+ext, sf, k_index, psnr))

                if n_channels == 3:
                    img_E_y = util.rgb2ycbcr(img_E, only_y=True)
                    img_H_y = util.rgb2ycbcr(img_H, only_y=True)
                    psnr_y = util.calculate_psnr(img_E_y, img_H_y, border=border)
                    test_results['psnr_y'].append(psnr_y)

            # --------------------------------
            # Average PSNR for all kernels
            # --------------------------------

            ave_psnr_k = sum(test_results['psnr']) / len(test_results['psnr'])
            logger.info('------> Average PSNR(RGB) of ({}) scale factor: ({}), kernel: ({}) sigma: ({:.2f}): {:.2f} dB'.format(testset_name, sf, k_index, noise_level_model, ave_psnr_k))
            test_results_ave['psnr_sf_k'].append(ave_psnr_k)

            if n_channels == 3:  # RGB image
                ave_psnr_y_k = sum(test_results['psnr_y']) / len(test_results['psnr_y'])
                logger.info('------> Average PSNR(Y) of ({}) scale factor: ({}), kernel: ({}) sigma: ({:.2f}): {:.2f} dB'.format(testset_name, sf, k_index, noise_level_model, ave_psnr_y_k))
                test_results_ave['psnr_y_sf_k'].append(ave_psnr_y_k)

    # ---------------------------------------
    # Average PSNR for all sf and kernels
    # ---------------------------------------

    ave_psnr_sf_k = sum(test_results_ave['psnr_sf_k']) / len(test_results_ave['psnr_sf_k'])
    logger.info('------> Average PSNR of ({}) {:.2f} dB'.format(testset_name, ave_psnr_sf_k))
    if n_channels == 3:
        ave_psnr_y_sf_k = sum(test_results_ave['psnr_y_sf_k']) / len(test_results_ave['psnr_y_sf_k'])
        logger.info('------> Average PSNR of ({}) {:.2f} dB'.format(testset_name, ave_psnr_y_sf_k))

if __name__ == '__main__':

    main()


import utils.utils_sisr
dir (utils.utils_sisr)

import torch.fft
import torch


def splits(a, sf):
    '''split a into sfxsf distinct blocks
    Args:
        a: NxCxWxH
        sf: split factor
    Returns:
        b: NxCx(W/sf)x(H/sf)x(sf^2)
    '''
    b = torch.stack(torch.chunk(a, sf, dim=2), dim=4)
    b = torch.cat(torch.chunk(b, sf, dim=3), dim=4)
    return b


def p2o(psf, shape):
    '''
    Convert point-spread function to optical transfer function.
    otf = p2o(psf) computes the Fast Fourier Transform (FFT) of the
    point-spread function (PSF) array and creates the optical transfer
    function (OTF) array that is not influenced by the PSF off-centering.
    Args:
        psf: NxCxhxw
        shape: [H, W]
    Returns:
        otf: NxCxHxWx2
    '''
    otf = torch.zeros(psf.shape[:-2] + shape).type_as(psf)
    otf[...,:psf.shape[2],:psf.shape[3]].copy_(psf)
    for axis, axis_size in enumerate(psf.shape[2:]):
        otf = torch.roll(otf, -int(axis_size / 2), dims=axis+2)
    otf = torch.fft.fftn(otf, dim=(-2,-1))
    #n_ops = torch.sum(torch.tensor(psf.shape).type_as(psf) * torch.log2(torch.tensor(psf.shape).type_as(psf)))
    #otf[..., 1][torch.abs(otf[..., 1]) < n_ops*2.22e-16] = torch.tensor(0).type_as(psf)
    return otf


def upsample(x, sf=3):
    '''s-fold upsampler
    Upsampling the spatial size by filling the new entries with zeros
    x: tensor image, NxCxWxH
    '''
    st = 0
    z = torch.zeros((x.shape[0], x.shape[1], x.shape[2]*sf, x.shape[3]*sf)).type_as(x)
    z[..., st::sf, st::sf].copy_(x)
    return z


def downsample(x, sf=3):
    '''s-fold downsampler
    Keeping the upper-left pixel for each distinct sfxsf patch and discarding the others
    x: tensor image, NxCxWxH
    '''
    st = 0
    return x[..., st::sf, st::sf]



def data_solution(x, FB, FBC, F2B, FBFy, alpha, sf):
    FR = FBFy + torch.fft.fftn(alpha*x, dim=(-2,-1))
    x1 = FB.mul(FR)
    FBR = torch.mean(splits(x1, sf), dim=-1, keepdim=False)
    invW = torch.mean(splits(F2B, sf), dim=-1, keepdim=False)
    invWBR = FBR.div(invW + alpha)
    FCBinvWBR = FBC*invWBR.repeat(1, 1, sf, sf)
    FX = (FR-FCBinvWBR)/alpha
    Xest = torch.real(torch.fft.ifftn(FX, dim=(-2, -1)))

    return Xest


def pre_calculate(x, k, sf):
    '''
    Args:
        x: NxCxHxW, LR input
        k: NxCxhxw
        sf: integer

    Returns:
        FB, FBC, F2B, FBFy
        will be reused during iterations
    '''
    w, h = x.shape[-2:]
    FB = p2o(k, (w*sf, h*sf))
    FBC = torch.conj(FB)
    F2B = torch.pow(torch.abs(FB), 2)
    STy = upsample(x, sf=sf)
    FBFy = FBC*torch.fft.fftn(STy, dim=(-2, -1))
    return FB, FBC, F2B, FBFy

















