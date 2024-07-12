!locate *.ipynb

!locate *.ipynb > ALL-IPYNB.list

!du ALL-IPYNB.list

cnt = 0
FileList = open("ALL-IPYNB.list", "r").readlines()

ALLnotebooks =[]
for lines in FileList:
    line = lines.replace("\n","")
    if "checkpoints" not in line:
        ALLnotebooks.append(line)
        cnt = cnt +1
        print(cnt,":",line, end=" | ")

len(ALLnotebooks)

# Importing Libraries
import os
import sys
from pathlib import Path
import hashlib
  
  
def FindDuplicate(SupFolder):
    
    # Duplic is in format {hash:[names]}
    Duplic = {}
    for file_name in files:
        
        # Path to the file
        path = os.path.join(folders, file_name)
          
        # Calculate hash
        file_hash = Hash_File(path)
          
        # Add or append the file path to Duplic
        if file_hash in Duplic:
            Duplic[file_hash].append(file_name)
        else:
            Duplic[file_hash] = [file_name]
    return Duplic
  
# Joins dictionaries
def Join_Dictionary(dict_1, dict_2):
    for key in dict_2.keys():
        
        # Checks for existing key
        if key in dict_1:
            
            # If present Append
            dict_1[key] = dict_1[key] + dict_2[key]
        else:
            
            # Otherwise Stores
            dict_1[key] = dict_2[key]
  
# Calculates MD5 hash of file
# Returns HEX digest of file
def Hash_File(path):
    
    # Opening file in afile
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    blocksize=65536
    buf = afile.read(blocksize)
      
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
  
Duplic = {}
folders = Path('/home/jack/')
files = sorted(os.listdir(folders))
for i in files:
    
    # Iterate over the files
    # Find the duplicated files
    # Append them to the Duplic
    Join_Dictionary(Duplic, FindDuplicate(i))
      
# Results store a list of Duplic values
results = list(filter(lambda x: len(x) > 1, Duplic.values()))
if len(results) > 0:
    for result in results:
        for sub_result in result:
            print('\t\t%s' % sub_result)
else:
    print('No duplicates found.')

import hashlib
dir(hashlib)

# dupFinder.py
import os, sys
import hashlib

def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
        afile.close()
        return hasher.hexdigest()


def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
            return dups


findDup("/home/jack")

# checkDuplicates.py
# Python 2.7.6

"""
Given a folder, walk through all files within the folder and subfolders
and get list of all files that are duplicates
The md5 checcksum for each file will determine the duplicates
"""

import os
import hashlib
from collections import defaultdict
import csv

src_folder = "/home/jack"

cnt=0
def generate_md5(fname, chunk_size=1024):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        #cnt=cnt+1    
        # Read the 1st block of the file
        chunk = f.read(chunk_size)
        # Keep reading the file until the end and update hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    # Return the hex checksum
    data = hash.hexdigest()
    print("DATA:"+str(cnt)+":  "+data)
    return data




# The dict will have a list as values
md5_dict = defaultdict(list)
"""
file_types_inscope = ["ppt", "pptx", "pdf", "txt", "html", "ipynb"
                      "mp4", "jpg", "png", "xls", "xlsx", "xml",
                      "vsd", "py", "json","js"]
"""
file_types_inscope = ["ipynb"]

# Walk through all files and folders within directory
for path, dirs, files in os.walk(src_folder):
    #print("Analyzing {}".format(path))
    for each_file in files:
        if each_file.split(".")[-1].lower() in file_types_inscope:
            cnt=cnt+1
            print(each_file)
            # The path variable gets updated for each subfolder
            file_path = os.path.join(os.path.abspath(path), each_file)
            # If there are more files with same checksum append to list
            md5_dict[generate_md5(file_path)].append(file_path)

# Identify keys (checksum) having more than one values (file names)
duplicate_files = (
    val for key, val in md5_dict.items() if len(val) > 1)
# Write the list of duplicate files to csv file
with open("duplicates.csv", "w") as log:
    # Lineterminator added for windows as it inserts blank rows otherwise
    csv_writer = csv.writer(log, quoting=csv.QUOTE_MINIMAL, delimiter=",", lineterminator="\n")
    header = ["File Names"]
    csv_writer.writerow(header)
    for file_name in duplicate_files:
        csv_writer.writerow(file_name)

print("Done")


import os
import hashlib
from collections import defaultdict
import csv

src_folder = "/home/jack"

cnt=0
def generate_md5(fname, chunk_size=1024):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        #cnt=cnt+1    
        # Read the 1st block of the file
        chunk = f.read(chunk_size)
        # Keep reading the file until the end and update hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    # Return the hex checksum
    data = hash.hexdigest()
    print("DATA:"+str(cnt)+":  "+data)
    return data

generate_md5(fname, chunk_size=1024)

!detox /home/jack/Desktop/LUA/BrynMawrCollege/

with open("duplicates.csv", "r") as log:


