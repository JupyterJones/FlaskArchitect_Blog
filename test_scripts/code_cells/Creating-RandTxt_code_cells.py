!find ~/ -name '*.py' >>python-files.txt

PYFILE = set()
cnt = 0
files = open("python-files.txt", "r")
for file in files:
    cnt = cnt +1
    if "KEY" not in file and "key" not in file:
        file = file.replace("\n","")
        if cnt < 30: print (file)
        PYFILE.add(file)

print(len (PYFILE))

import random
from random import randint
PYFILE = set()
cnt = 0
files = open("python-files.txt", "r")
for file in files:
    cnt = cnt +1
    if "KEY" not in file and "key" not in file:
        file = file.replace("\n","")
        PYFILE.add(file)
PYFILES = []
for file in PYFILE:
    PYFILES.append(file)        
        
def primary(cnt):
    ind=len(PYFILES)
    IND = randint(0,ind)
    quotes = open(PYFILES[IND], errors='replace').readlines()
    #quotes = f.readlines()
    try:
        quote = []
        sampling = random.sample(quotes, 6)
        for sample in sampling:
            if len(sample)>3:
                #sample = sample.replace("\"","'")
                #sample = sample.replace("\n","")
                quote.append(sample)
        #print("___________________")
        return quote
    except:
        pass
txtout = open("outPUT.txt","a")
for cnt in range(0,2000):
        text = primary(cnt)
        if len(str(text))>10:
            for samp in text:
                #print(samp)
                if len(samp[:83])<84:
                    txtout.write(samp[:83])
        txtout.write("\nXXXXX")    
            


txtout.close()



#%%writefile randtext.py
from random import randint
import re
"""
Create a text file called outPUT.txt
break it into sections you woul like to return with XXXXX
That will split the file into segments.
Those segments will randomly be chosen and returned.
example:
XXXXX        cmd.force = True
                          infiles=1, outfile='', func='func', args=())
        cmd.make_file(infiles='in', outfile='out', func='func', args=())
        cmd.ensure_dirname('option1')
        # making sure execute gets called properly

XXXXX
XXXXX                else:
        __getattr__ = __setattr__ = lambda self, *_: report()
            except messaging.JsonIOError as exc:
    @property

XXXXXdef replace_types(type_: Any, type_map: Mapping[Any, Any]) -> Any:
    # Setting the return type as Type[Any] instead of Type[BaseModel] prevents PyCh                model_name,
    return type_map.get(type_, type_)
            passed to `cls` as type variables.

XXXXX        ValidationFailure(func=mac_address, args={'value': '00:00:00:00:00'})
        >>> mac_address('00:00:00:00:00')
    Examples::

XXXXX
"""
def randTXT():
    textout = open("outPUT.txt","r").read()
    out = str(textout).split("XXXXX")
    num = len(out)-1
    ID = randint(0,num)
    STr = out[ID]
    if len(STr)<10:randTXT()
    STr = re.sub(' +', ' ', STr)
    return STr


from randtext import randTXT
STR = randTXT()
print (STR)

import random
from random import randint
PYFILE = set()
cnt = 0
files = open("python-files.txt", "r")
for file in files:
    cnt = cnt +1
    if "KEY" not in file and "key" not in file:
        file = file.replace("\n","")
        PYFILE.add(file)
PYFILES = []
for file in PYFILE:
    PYFILES.append(file)        
        
def primary(cnt):
    ind=len(PYFILES)
    IND = randint(0,ind)
    f = open(PYFILES[IND])
    quotes = f.readlines()
    f.close()
    try:
        quote = []
        sampling = random.sample(quotes, 6)
        for sample in sampling:
            if len(sample)>3:
                #sample = sample.replace("\"","\"")
                sample = sample.replace("\n","")
                quote.append(sample)
        #print("___________________")
        return quote
    except:
        pass
txtout = open("outPUT.txt","a")
for cnt in range(0,1000):
        text = primary(cnt)
        if len(str(text))>10:
            for samp in text:
                #print(samp)
                txtout.write("\""+samp[:83]+"\",\n")
            #print("-------------------------")
            txtout.write("],\n[")

txtout()

ind=len(PYFILES)
IND = randint(0,ind)
PYFILES[IND]

PYFILES = []
for file in PYFILE:
    PYFILES.append(file)

test = "<https://books.google.com/ngrams/graph?content=canceled%2Ccancelled&year_start=1800&year_end=2000&corpus=18&smoothing=3&share=&direct_url=t1%3B%2Ccancele"

print(test[:83])




