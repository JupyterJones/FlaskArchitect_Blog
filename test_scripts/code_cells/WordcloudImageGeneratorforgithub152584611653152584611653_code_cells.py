!pip freeze >>freez.txt
# I used my installed modules as the word cloud I executed 'pip' freeze
# then copied the resulting words, minus the version to 'wordcloud.txt'

f = open("freez.txt").readlines()
for line in f:
    line = line.replace("\n", "")
    print line

%%writefile wordcloud.txt
aiml
alabaster
altair
anaconda_client
anaconda_project
appdirs
apptools
argcomplete
arrow
astroid
astropy
attrs
Automat
Babel
backports_abc
backports.functools-lru-cache
backports.shutil-get-terminal-size
backports.ssl-match-hostname
BeautifulSoup
beautifulsoup4
bitarray
blaze
bleach
bokeh
boto
Bottleneck
branca
bs4
cdecimal
certifi
cffi
chardet
ChatterBot
chatterbot-corpus
chest
click
get-mak-eurl
cloudpickle
clyent
colorama
coloredlogs
conda
configobj
configparser
constantly
contextlib2
cov-core
coverage
cryptography
cssselect
cycler
Cython
cytoolz
dask
data
datashape
decorator
dill
dlib
docopt
docutils
dot2tex
e
entrypoints
enum34
et-xmlfile
facemorpher
fastcache
Flask
Flask-Admin
Flask-Cors
Flask-GraphQL
Flask-WTF
flickr-api
flickrapi
folium
funcsigs
functions
functools32
future
futures
gevent
gitter
graphene
graphene
sqlalchemy
graphql-core
graphql-relay
graphviz
greenlet
grin
h5py
HeapDict
html2text
html5lib
httplib2
humanfriendly
hyperlink
icrawler
idna
ijson
imageio
imagesize
imutils
incremental
inflect
ipaddress
ipykernel
ipyleaflet
ipython
ipython-genutils
ipyvolume
ipywidgets
irc
iso8601
isort
itsdangerous
jaraco.classes
jaraco.collections
jaraco.functools
jaraco.itertools
jaraco.logging
jaraco.stream
jaraco.text
jdcal
jedi
Jinja2
JSON-log-formatter
json-tricks
jsondatabase
jsonschema
jupyter-client
jupyter-console
jupyter-contrib-core
jupyter-contrib-nbextensions
jupyter-core
jupyter-highlight-selected-word==0.0.11jupyter-latex-envs
jupyter-nbextensions-configurator
jupyterlab
jupyterlab-launcher
labellio-cli
latex
lazy-object-proxy
leveldb
lightning-python
llvmlite
locket
lxml
mahotas
Markdown
markovbot
markovify
MarkupSafe
matplotlib
metakernel
meteor-ejson
mistune
mock
mongoengine
monotonic
more-itertools
mpld3
mpmath
msnoise
msnoise-tomo
multipledispatch
MySQL-python
nbconvert
nbformat
networkx
nltk
nodebox-opengl
nose
nose-cov
notebook
numba
numexpr
numpy
numpydoc
oauth
oauthlib
obspy
odo
olefile
openpyxl
packaging
pandas
pandocfilters
parsel
partd
pathlib2
patsy
pbr
pep8
pexpect
pickleshare
Pillow
pkginfo
plotly
ply
processing
progressbar
promise
prompt-toolkit
protobuf
psutil
PsychoPy
psycopg2
ptyprocess
py
py3-protobuffers
PyAIML
pyamg
pyasn1
pyasn1-modules
pycairo
pychecker
pycosat
pycparser
pycrypto
pycurl
PyDispatcher
pydot
pyee
pyface
pyflakes
pygame
pyglet
Pygments
PyInstaller
pylint
pymongo
pymorph
pymunk
PyMySQL
PyOpenGL
PyOpenGL-accelerate
pyOpenSSL
pyparsing
pytest
python-coveralls
python-dateutil
python-ddp
python-meteor
python-resize-image
python-twitter
pythreejs
pyttsx
pytz
PyWavelets
PyYAML
pyzmq
QtAwesome
QtPy
queuelib
redis
requests
requests-oauthlib
requests-toolbelt
requirements
rope
scandir
scikit-image
scikit-learn
scipy
Scrapy
seaborn
selectivesearch
service-identity
Shapely
shutilwhich
simplegeneric
singledispatch
six
skulpt-python
snowballstemmer
sockjs-tornado
Sphinx
sphinx-rtd-theme
SQLAlchemy
statsmodels
subprocess32
surrealism
SVGFig
svgwrite
sympy
tables
tempdir
tempora
tensorflow
termenu
terminado
testpath
textblob
times
toolz
tornado
tqdm
traitlets
traits
traitsui
traittypes
tweepy
twine
Twisted
TwitterAPI
typing
unicodecsv
Unidecode
vega
virtualenv
vpnotebook
vpython
vtk
w3lib
Wand
wcwidth
webcolors
webencodings
Werkzeug
widgetsnbextension
wrapt
ws4py
WTForms
wxPython
xerox
xlrd
XlsxWriter
xlwt
zope.interface

