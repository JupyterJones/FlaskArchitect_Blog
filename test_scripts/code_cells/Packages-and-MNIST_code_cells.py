import sys
sys.path.append('/home/jack/Desktop/Imagedata')
from ImageDirectories import imagelist

for num in range(0,17):
    print(str(num)+": ",imagelist(num))

import VID2img

import sys
print(sys.path)
#dir(sys)

from random import randint
Hash = ["#CreativeCoding #fxhash #p5js #Generative\n","#twitme #Python #100DaysOfCode\n","#Python #PythonBots #codefor30days\n" ]
hashnum = randint(0,len(Hash)-1)
hashs =Hash[hashnum]
hashs         

!ls /home/jack/.local/lib/python3.9/site-packages

/home/jack/hidden

!ls /home/jack/miniconda3/envs/cloned_base/lib/python3.9/site-packages/ImageGenerator

!mv ~/miniconda3/envs/cloned_base/lib/python3.9/site-packages/ImageGenerator .

from ImageGenerator import *
import ImageGenerator.mkimage
dir (mkimage.mkimage())

from ImageGenerator import *
#dir (ImageGenerator.__file__)
dir (ImageGenerator)

Create a package

from setuptools import setup, find_packages
find_packages()

from ImageGenerator import *
dir()

from PIL import Image
def cropfromcenter(PATH,new_width,height):
    im = Image.open(PATH)
    width, height = im.size   # Get dimensions

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    return im


from PIL import Image
def cropfromcenter(PATH,new_width,height,moveright=0,movedown=0):
    im = Image.open(PATH)
    width, height = im.size   # Get dimensions

    left = ((width - new_width)/2)+moveright
    top = ((height - new_height)/2)+movedown
    right = ((width + new_width)/2)+moveright
    bottom = ((height + new_height)/2)+movedown
    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    return im


PATH = "processed_images/02594.jpg"
new_width = 200
new_height = 200
nim = cropfromcenter(PATH,new_width,new_height,moveright=160,movedown=-10,)
print(nim.size)
nim



PATH = "processed_images/02594.jpg"
new_width = 350
new_height = 200
nim = cropfromcenter(PATH,new_width,new_height,offsetw=-150,offseth=50,)
nim

PATH = "processed_images/02594.jpg"
new_width = 200
new_height = 200
nim = cropfromcenter(PATH,new_width,new_height)
nim

# I want to crop 640x640 from the center
from PIL import Image
Bp=Image.open("processed_images/02594.jpg")
width, height = Bp.size
wc = int(width/4)
hc = int(height/4)

print (width, height, wc, hc)
# I want to crop 640x640 from the center


!pip freeze >>FREEZE

