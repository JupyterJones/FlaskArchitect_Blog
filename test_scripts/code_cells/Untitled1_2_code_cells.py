https://github.com/jixiaozhong/RealSR

You can prepend the env variable to the build command:

USE_NNPACK=0 python setup.py install

or set it via:

export USE_NNPACK=0

before building PyTorch from source.

Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/BSRGAN
        https://github.com/cszn/KAIR
@inproceedings{zhang2021designing,
Designing a Practical Degradation Model 
for Deep Blind Image Super-Resolution},
author={Zhang, Kai and Liang, Jingyun and Van Gool, Luc and Timofte, Radu}            

os.environ["CUDA_VISIBLE_DEVICES"]=""

import os.path
import logging
import torch
import sys
import os
sys.path.append('/home/jack/Desktop/BSRGAN')
#from utils import utils_image
import utils_image
#sys.path.remove('/home/jack/hidden')
#sys.path
from python_utils.logger import Logged
import python_utils.logger
#import python_utils
#from utils import utils_logger
#from utils import utils_image as util
# from utils import utils_model
from models.network_rrdbnet import RRDBNet as net
os.environ["CUDA_VISIBLE_DEVICES"]=""

"""
Spyder (Python 3.6-3.7)
PyTorch 1.4.0-1.8.1
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/BSRGAN
        https://github.com/cszn/KAIR
If you have any question, please feel free to contact with me.
Kai Zhang (e-mail: cskaizhang@gmail.com)
by Kai Zhang ( March/2020 --> March/2021 --> )
This work was previously submitted to CVPR2021.

# --------------------------------------------
@inproceedings{zhang2021designing,
  title={Designing a Practical Degradation Model for Deep Blind Image Super-Resolution},
  author={Zhang, Kai and Liang, Jingyun and Van Gool, Luc and Timofte, Radu},
  booktitle={arxiv},
  year={2021}
}
# --------------------------------------------

"""


def main(cnt):

    #utils_logger.logger_info('blind_sr_log', log_path='blind_sr_log.log')
    Logged.info('blind_sr_log', log_path='blind_sr_log.log')
    #python_utils.logger('blind_sr_log', log_path='blind_sr_log.log')
    #logger = logging.getLogger('blind_sr_log')

#    print(torch.__version__)               # pytorch version
#    print(torch.version.cuda)              # cuda version
#    print(torch.backends.cudnn.version())  # cudnn version

    testsets = 'testsets'       # fixed, set path of testsets
    testset_Ls = ['RealSRSet']  # ['RealSRSet','DPED']

    model_names = ['RRDB','ESRGAN','FSSR_DPED','FSSR_JPEG','RealSR_DPED','RealSR_JPEG','BSRGANx2']
    #model_names = ['FSSR_DPED']    # 'BSRGANx2' for scale factor 2



    save_results = True
    sf = 4
    device = torch.device('cpu')# if torch.cuda.is_available() else 'cpu')

    for model_name in model_names:
        if model_name in ['BSRGANx2']:
            sf = 2
        model_path = os.path.join('model_zoo', model_name+'.pth')          # set model path
        Logged.logger.info('{:>16s} : {:s}'.format('Model Name', model_name))
        # torch.cuda.set_device(0)      # set GPU ID
        #Logged.logger.info('{:>16s} : {:<d}'.format('GPU ID', torch.cuda.current_device()))
        #torch.cuda.empty_cache()

        # --------------------------------
        # define network and load model
        # --------------------------------
        model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=sf)  # define network

#            model_old = torch.load(model_path)
#            state_dict = model.state_dict()
#            for ((key, param),(key2, param2)) in zip(model_old.items(), state_dict.items()):
#                state_dict[key2] = param
#            model.load_state_dict(state_dict, strict=True)

        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        for k, v in model.named_parameters():
            v.requires_grad = False
        model = model.to(device)
        torch.cuda.empty_cache()

        for testset_L in testset_Ls:

            L_path = os.path.join(testsets, testset_L)
            #E_path = os.path.join(testsets, testset_L+'_'+model_name)
            E_path = os.path.join(testsets, testset_L+'_results_x'+str(sf))
            try:
                os.makedirs(E_path)
            except FileExistsError:
                # directory already exists
                pass
 
            Logged.logger.info('{:>16s} : {:s}'.format('Input Path', L_path))
            Logged.logger.info('{:>16s} : {:s}'.format('Output Path', E_path))
            idx = 0

            for img in utils_image.get_image_paths(L_path):

                # --------------------------------
                # (1) img_L
                # --------------------------------
                idx += 1
                img_name, ext = os.path.splitext(os.path.basename(img))
                Logged.logger.info('{:->4d} --> {:<s} --> x{:<d}--> {:<s}'.format(idx, model_name, sf, img_name+ext))

                img_L = utils_image.imread_uint(img, n_channels=3)
                img_L = utils_image.uint2tensor4(img_L)
                img_L = img_L.to(device)

                # --------------------------------
                # (2) inference
                # --------------------------------
                img_E = model(img_L)

                # --------------------------------
                # (3) img_E
                # --------------------------------
                img_E = utils_image.tensor2uint(img_E)
                if save_results:
                    utils_image.imsave(img_E, os.path.join(E_path, img_name+'_'+str(cnt)+'_'+model_name+'.png'))