#%%writefile twitterpost.py

#%%writefile twitterpost.py
#!/anaconda2/bin/python
import os
import random
import sys
import markovify
sys.path.insert(0, '/home/jack/Desktop/pycode/vpython2')
import twython
from twython import Twython
import time
#removed keys for privacy reasons
CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXX'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
#STR = (text_model.make_short_sentence(140))
STR = ("Nice and simple graph. Making graphic images is easy and fun. These circular graphs have a nice appearance to me")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "images/NewFolder/lightning01T.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


# Testing script to print one random word from wordcloud.txt

import random

def generate_the_word(infile):
    with open(infile) as f:
        contents_of_file = f.read()
    lines = contents_of_file.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]
wrd = (generate_the_word("wordcloud.txt"))
print wrd


# Testing a random loop

import random
count = 0
while count< 10:
    def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
    TEXT = "freez.txt"
    #TEXT = "wordcloud.txt"
    wrd = (generate_the_word(TEXT))
    count = count+1
    print wrd

from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
base = Image.open('images/NewFolder/textback.jpg').convert('RGBA')
w, h = base.size
Lw = randint(0,w-50)
Lh = randint(0,h-30)
print Lw, Lh

# generating just a Wordcloud background

from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
# get an image
count = 1
# use an existing image
#start = Image.open('images/NewFolder/textback.jpg').convert('RGBA')
#or create a blank on
start = Image.new('RGBA', (640,640), (255,0,255,0))
start.save('images/StartBlank.png')


from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
# get an image
count = 1
start2 = Image.open('images/NewFolder/textback.jpg').convert('RGBA')
start2.save('images/NewFolder/textbackU.jpg')
while count < 256 :
    base = Image.open('images/NewFolder/textbackU.jpg').convert('RGBA')
 
    #8 5 4 6 3 2
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    # get a font
    #generate a random size for the font
    int_n = int(count*.2)
    Fsize = randint(15,100-int_n)
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", Fsize)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    width, height = base.size


    def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
    textin = (generate_the_word("wordcloud.txt"))

    # calculate the x,y coordinates of the text
    w, h = base.size
    Lw = randint(-150,w-50)
    Lh = randint(-50,h-30)
    #textin = "The TwitterBot Project" 
    #generate random color and opacity
    r = randint(0,256)
    g = randint(0,256)
    b = randint(0,256)
    a = randint(0,count)
    d.text((Lw,Lh), textin, font=fnt, fill=(r,g,b,a))

    out = Image.alpha_composite(base, txt)
    out.save("images/NewFolder/textbackU3.jpg", "JPEG")
    count=count+1
       
    
out.show()


