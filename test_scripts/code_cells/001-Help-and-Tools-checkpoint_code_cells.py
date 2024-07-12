# To get the directory source of a module
import inspect
#load the module
from PIL import Image
#run inspect.getfile on the module
print(inspect.getfile(Image))

# Example without comments
import os
import inspect
from mpl_toolkits.basemap import Basemap
print(inspect.getfile(Basemap))

# send python help() output to a file
import sys, os
import os.path
# Create target Directory if don't exist
dirName="HelpFiles/"
if not os.path.exists(dirName):
    os.mkdir(dirName)
else:    
    print("Directory " , dirName ,  " already exists")
# import the module if required
# request help in line 25
from PIL import Image
#Create a name for the file (no extension) usually the same as the imported module
NAME="Image"
filename = dirName+NAME+'.help'
if os.path.isfile(filename):
    print ("File exist:",filename)
    
else:
    with open(filename,"w") as helper:
        t = sys.stdout
        sys.stdout = helper
        # line 25 request the help with the Python help command
        #
        help(Image)
        sys.stdout = t
print(filename)        

%%writefile FileSearch.py
#!/usr/bin/env -m python
#Searches a file enter search term and filename
#Range is to give context before and after the search term.
#It defaults to eight lines before the word and eight lines after.
#USAGE:
#from FileSearch import filesearch                
#search ="urcrnrlat"
#filename = "basemap.help"
#filesearch(search,filename,Range=2)
def filesearch(search,filename, Range=8):
    cnt=0
    oldcount = -8
    INDEX = []
    for view in open(filename, "r").readlines():
        cnt=cnt+1
        view=view.replace("\n","")
        if search in view:
            if cnt>oldcount:
                INDEX.append([search,cnt-Range,cnt+Range])
                oldcount=cnt+(Range*2)
    cnt=0
    cnt0=0
    for view in open(filename, "r").readlines():
            cnt=cnt+1
            line=view.replace("\n","")
            for content in INDEX:
                if cnt > int(content[1]) and cnt < int(content[2]):
                    if search not in line:print(cnt,line)
                    if cnt==int(content[2]-1):print("-----------")  
                    if search in line:print("\nSEARCHTERM>> ",cnt,line,"\n") 

#!rm HelpFiles/*.help

!ls HelpFiles

from FileSearch import filesearch                
search ="resize"
filename = "HelpFiles/Image.help"
#filesearch(search,filename,Range=2)
filesearch(search,filename, Range=4)


def ReadLines(START, STOP=20):
    cnt=0
    STOP=STOP+START+1
    for view in open("HelpFiles/Image.help", "r").readlines():
        cnt=cnt+1        
        line=view.replace("\n","")
        if cnt>START and cnt<STOP:
                print(cnt,line)
                
                
ReadLines(729,30)                



