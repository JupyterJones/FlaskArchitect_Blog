!cat logs/api.log

#import logging
# Create and configure logger
#logging.basicConfig(filename="newfile.log",
format='%(asctime)s %(message)s',
#filemode='a')
# Creating an object
#api_logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
#api_logger.setLevel(logging.DEBUG)
# Test messages
api_logger.debug('Harmless debug Message')
api_logger.info('Just an information')
api_logger.warning('Its a Warning')
api_logger.error('Did you try to divide by zero')
api_logger.critical('Internet is down')

quote_h  = "0200-000000-000000-c0f7769ec2-5500000200000-00000-0000-00b7f73ac6fc0100"
api_logger.info(quote_h)

import ctypes
example_string = "Hello world!"
address = id(example_string)
api_logger.info(address)
#string_from_address = ctypes.cast(address).value
#print(string_from_address)

import os
basedir = os.getcwd()
logger.info(basedir)

import codecs
quote_h  = "0200000000000000c0f7769ec2550000020000000000000000b7f73ac6fc0100"
api_logger.debug('Harmless debug Message')
api_logger.info('Just an information')
api_logger.warning('Its a Warning')
api_logger.error('Did you try to divide by zero')
api_logger.critical('Internet is down')
api_logger.info("new error",quote_h)
quote_a  = codecs.decode(quote_h, 'hex').decode("ASCII")

quote    = quote_a.replace(';', '\n- ')
print(quote)

!rm /home/jack/hidden/logger_settings.py

!cat logs/api.log

from ctypes import string_at
from sys import getsizeof

a = 0x7f31baf7b700 
print(string_at(id(a),getsizeof(a)).hex())


quote_h  = "4d7920736f667477617265206e657665722068617320627567732e204974206a75737420646576656c6f70732072616e646f6d2066656174757265732e3b416e6f6e796d6f7573"
quote_a  = codecs.decode(quote_h, 'hex').decode("ASCII")
quote    = quote_a.replace(';', '\n- ')
print(quote)

%%writefile /home/jack/hidden/logger_settings.py
import sys
import os
import logging
from logging.config import dictConfig
import os


basedir = os.getcwd()
directory = "logs"
if not os.path.exists(directory):
    os.mkdir(os.path.join(basedir, directory))