from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
# get an image
count = 1
start = Image.open('images/StartBlank.png').convert('RGBA')
start.save('images/StartBlank.png')
while count < 256 :
    base = Image.open('images/StartBlank.png').convert('RGBA')
 
    #8 5 4 6 3 2
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    # get a font
    #generate a random size for the font
    int_n = int(count*.2)
    Fsize = randint(15,100-int_n)
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", Fsize)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    width, height = base.size


    def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
    textin = (generate_the_word("wordcloud.txt"))

    # calculate the x,y coordinates of the text
    w, h = base.size
    Lw = randint(-150,w-50)
    Lh = randint(-50,h-30)
    #textin = "The TwitterBot Project" 
    #generate random color and opacity
    r = randint(0,256)
    g = randint(0,256)
    b = randint(0,256)
    a = randint(0,count)
    d.text((Lw,Lh), textin, font=fnt, fill=(r,g,b,a))

    out = Image.alpha_composite(base, txt)
    out.save("images/textbacktmp.png", "PNG")
    count=count+1
       
#base = Image.open('images/NewFolder/lightning01.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', out.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = out.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy
textin = "The TwitterBot Project" 
d.text((x,y), textin, font=fnt, fill=(0,0,0,256))

out = Image.alpha_composite(out, txt)
out.save("images/textbackP001.png", "PNG")
out.show()


!showme images/textbackP001.png

from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('images/textbackP001.png').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
x = 90
y = 10
textin = "PYTHON MODULES" 
d.text((x,y), textin, font=fnt, fill=(0,0,0,250))

out2 = Image.alpha_composite(base, txt)
out2.save("images/textbackP_post002.png", "PNG")
out2.show()