# %load FREEZE
absl-py==1.2.0
anyio @ file:///tmp/build/80754af9/anyio_1644463572971/work/dist
argon2-cffi @ file:///opt/conda/conda-bld/argon2-cffi_1645000214183/work
argon2-cffi-bindings @ file:///tmp/build/80754af9/argon2-cffi-bindings_1644569679365/work
arrow==1.2.3
asttokens @ file:///opt/conda/conda-bld/asttokens_1646925590279/work
astunparse==1.6.3
async-generator==1.10
attrs @ file:///opt/conda/conda-bld/attrs_1642510447205/work
Babel @ file:///tmp/build/80754af9/babel_1620871417480/work
backcall @ file:///home/ktietz/src/ci/backcall_1611930011877/work
beautifulsoup4 @ file:///opt/conda/conda-bld/beautifulsoup4_1650462163268/work
binaryornot==0.4.4
bleach @ file:///opt/conda/conda-bld/bleach_1641577558959/work
blinker==1.4
brotlipy==0.7.0
cachetools==5.2.0
certifi==2022.9.24
cffi @ file:///opt/conda/conda-bld/cffi_1642701102775/work
chardet==5.0.0
charset-normalizer==2.1.1
chart-studio==1.1.0
click==8.1.3
cloudpickle @ file:///tmp/build/80754af9/cloudpickle_1632508026186/work
colorama @ file:///tmp/build/80754af9/colorama_1607707115595/work
colorific==0.3
colormath==3.0.0
colour==0.1.5
colour-science @ git+https://github.com/crowsonkb/colour@bf653ac17ca57fea0695df114cf785df7161beec
conda-content-trust @ file:///tmp/build/80754af9/conda-content-trust_1617045594566/work
conda-package-handling @ file:///tmp/build/80754af9/conda-package-handling_1649105784853/work
cookiecutter==2.1.1
cookiejar==0.0.3
cryptography @ file:///tmp/build/80754af9/cryptography_1639414572950/work
cycler @ file:///tmp/build/80754af9/cycler_1637851556182/work
cytoolz==0.11.0
dask @ file:///tmp/abs_994957d9-ec12-411f-b953-c010f9d489d10hj3gz4k/croots/recipe/dask-core_1658513209934/work
debugpy @ file:///tmp/build/80754af9/debugpy_1637091799509/work
decorator==4.4.2
defusedxml @ file:///tmp/build/80754af9/defusedxml_1615228127516/work
dill==0.3.5.1
entrypoints @ file:///tmp/build/80754af9/entrypoints_1649926439650/work
etils==0.8.0
executing @ file:///opt/conda/conda-bld/executing_1646925071911/work
fastjsonschema @ file:///opt/conda/conda-bld/python-fastjsonschema_1661371079312/work
filelock==3.8.0
flatbuffers==22.9.24
fonttools==4.25.0
fsspec @ file:///opt/conda/conda-bld/fsspec_1659972197723/work
future==0.18.2
gast==0.4.0
generativepy==3.2
google-auth==2.12.0
google-auth-oauthlib==0.4.6
google-images-download==2.8.0
google-pasta==0.2.0
googleapis-common-protos==1.56.4
grpcio==1.49.1
h11==0.13.0
h5py==3.7.0
huepy==1.2.1
huggingface-hub==0.10.0
idna==3.4
imageio @ file:///tmp/abs_cd920173-f360-47c5-97b0-bf4d1076d5d4dvic0oys/croots/recipe/imageio_1658785036907/work
imageio-ffmpeg==0.4.7
importlib-metadata==5.0.0
importlib-resources==5.9.0
imread==0.7.4
iniconfig==1.1.1
instabot==0.117.0
ipykernel @ file:///tmp/build/80754af9/ipykernel_1647000773790/work/dist/ipykernel-6.9.1-py3-none-any.whl
ipyplot==1.1.1
ipython @ file:///opt/conda/conda-bld/ipython_1657652213665/work
ipython-genutils @ file:///tmp/build/80754af9/ipython_genutils_1606773439826/work
ipywidgets @ file:///tmp/build/80754af9/ipywidgets_1634143127070/work
jedi @ file:///tmp/build/80754af9/jedi_1644297102865/work
Jinja2 @ file:///opt/conda/conda-bld/jinja2_1647436528585/work
jinja2-time==0.2.0
joblib==1.2.0
json5 @ file:///tmp/build/80754af9/json5_1624432770122/work
jsonschema @ file:///tmp/build/80754af9/jsonschema_1650025953207/work
jupyter @ file:///tmp/abs_33h4eoipez/croots/recipe/jupyter_1659349046347/work
jupyter-client @ file:///opt/conda/conda-bld/jupyter_client_1643638337975/work
jupyter-console @ file:///opt/conda/conda-bld/jupyter_console_1647002188872/work
jupyter-core @ file:///opt/conda/conda-bld/jupyter_core_1651671229925/work
jupyter-server @ file:///tmp/abs_b88b31b8-83b9-476d-a46d-e563c421f38fvsnyi1ur/croots/recipe/jupyter_server_1658754481507/work
jupyterlab @ file:///tmp/abs_12f3h01vmy/croots/recipe/jupyterlab_1658907535764/work
jupyterlab-pygments @ file:///tmp/build/80754af9/jupyterlab_pygments_1601490720602/work
jupyterlab-server @ file:///opt/conda/conda-bld/jupyterlab_server_1650462180599/work
jupyterlab-widgets @ file:///tmp/build/80754af9/jupyterlab_widgets_1609884341231/work
keras==2.10.0
Keras-Preprocessing==1.1.2
kiwisolver @ file:///opt/conda/conda-bld/kiwisolver_1653292039266/work
libclang==14.0.6
locket @ file:///opt/conda/conda-bld/locket_1652903118915/work
mahotas==1.4.13
Markdown==3.4.1
markovify==0.9.4
MarkupSafe==2.1.1
matplotlib @ file:///tmp/build/80754af9/matplotlib-suite_1634667019719/work
matplotlib-inline @ file:///opt/conda/conda-bld/matplotlib-inline_1662014470464/work
mistune @ file:///tmp/build/80754af9/mistune_1607364877025/work
mock==4.0.3
moviepy==1.0.3
munkres==1.1.4
nbclassic @ file:///opt/conda/conda-bld/nbclassic_1644943264176/work
nbclient @ file:///tmp/build/80754af9/nbclient_1650290509967/work
nbconvert @ file:///opt/conda/conda-bld/nbconvert_1649751911790/work
nbformat @ file:///tmp/build/80754af9/nbformat_1649826788557/work
nest-asyncio @ file:///tmp/build/80754af9/nest-asyncio_1649847906199/work
networkx @ file:///opt/conda/conda-bld/networkx_1657784097507/work
notebook @ file:///tmp/abs_abf6xa6h6f/croots/recipe/notebook_1659083654985/work
numpy==1.22.4
oauthlib==3.2.1
opt-einsum==3.3.0
outcome==1.2.0
packaging==21.3
pager==3.3
pandas==1.2.4
pandocfilters @ file:///opt/conda/conda-bld/pandocfilters_1643405455980/work
parso @ file:///opt/conda/conda-bld/parso_1641458642106/work
partd @ file:///opt/conda/conda-bld/partd_1647245470509/work
pexpect @ file:///tmp/build/80754af9/pexpect_1605563209008/work
pickleshare @ file:///tmp/build/80754af9/pickleshare_1606932040724/work
Pillow==9.0.1
plotly==5.10.0
pluggy==1.0.0
proglog==0.1.10
prometheus-client @ file:///tmp/abs_d3zeliano1/croots/recipe/prometheus_client_1659455100375/work
promise==2.3
prompt-toolkit @ file:///tmp/build/80754af9/prompt-toolkit_1633440160888/work
protobuf==3.19.6
ptyprocess @ file:///tmp/build/80754af9/ptyprocess_1609355006118/work/dist/ptyprocess-0.7.0-py2.py3-none-any.whl
pure-eval @ file:///opt/conda/conda-bld/pure_eval_1646925070566/work
py==1.11.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycairo==1.21.0
pycosat==0.6.3
pycparser @ file:///tmp/build/80754af9/pycparser_1636541352034/work
Pygments @ file:///opt/conda/conda-bld/pygments_1644249106324/work
PyJWT @ file:///opt/conda/conda-bld/pyjwt_1657544592787/work
pyOpenSSL @ file:///opt/conda/conda-bld/pyopenssl_1643788558760/work
pyparsing==3.0.9
pyrsistent @ file:///tmp/build/80754af9/pyrsistent_1636110951836/work
PySocks @ file:///tmp/build/80754af9/pysocks_1605305812635/work
pytest==7.1.3
python-dateutil @ file:///tmp/build/80754af9/python-dateutil_1626374649649/work
python-dotenv==0.21.0
python-slugify==6.1.2
pytz @ file:///opt/conda/conda-bld/pytz_1654762638606/work
PyWavelets @ file:///tmp/build/80754af9/pywavelets_1607645421828/work
PyYAML==5.3.1
pyzmq @ file:///tmp/build/80754af9/pyzmq_1638434985866/work
qtconsole @ file:///opt/conda/conda-bld/qtconsole_1662018252641/work
QtPy @ file:///opt/conda/conda-bld/qtpy_1662014892439/work
regex==2022.9.13
requests==2.28.1
requests-oauthlib==1.3.1
requests-toolbelt==0.9.1
responses==0.21.0
retrying==1.3.3
rsa==4.9
ruamel-yaml-conda @ file:///tmp/build/80754af9/ruamel_yaml_1616016711199/work
schedule==1.1.0
scikit-image==0.16.2
scikit-learn==1.1.2
scipy @ file:///tmp/build/80754af9/scipy_1641555002955/work
seaborn @ file:///tmp/build/80754af9/seaborn_1629307859561/work
selenium==4.4.3
Send2Trash @ file:///tmp/build/80754af9/send2trash_1632406701022/work
shortuuid==1.0.9
sip==4.19.13
six==1.16.0
sklearn==0.0
sniffio @ file:///tmp/build/80754af9/sniffio_1614030464178/work
sortedcontainers==2.4.0
soupsieve @ file:///tmp/build/80754af9/soupsieve_1636706018808/work
stack-data @ file:///opt/conda/conda-bld/stack_data_1646927590127/work
tenacity==8.1.0
tensorboard==2.10.1
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow @ file:///home/jack/base_tensorflow_pkg/tensorflow-2.11.0-cp39-cp39-linux_x86_64.whl
tensorflow-estimator==2.10.0
tensorflow-hub==0.12.0
tensorflow-io-gcs-filesystem==0.27.0
tensorflow-metadata==1.10.0
termcolor==2.0.1
terminado @ file:///tmp/build/80754af9/terminado_1644322582718/work
testpath @ file:///opt/conda/conda-bld/testpath_1655908557405/work
text-unidecode==1.3
threadpoolctl==3.1.0
tokenizers==0.12.1
toml==0.10.2
tomli==2.0.1
toolz @ file:///tmp/build/80754af9/toolz_1636545406491/work
torch==1.12.1
tornado @ file:///tmp/build/80754af9/tornado_1606942317143/work
tqdm @ file:///opt/conda/conda-bld/tqdm_1647339053476/work
traitlets @ file:///tmp/build/80754af9/traitlets_1636710298902/work
transformers==4.22.2
trio==0.21.0
trio-websocket==0.9.2
twython @ file:///tmp/build/80754af9/twython_1614080287802/work
typing_extensions==4.3.0
Unidecode==1.3.4
urllib3==1.26.12
wcwidth @ file:///Users/ktietz/demo/mc3/conda-bld/wcwidth_1629357192024/work
webdriver-manager==3.8.3
webencodings==0.5.1
websocket-client @ file:///tmp/build/80754af9/websocket-client_1614803975924/work
Werkzeug==2.2.2
widgetsnbextension @ file:///tmp/build/80754af9/widgetsnbextension_1644992802045/work
wrapt==1.14.1
wsproto==1.2.0
zipp==3.8.1


 FILE FORMATS FOR THE MNIST DATABASE