#if __name__ == '__main__':

cnt = 110
main(cnt)


import os.path
import logging
import torch

from utils import utils_logger
from utils import utils_image as util
# from utils import utils_model
from models.network_rrdbnet import RRDBNet as net


"""
Spyder (Python 3.6-3.7)
PyTorch 1.4.0-1.8.1
Windows 10 or Linux
Kai Zhang (cskaizhang@gmail.com)
github: https://github.com/cszn/BSRGAN
        https://github.com/cszn/KAIR
If you have any question, please feel free to contact with me.
Kai Zhang (e-mail: cskaizhang@gmail.com)
by Kai Zhang ( March/2020 --> March/2021 --> )
This work was previously submitted to CVPR2021.

# --------------------------------------------
@inproceedings{zhang2021designing,
  title={Designing a Practical Degradation Model for Deep Blind Image Super-Resolution},
  author={Zhang, Kai and Liang, Jingyun and Van Gool, Luc and Timofte, Radu},
  booktitle={arxiv},
  year={2021}
}
# --------------------------------------------

"""


def main():

    utils_logger.logger_info('blind_sr_log', log_path='blind_sr_log.log')
    logger = logging.getLogger('blind_sr_log')

#    print(torch.__version__)               # pytorch version
#    print(torch.version.cuda)              # cuda version
#    print(torch.backends.cudnn.version())  # cudnn version

    testsets = 'testsets'       # fixed, set path of testsets
    testset_Ls = ['RealSRSet']  # ['RealSRSet','DPED']

    model_names = ['RRDB','ESRGAN','FSSR_DPED','FSSR_JPEG','RealSR_DPED','RealSR_JPEG']
    model_names = ['BSRGANx2']    # 'BSRGANx2' for scale factor 2
    model_names = ['RealSR_DPED']
    model_names = ['RRDB']
    model_names = ['BSRGANx2']
    model_names = ['RealSR_JPEG']
    model_names = ['BSRGANx2'] 
    save_results = True
    sf = 4
    #device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cpu')# if torch.cuda.is_available() else 'cpu')

    for model_name in model_names:
        if model_name in ['BSRGANx2']:
            sf = 2
        model_path = os.path.join('model_zoo', model_name+'.pth')          # set model path
        logger.info('{:>16s} : {:s}'.format('Model Name', model_name))

        # torch.cuda.set_device(0)      # set GPU ID
        #logger.info('{:>16s} : {:<d}'.format('GPU ID', torch.cuda.current_device()))
        #torch.cuda.empty_cache()

        # --------------------------------
        # define network and load model
        # --------------------------------
        model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=sf)  # define network

#            model_old = torch.load(model_path)
#            state_dict = model.state_dict()
#            for ((key, param),(key2, param2)) in zip(model_old.items(), state_dict.items()):
#                state_dict[key2] = param
#            model.load_state_dict(state_dict, strict=True)

        model.load_state_dict(torch.load(model_path), strict=True)
        model.eval()
        for k, v in model.named_parameters():
            v.requires_grad = False
        model = model.to(device)
        torch.cuda.empty_cache()

        for testset_L in testset_Ls:

            L_path = os.path.join(testsets, testset_L)
            #E_path = os.path.join(testsets, testset_L+'_'+model_name)
            E_path = os.path.join(testsets, testset_L+'_results_x'+str(sf))
            util.mkdir(E_path)

            logger.info('{:>16s} : {:s}'.format('Input Path', L_path))
            logger.info('{:>16s} : {:s}'.format('Output Path', E_path))
            idx = 0

            for img in util.get_image_paths(L_path):

                # --------------------------------
                # (1) img_L
                # --------------------------------
                idx += 1
                img_name, ext = os.path.splitext(os.path.basename(img))
                logger.info('{:->4d} --> {:<s} --> x{:<d}--> {:<s}'.format(idx, model_name, sf, img_name+ext))

                img_L = util.imread_uint(img, n_channels=3)
                img_L = util.uint2tensor4(img_L)
                img_L = img_L.to(device)

                # --------------------------------
                # (2) inference
                # --------------------------------
                img_E = model(img_L)

                # --------------------------------
                # (3) img_E
                # --------------------------------
                img_E = util.tensor2uint(img_E)
                if save_results:
                    util.imsave(img_E, os.path.join(E_path, img_name+'_'+model_name+'XX.png'))


if __name__ == '__main__':

    main()

sys.path.remove('/home/jack/hidden')
sys.path.append('/home/jack/Desktop/BSRGAN')
from utils import utils_logger

f=open("/home/jack/Desktop/BSRGAN/blind_sr_log.log").readlines()
for line in f:
    line = line.replace("\n","")
    print(line)



