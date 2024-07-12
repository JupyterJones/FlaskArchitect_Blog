<a href='#the_destination'>Link to the destination'</a>

<a id='the_destination'></a>



# Bible_Search.ipynb
Complete SQLite with FTS3<b
Search by words/term
search by line number
search chapter and verse
search by line span start line and stopline

colorific.ipynb

Crawler.ipynb

Dream-and-Post-to-Twitter.ipynb makes dreams but is not compley topost

GO-Simple-Example.ipynb

ImageBot1.py.ipynb

ImageBot_Triangles.ipynb
ImageBot1.py
Turns images into triangles

ImageEffectsBot-bak.ipynb

ImageEffectsBot-Copy1.ipynb

Image-Maker.ipynb
GOOD RANDOM resize and crop  Sepia experiment
emboss -EXPERIMENT
colage maker
PIL filters
Large collagemaker.py

imfractal.ipynb

INDEX.ipynb

MaskGenerator-Copy1.ipynb

create a sharp and a blurred mask from random images 

MEAN_Graphics.ipynb

Meanshift Image Segmentation.ipynb

Meanshift In 2D.ipynb

Palett_Swap_ARRAY_STUFF.ipynb

Pattern-Recognition.ipynb

PIL-ONLY.ipynb

POST_NOW.ipynb

pygame.ipynb

rand-palette-post.ipynb

Rorschach-ImageMaker.ipynb

Filtering twitter text</br>
Formating Twitter Text</br>
Using a Key.py for authorization<b />
Saving results to a text file<b />

Picks a Random Image and Random Titles
Also and Signs and Posts to Twitter

TwitterBot.ipynb
Images and more

Introduction to markovify 
twitterpost.py

twitterpost

# Twitter-image-and-comment-manual-upload.ipynb
#%%writefile twitterpost.py
ALL IN ONE: Get image, place text in it and publish

Twitter-Wordcloud-Image-Generator.ipynb
Wordcloud-Image
post an image file of your choice with text that you enter.
open to view ImageChops.py

TXT_and_CSV-Copy1.ipynb

TXT_and_CSV.ipynb

Utilities.ipynb


Wordcloud-Image-Generator-for github.ipynb


NewNotebook1.ipynb
NewNotebook2.ipynb
NewNotebook.ipynb



TwitterBot.ipynb


TXT_and_CSV-Copy1.ipynb
TXT_and_CSV.ipynb
Utilities.ipynb
Wordcloud-Image-Generator-for github.ipynb




!ls images/

# an Explinatione with examples of the terms argv and if __name__ == "__main__"
import sys
a = sys.argv[2]
print a 

also:
    Dec2Year.py Change a decimal year into full readable year
    and a little about Formating 

import glob
print glob.glob("/home/jack/*.txt")

#list files only
import os
print os.walk('../imagebot').next()[2]

import os
import glob
image_list = []

for ext in ('jpg', 'jpeg', 'bmp', 'png', 'gif'):
    search_str = os.path.join('../imagebot/','*.%s' % ext)
    image_list.extend(glob.glob(search_str))

#out = open(os.path.join('../imagebot/', 'index.txt'), 'w')
print image_list

!mkdir bak

#list directories only
import os
print os.walk('../imagebot').next()[1]

#copy all files to a new location
import os
import shutil
src = '../imagebot/'
dest = '../imagebot/bak/'
src_files = os.listdir(src)
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if (os.path.isfile(full_file_name)):
        shutil.copy(full_file_name, dest)

#to copy a file 
from shutil import copyfile
copyfile(src, dst)

#list all jpg and png in imagebot nad subdirectories
import os
def fileList():
    matches = []
    for root, dirnames, filenames in os.walk('../imagebot/'):
        for filename in filenames:
            if filename.endswith(('.jpg', '.png')):
                matches.append(os.path.join(root, filename))
    return matches
fileList()