The data is stored in a very simple file format designed for storing vectors and multidimensional matrices. General info on this format is given at the end of this page, but you don't need to read that to use the data files.

All the integers in the files are stored in the MSB first (high endian) format used by most non-Intel processors. Users of Intel processors and other low-endian machines must flip the bytes of the header.

There are 4 files:

train-images-idx3-ubyte: training set images
train-labels-idx1-ubyte: training set labels
t10k-images-idx3-ubyte:  test set images
t10k-labels-idx1-ubyte:  test set labels

The training set contains 60000 examples, and the test set 10000 examples.

The first 5000 examples of the test set are taken from the original NIST training set. The last 5000 are taken from the original NIST test set. The first 5000 are cleaner and easier than the last 5000.
TRAINING SET LABEL FILE (train-labels-idx1-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  60000            number of items
0008     unsigned byte   ??               label
0009     unsigned byte   ??               label
........
xxxx     unsigned byte   ??               label

The labels values are 0 to 9.
TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  60000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     unsigned byte   ??               pixel
0017     unsigned byte   ??               pixel
........
xxxx     unsigned byte   ??               pixel

Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
TEST SET LABEL FILE (t10k-labels-idx1-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  10000            number of items
0008     unsigned byte   ??               label
0009     unsigned byte   ??               label
........
xxxx     unsigned byte   ??               label

The labels values are 0 to 9.
TEST SET IMAGE FILE (t10k-images-idx3-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  10000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     unsigned byte   ??               pixel
0017     unsigned byte   ??               pixel
........
xxxx     unsigned byte   ??               pixel

Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
 
THE IDX FILE FORMAT
the IDX file format is a simple format for vectors and multidimensional matrices of various numerical types.

The basic format is

magic number
size in dimension 0
size in dimension 1
size in dimension 2
.....
size in dimension N
data

The magic number is an integer (MSB first). The first 2 bytes are always 0.

The third byte codes the type of the data:
0x08: unsigned byte
0x09: signed byte
0x0B: short (2 bytes)
0x0C: int (4 bytes)
0x0D: float (4 bytes)
0x0E: double (8 bytes)

The 4-th byte codes the number of dimensions of the vector/matrix: 1 for vectors, 2 for matrices....

The sizes in each dimension are 4-byte integers (MSB first, high endian, like in most non-Intel processors).

The data is stored like in a C array, i.e. the index in the last dimension changes the fastest.
  