logging_config = dict(
    version=1,
    formatters={
        'verbose': {
            'format': ("[%(asctime)s] %(levelname)s "
                       "[%(name)s:%(lineno)s] %(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    handlers={
        'api-logger': {'class': 'logging.handlers.RotatingFileHandler',
                           'formatter': 'verbose',
                           'level': logging.DEBUG,
                           'filename': basedir+'/logs/api.log',
                           'maxBytes': 52428800,
                           'backupCount': 7},
        'batch-process-logger': {'class': 'logging.handlers.RotatingFileHandler',
                             'formatter': 'verbose',
                             'filename': basedir+'/logs/batch.log',
                             'maxBytes': 52428800,
                             'backupCount': 7},
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
    },
    loggers={
        'api_logger': {
            'handlers': ['api-logger', 'console'],
            'level': logging.DEBUG
        },
        'batch_process_logger': {
            'handlers': ['batch-process-logger', 'console'],
            'level': logging.DEBUG
        }
    }
)

dictConfig(logging_config)

api_logger = logging.getLogger('api_logger')
batch_process_logger = logging.getLogger('batch_process_logger')


import ctypes
example_string = "Hello world!"
address = id(example_string)
#value = ctypes.c_int.from_address(address)
#value = ctypes.cast(address, id )
#print (value)
print(address)

from logger_settings import api_logger
api_logger.info('more')
api_logger.debug('Harmless debug Message')
api_logger.info('Just an information')
api_logger.warning('Its a Warning')
api_logger.error('Did you try to divide by zero')
api_logger.critical('Internet is down')

!cat logs/api.log

    Logger.info(msg) : This will log a message with level INFO on this logger.
    Logger.warning(msg) : This will log a message with a level WARNING on this logger.
    Logger.error(msg) : This will log a message with level ERROR on this logger.
    Logger.critical(msg) : This will log a message with level CRITICAL on this logger.
    Logger.log(lvl,msg) : This will Logs a message with integer level lvl on this logger.
    Logger.exception(msg) : This will log a message with level ERROR on this logger.
    Logger.setLevel(lvl) : This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
    Logger.addFilter(filt) : This adds a specific filter filt into this logger.
    Logger.removeFilter(filt) : This removes a specific filter filt into this logger.
    Logger.filter(record) : This method applies the logger’s filter to the record provided and returns True if the record is to be processed. Else, it will return False.
    Logger.addHandler(hdlr) : This adds a specific handler hdlr to this logger.
    Logger.removeHandler(hdlr) : This removes a specific handler hdlr into this logger.
    Logger.hasHandlers() : This checks if the logger has any handler configured or not. 

   #utils_logger.logger_info('blind_sr_log', log_path='blind_sr_log.log')
    Logged.info('blind_sr_log', log_path='blind_sr_log.log')
    #python_utils.logger('blind_sr_log', log_path='blind_sr_log.log')
    #logger = logging.getLogger('blind_sr_log')

import sys
sys.path.append("/media/jack/HDD500/")
from model_zoo.ModelList import MODEL
model_name = MODEL()[3]



api_logger.info('{:>16s} : {:s}'.format('Model Name', model_name))

model_names = ['RRDB','ESRGAN','FSSR_DPED','FSSR_JPEG','RealSR_DPED','RealSR_JPEG']
#model_names = ['BSRGAN','BSRGANx2']    # 'BSRGANx2' for scale factor 2
for model_name in model_names:
    if model_name in ['BSRGANx2']:
        sf = 2
    model_path = os.path.join('/media/jack/HDD500/model_zoo', model_name+'.pth')          # set model path
    api_logger.info('{:>16s} : {:s}'.format('Model Name', model_name))
    print (model_path)

import sys
sys.path.append('/home/jack/Desktop/BSRGAN')
sys.path
#['', ..., '/home/sergey']
sys.path.remove('/home/jack/hidden')
#sys.path

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
api_logger.info(FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
api_logger.debug('tcpserver')
api_logger.warning('Protocol problem: %s', 'connection reset', extra=d)

# simple logging example
#import logging

#level = logging.DEBUG
#logging_format = "[%(levelname)s] %(asctime)s - %(message)s"
#logging.basicConfig(level = level, format=logging_format)

def print_vs_logging():
    api_logger.debug("What is the value of this variable")
    api_logger.info("Just FYI")
    api_logger.error("We found the error")

print_vs_logging()

api_logger.info("-------------------------------\n")

!cat logs/api.log

import os.path
import logging
import torch
from python_utils.logger import Logged
import python_utils.logger
import python_utils
from utils import utils_logger
from utils import utils_image as util
from utils import utils_model
from models.network_rrdbnet import RRDBNet as net
import sys
sys.path.append("/media/jack/HDD500/")
from model_zoo.ModelList import MODEL
data = MODEL()[3]
print(data)
MODELlist = []
model_names = ['RRDB','ESRGAN','FSSR_DPED','FSSR_JPEG','RealSR_DPED','RealSR_JPEG','BSRGANx2']
cnt = -1
for model_ in MODEL():
    cnt = cnt +1
    for model_name in model_names:
        if model_name in model_:
            print(model_name,"MODEL("+str(cnt)+")", MODEL()[cnt])
            MODELlist.append(MODEL()[cnt])

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

    #utils_logger.logger_info('blind_sr_log', log_path='blind_sr_log.log')
    #Logged.info('blind_sr_log', log_path='blind_sr_log.log')
    #python_utils.logger('blind_sr_log', log_path='blind_sr_log.log')
    #logger = logging.getLogger('blind_sr_log')

#    print(torch.__version__)               # pytorch version
#    print(torch.version.cuda)              # cuda version
#    print(torch.backends.cudnn.version())  # cudnn version

    testsets = 'testsets'       # fixed, set path of testsets
    testset_Ls = ['RealSRSet']  # ['RealSRSet','DPED']

    #model_names = ['RRDB','ESRGAN','FSSR_DPED','FSSR_JPEG','RealSR_DPED','RealSR_JPEG','BSRGANx2']
    #model_names = ['BSRGANx2']    # 'BSRGANx2' for scale factor 2



    save_results = True
    sf = 4
    device = torch.device('cpu')# if torch.cuda.is_available() else 'cpu')

    for model_path in MODELlist:
        if model_path == MODEL()[3]:
            sf = 2
        else:
            sf=4
            print(model_path)
        #model_path = os.path.join('model_zoo', model_name+'.pth')          # set model path
        api_logger.info('{:>16s} : {:s}'.format('Model Name', model_name))

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
        print(model_path)
        suf =model_path[29:][:6]
        print ("SUF: ",suf)
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
 
            api_logger.info('{:>16s} : {:s}'.format('Input Path', L_path))
            api_logger.info('{:>16s} : {:s}'.format('Output Path', E_path))
            idx = 0

            for img in utils_image.get_image_paths(L_path):

                # --------------------------------
                # (1) img_L
                # --------------------------------
                idx += 1
                img_name, ext = os.path.splitext(os.path.basename(img))
                api_logger.info('{:->4d} --> {:<s} --> x{:<d}--> {:<s}'.format(idx, model_name, sf, img_name+ext))

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
                imagenumber = 0
                if save_results:
                    imagenumber =imagenumber +1
                    number = str(imagenumber)
                    utils_image.imsave(img_E, os.path.join(E_path, img_name+suf+'_'+number+'_.png'))
                    print(os.path.join(E_path, img_name+suf+'_'+number+'_.png'))


if __name__ == '__main__':

    main()


!cat newfile.log

import logging
from python_utils.logger import Logged
import python_utils.logger

!pwd

!ls logs

!cat logs/api.log

!cat logs/batch.log

from python_utils import logger
import logging
import functools

Logged.info('blind_sr_log', log_path='blind_sr_log.log')

Logged.info('blind_sr_log', log_path='blind_sr_log.log')

!cat blind_sr_log.log



