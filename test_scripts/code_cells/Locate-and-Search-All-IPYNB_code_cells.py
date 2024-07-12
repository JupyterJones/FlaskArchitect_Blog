!locate *.ipynb >>ALL-IPYNB.list

!ls

files = open("ALL-IPYNB.list").readlines()
for file in files:
    file = file.replace("\n","")
    print(file)
    

from pathlib import Path
import shutil
files = open("ALL-IPYNB.list").readlines()
for file in files:
    file = file.replace("\n","")
    print(file)
    #shutil.copy2(os.path.join(src,fname), trg)
    shutil.copy2(file, ".")
    #shutil.copy2(os.path.join(src,fname), trg)

files = open("ALL-IPYNB.list").readlines()
SEARCH = input("Search for a term: ")
for file in files:
    file = file.replace("\n","")
    if SEARCH in file:
        print(file)

!ls

import os
filelist=[]
files = os.listdir(".")
for file in files:
    filelist.append(file)


print(len(filelist))

SEARCH =input("Search for Term in a notebook:")
for filename in filelist:
    if "checkpoints" not in filename:
        count=0
        data = open(filename).readlines()
        for line in data:
            if SEARCH in line:
                count=count+1
                print( count,filename)