from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('images/NewFolder/textbackP_post002.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy
textin = "The TwitterBot Project" 
d.text((x,y), textin, font=fnt, fill=(0,0,0,180))

out = Image.alpha_composite(base, txt)
out.save("images/NewFolder/textbackP_post002_signed.jpg", "JPEG")
out.show()


#%%writefile twitterpost.py
#!/anaconda2/bin/python
import os
import random
import sys
import markovify
sys.path.insert(0, '/home/jack/Desktop/pycode/vpython2')
import twython
from twython import Twython
import random
import time
#removed keys for privacy reasons
CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXX'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
#STR = (text_model.make_short_sentence(140))
STR = ("#wordcloud from pip freeze - a few of my modules. not enough roomfor all #pip #freeze #python #modules #pythonmodules #pythongraphics")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "images/NewFolder/textbackP_post002_signed.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])


from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
# get an image
-

from PIL import Image, ImageDraw, ImageFont
import random
from random import randint
# get an image


#title = "Python Stuff"
signature_ = "The TwitterBot Project" 

count = 1
start = Image.open('images/NewFolder/newback.jpg').convert('RGBA')
start.save('images/NewFolder/textbacktmp.jpg')
while count < 256 :
    base = Image.open('images/NewFolder/textbacktmp.jpg').convert('RGBA')
 
    #8 5 4 6 3 2
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    # get a font
    #generate a random size for the font
    int_n = int(count*.2)
    Fsize = randint(15,100-int_n)
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", Fsize)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    width, height = base.size


    def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
    textin = (generate_the_word("wordcloud.txt"))

    # calculate the x,y coordinates of the text
    w, h = base.size
    Lw = randint(-150,w-50)
    Lh = randint(-50,h-30)
    #textin = "The TwitterBot Project" 
    #generate random color and opacity
    r = randint(0,256)
    g = randint(0,256)
    b = randint(0,256)
    a = randint(0,count)
    d.text((Lw,Lh), textin, font=fnt, fill=(r,g,b,a))

    out = Image.alpha_composite(base, txt)
    out.save("images/NewFolder/textbacktmp.jpg", "JPEG")
    count=count+1
       
#base = Image.open('images/NewFolder/lightning01.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', out.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = out.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy

d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

out = Image.alpha_composite(out, txt)
out.save("images/NewFolder/tmp.jpg", "JPEG")
# save the image then reopen to put a title
base = Image.open('images/NewFolder/tmp.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
x = 90
y = 10
#generate a title
title = (generate_the_word("titles.txt"))

d.text((x,y), title , font=fnt, fill=(0,0,0,250))

out2 = Image.alpha_composite(base, txt)
out2.save("images/NewFolder/textbackP_post003.jpg", "JPEG")
out2.show()


%%writefile titles.txt
Python Fun
Python Graphics
Generator
Word Cloud
Graphics
Fun w/Python
Python Stuff
PYTHON !!!
Love`en Python
Creative Python
Graphic Fun



#%%writefile TwittePost.py
#!/anaconda2/bin/python
import os
import random
import sys
import markovify
import twython
from twython import Twython
import time
from PIL import Image, ImageDraw, ImageFont
from random import randint
# get an image

#title = "Python Stuff"
signature_ = "The TwitterBot Project" 

count = 1
start = Image.open('images/NewFolder/newback.jpg').convert('RGBA')
start.save('images/NewFolder/textbacktmp.jpg')
while count < 256 :
    base = Image.open('images/NewFolder/textbacktmp.jpg').convert('RGBA')
 
    #8 5 4 6 3 2
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    # get a font
    #generate a random size for the font
    int_n = int(count*.2)
    Fsize = randint(15,100-int_n)
    fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", Fsize)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    width, height = base.size


    def generate_the_word(infile):
        with open(infile) as f:
            contents_of_file = f.read()
        lines = contents_of_file.splitlines()
        line_number = random.randrange(0, len(lines))
        return lines[line_number]
    textin = (generate_the_word("wordcloud.txt"))

    # calculate the x,y coordinates of the text
    w, h = base.size
    Lw = randint(-150,w-50)
    Lh = randint(-50,h-30)
    #textin = "The TwitterBot Project" 
    #generate random color and opacity
    r = randint(0,256)
    g = randint(0,256)
    b = randint(0,256)
    a = randint(0,count)
    d.text((Lw,Lh), textin, font=fnt, fill=(r,g,b,a))

    out = Image.alpha_composite(base, txt)
    out.save("images/NewFolder/textbacktmp.jpg", "JPEG")
    count=count+1
       
#base = Image.open('images/NewFolder/lightning01.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', out.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 20)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = out.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
marginx = 225
marginy = 50
x = width - marginx
y = height - marginy

d.text((x,y), signature_, font=fnt, fill=(0,0,0,256))

out = Image.alpha_composite(out, txt)
out.save("images/NewFolder/tmp.jpg", "JPEG")
# save the image then reopen to put a title
base = Image.open('images/NewFolder/tmp.jpg').convert('RGBA')
#8 5 4 6 3 2
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype("/home/jack/.fonts/Exo-Black.ttf", 50)
# get a drawing context
d = ImageDraw.Draw(txt)

width, height = base.size
# calculate the x,y coordinates of the text
#marginx = 325
#marginy = 75
x = 90
y = 10
#generate a title
title = (generate_the_word("titles.txt"))
d.text((x,y), title , font=fnt, fill=(0,0,0,250))
out2 = Image.alpha_composite(base, txt)
out2.save("images/NewFolder/TM_POST.jpg", "JPEG")

#removed keys for privacy reasons
CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXX'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
#path = 'images/NewFolder'
f = open("art.txt")
text = f.read()
# Build the model.
text_model = markovify.Text(text)
# Print randomly-generated sentences of no more than 140 characters
#http://paulbourke.net/fractals/
#STR = (text_model.make_short_sentence(140))
STR = ("#All_in_One - #WordCloud #Create - Added ability to randomly choose an image background  #Automated")
#PATH = "/home/jack/Desktop/deep-dream-generator/notebooks/STUFF/experiment/experiment8.jpg"
PATH = "images/NewFolder/TM_POST.jpg"
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')
photo = open(PATH,'rb')
response = twitter.upload_media(media=photo)
twitter.update_status(status=STR, media_ids=[response['media_id']])




