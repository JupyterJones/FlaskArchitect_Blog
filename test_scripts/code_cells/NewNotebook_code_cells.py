# import wikipedia doing a wikipedia.search
# searches for wiki pages concerning the topic
from time import sleep
import wikipedia
from ast import literal_eval
# opens a text input and prints
# Research : topic entered
#topic = raw_input("Research : ")
f = open("super.txt", "a")
rows = wikipedia.search("micro processor")
for row in rows:
    nrows = wikipedia.search(row)
    for nrow in nrows:
            nrow = nrow.encode('ascii', 'ignore')
            Sum = wikipedia.summary(nrow)
            f.write(Sum)   
    

Python_Cookbook_3rd_Edition.txt
Automate-the-Boring-Stuff.txt
WebScrapingwithPython.txt


!ls *.txt

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'pdfs.db'
conn = sqlite3.connect(Dbase)
conn.text_factory = str
c = conn.cursor()
c.execute('''
CREATE VIRTUAL TABLE IF NOT EXISTS pdfs
USING FTS3(text, title);
''')

title = "Web Scraping with Python"
#text = wikipedia.summary("Heaven")
#text = text.encode("ascii", "ignore")
#text = text.replace(". ",". \n")

reaD = open("pdf.txt","r")
lines = reaD.readlines()
for line in lines:
    line = line.decode("utf8")
    conn = sqlite3.connect(Dbase)
    c = conn.cursor()
    c.execute("INSERT INTO pdfs  VALUES (?, ?)", (line, title))
    conn.commit()
    conn.close()

%%writefile generate.py
#!/usr/bin/python

import re
import random
import sys

# These mappings can get fairly large -- they're stored globally to
# save copying time.

# (tuple of words) -> {dict: word -> number of times the word appears following the tuple}
# Example entry:
#    ('eyes', 'turned') => {'to': 2.0, 'from': 1.0}
# Used briefly while first constructing the normalized mapping
tempMapping = {}

# (tuple of words) -> {dict: word -> *normalized* number of times the word appears following the tuple}
# Example entry:
#    ('eyes', 'turned') => {'to': 0.66666666, 'from': 0.33333333}
mapping = {}

# Contains the set of words that can start sentences
starts = []

# We want to be able to compare words independent of their capitalization.
def fixCaps(word):
    # Ex: "FOO" -> "foo"
    if word.isupper() and word != "I":
        word = word.lower()
        # Ex: "LaTeX" => "Latex"
    elif word [0].isupper():
        word = word.lower().capitalize()
        # Ex: "wOOt" -> "woot"
    else:
        word = word.lower()
    return word

# Tuples can be hashed; lists can't.  We need hashable values for dict keys.
# This looks like a hack (and it is, a little) but in practice it doesn't
# affect processing time too negatively.
def toHashKey(lst):
    return tuple(lst)

# Returns the contents of the file, split into a list of words and
# (some) punctuation.
def wordlist(filename):
    f = open(filename, 'r')
    wordlist = [fixCaps(w) for w in re.findall(r"[\w']+|[.,!?;]", f.read())]
    f.close()
    return wordlist

# Self-explanatory -- adds "word" to the "tempMapping" dict under "history".
# tempMapping (and mapping) both match each word to a list of possible next
# words.
# Given history = ["the", "rain", "in"] and word = "Spain", we add "Spain" to
# the entries for ["the", "rain", "in"], ["rain", "in"], and ["in"].
def addItemToTempMapping(history, word):
    global tempMapping
    while len(history) > 0:
        first = toHashKey(history)
        if first in tempMapping:
            if word in tempMapping[first]:
                tempMapping[first][word] += 1.0
            else:
                tempMapping[first][word] = 1.0
        else:
            tempMapping[first] = {}
            tempMapping[first][word] = 1.0
        history = history[1:]

# Building and normalizing the mapping.
def buildMapping(wordlist, markovLength):
    global tempMapping
    starts.append(wordlist [0])
    for i in range(1, len(wordlist) - 1):
        if i <= markovLength:
            history = wordlist[: i + 1]
        else:
            history = wordlist[i - markovLength + 1 : i + 1]
        follow = wordlist[i + 1]
        # if the last elt was a period, add the next word to the start list
        if history[-1] == "." and follow not in ".,!?;":
            starts.append(follow)
        addItemToTempMapping(history, follow)
    # Normalize the values in tempMapping, put them into mapping
    for first, followset in tempMapping.iteritems():
        total = sum(followset.values())
        # Normalizing here:
        mapping[first] = dict([(k, v / total) for k, v in followset.iteritems()])

# Returns the next word in the sentence (chosen randomly),
# given the previous ones.
def next(prevList):
    sum = 0.0
    retval = ""
    index = random.random()
    # Shorten prevList until it's in mapping
    while toHashKey(prevList) not in mapping:
        prevList.pop(0)
    # Get a random word from the mapping, given prevList
    for k, v in mapping[toHashKey(prevList)].iteritems():
        sum += v
        if sum >= index and retval == "":
            retval = k
    return retval

def genSentence(markovLength):
    # Start with a random "starting word"
    curr = random.choice(starts)
    sent = curr.capitalize()
    prevList = [curr]
    # Keep adding words until we hit a period
    while (curr not in "."):
        curr = next(prevList)
        prevList.append(curr)
        # if the prevList has gotten too long, trim it
        if len(prevList) > markovLength:
            prevList.pop(0)
        if (curr not in ".,!?;"):
            sent += " " # Add spaces between words (but not punctuation)
        sent += curr
    return sent

def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ' + sys.argv [0] + ' text_source [chain_length=1]\n')
        sys.exit(1)

    filename = sys.argv[1]
    markovLength = 1
    if len (sys.argv) == 3:
        markovLength = int(sys.argv [2])

    buildMapping(wordlist(filename), markovLength)
    print genSentence(markovLength)

if __name__ == "__main__":
    main()

from Immanip import SwapPalettes
filename0 = '/home/jack/Desktop/text_stuff/instagram/PalletteTemp.png'
filename1 = '/home/jack/Desktop/text_stuff/instagram/sea1.jpg'
filename = 'pallet_test.jpg'
SwapPalettes.swappalettes(filename0,filename1,filename)

!python generate.py grimm.txt 6

!python generate.py grimm.txt 8


!python generate.py hek.txt 6

%reset -f

import SearchFilename
filename = "grimm.txt"
length = 4
SearchFilename.searchfilename(filename, length)

import SearchFilename
filename = "Automate-the-Boring-Stuff.txt"
length = 4
SearchFilename.searchfilename(filename, length)

#%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/SearchFilename.py
'''
Search a filename for a phrase and how many following lines to display
USAGE:
import SearchFilename
filename = "hek.txt"
length = 4
SearchFilename.searchfilename(filename, length)
'''
def searchfilename(filename, length):
    f = open(filename, "r")
    searchlines = f.readlines()
    f.close()
    search = str(raw_input("Search Phrase"))
    for i, line in enumerate(searchlines):
        if search in line: 
            for l in searchlines[i:i+length]: print l,
            print

f = open("hek.txt", "r")
searchlines = f.readlines()
f.close()
search = str(raw_input("Search Phrase"))
for i, line in enumerate(searchlines):
    if search in line: 
        for l in searchlines[i:i+8]: print l,
        print

# Open file for reading
fo = open('hek.txt')

# Read the first line from the file
line = fo.readline()

# Initialize counter for line number
line_no = 1
search_str = raw_input("Search Phrase")
# Loop until EOF
while line != '' :
        # Search for string in line
        index = line.find(search_str)
        if ( index != -1) :
            print("[", line_no, ",", index, "] ", line," ")
            # Read next line
            line = fo.readline()  

            # Increment line counter
            line_no += 1
# Close the files
fo.close()


f = open("file.txt", "r")
searchlines = f.readlines()
f.close()
for i, line in enumerate(searchlines):
    if "searchphrase" in line: 
        for l in searchlines[i:i+3]: print l,
        print


# Open file for reading
fo = open('grimm.txt')

# Read the first line from the file
line = fo.readline()

# Initialize counter for line number
line_no = 1
search_str = str(raw_input("Search Phrase"))
# Loop until EOF
while line != '' :
        # Search for string in line
        index = line.find(search_str)
        if ( index != -1) :
            print(fname, "[", line_no, ",", index, "] ", line," ")
            # Read next line
            line = fo.readline()  

            # Increment line counter
            line_no += 1
# Close the files
fo.close()


import timeit

def search(word=None,source=None):
    word = "is"
    source = "Lorem Ipsum is simply dummy text"
    return source.lower().find(word.lower())

print timeit.timeit(search, number=1000)

!locate Txmanip

%%writefile /home/jack/anaconda2/lib/python2.7/site-packages/Txmanip/Txsearch.py
# Ask to enter string to search
# this will search all *.txt files in the current directory
# input window will ask "Search Phrase" 
"""
import Txsearch
Txsearch.txsearch()
"""
import os
import timeit
def txsearch():
    Sstring = raw_input("Search Phrase")
    for fname in os.listdir('./'):
       # Apply file type filter   
       if fname.endswith(".txt"):
            # Open file for reading
            fo = open(fname)
            # Read the first line from the file
            line = fo.readline()
            # Initialize counter for line number
            line_no = 1
            # Loop until EOF
            while line != '' :
                    index = line.find(Sstring)
                    if ( index != -1) :
                        # Set some parameters no lines longer than 240 characters 
                        # or less than search phrase +30 characters 
                        if len(line)< 240 and len(line)> len(Sstring)+20 :
                            #print(fname, "[", line_no, ",", index, "] ", line)
                            #print fname,line[1:-8],"  "
                            print fname,line_no,line
                    # Read next line
                    line = fo.readline()  
                    # Increment line counter
                    line_no += 1
            # Close the files
            fo.close()
            
txsearch()

import Txsearch
Txsearch.txsearch()

import os

# Ask to enter string to search
Sstring = raw_input("Search Phrase")
for fname in os.listdir('./'):
   # Apply file type filter   
   if fname.endswith(".txt"):
        # Open file for reading
        fo = open(fname)
        # Read the first line from the file
        line = fo.readline()
        # Initialize counter for line number
        line_no = 1
        # Loop until EOF
        while line != '' :
                index = line.find(Sstring)
                if ( index != -1) :
                    # Set some parameters no lines longer than 240 characters 
                    # or less than search phrase +30 characters 
                    if len(line)< 240 and len(line)> len(Sstring)+20 :
                        #print(fname, "[", line_no, ",", index, "] ", line)
                        #print fname,line[1:-8],"  "
                        print fname,line_no,line
                # Read next line
                line = fo.readline()  
                # Increment line counter
                line_no += 1
        # Close the files
        fo.close()


import timeit
# Open file for reading
fo = open('hek.txt')

# Read the first line from the file
line = fo.readline()

def search():
    # Read the first line from the file
    line = fo.readline()

    word = "is"
    source = "Lorem Ipsum is simply dummy text"
    return source.lower().find(word.lower())

print timeit.timeit(search, number=1000)



