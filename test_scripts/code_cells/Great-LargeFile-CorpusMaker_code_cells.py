import os  
import string
import io
from ruamel.yaml import YAML
from ruamel.yaml.reader import Reader

yaml = YAML(typ='safe')

def strip_invalid(s):
    res = ''
    for x in s:
        if Reader.NON_PRINTABLE.match(x):
            # res += '\\x{:x}'.format(ord(x))
            continue
        res += x
    return res

count = 0
newfile = "64-80test.json"
clean = open(newfile, "w")
clean.write("{\n \"conversations\": \n[\n")
filename = "result.txt"
with io.open(filename, mode="r", encoding="utf-8") as infile:
#with open() as infile:
    for line in infile:
        line = line.encode('utf8').decode('latin1')
        line = line.replace("\n","")
        line =line.replace("\"","'")
        line=line.replace("\\","")
        line=line.replace("{","")
        line=line.replace("}","")
        line=line.replace("[","")
        line=line.replace("]","")        
        line = strip_invalid(line)
        line = line.replace("-","")
        count = count +1
        txt = "[\""
        if(count % 2 != 0):
            #newline.append(""+line +"")
            txt2 = txt+line
            #print(txt2)
            #clean.write(txt2)
        if(count % 2 == 0):
            #newline.append(""+line +"")
            txt3 = txt2 +"\",\n\""+ line +"\"],\n"
            #print(count,txt3)
            #clean.write(txt3)        
            if count>6400000 and count<8000000:clean.write(txt3)
            if count>8000000:break    
            

clean.close()          

count=0 
newfile = "testfile.json"
clean = open(newfile, "r").readlines()
for line in clean:
    count=count+1
print(count)





from ruamel.yaml import YAML
from ruamel.yaml.reader import Reader

yaml = YAML(typ='safe')

def strip_invalid(s):
    res = ''
    for x in s:
        if Reader.NON_PRINTABLE.match(x):
            # res += '\\x{:x}'.format(ord(x))
            continue
        res += x
    return res


def convert(filename) :
    newfile = "testfile.json"
    clean = open(newfile, "w")
    count = 0
    #ALL = [] 
    #f = io.open(filename, mode="r", encode("latin_1"),decode("utf_8")).readlines()
    with io.open(filename, mode="r", encoding="utf-8").readlines()
    #f = open(filename, "r").readlines()
    for line in f:
        line = line.encode('utf8').decode('latin1')
        line = line.replace("\n","")
        line =line.replace("\"","'")
        line=line.replace("\\","")
        line=line.replace("{","")
        line=line.replace("}","")
        line = strip_invalid(line)
        count=count+1
        newline =[]
        txt = "[\""
        if(count % 2 != 0):
            newline.append(""+line +"")
            txt2 = txt+line
            clean.write(txt2)
        if(count % 2 == 0):
            newline.append(""+line +"")
            txt3 = txt2 +"\",\n\""+ line +"\"],\n"
            clean.write(text3)
        if count>200:
            break 
            clean.close()
    return print(count)

        

filename ="result.txt"    
convert(filename)

import os
filez = os.listdir('/home/jack/Desktop/PAV/opensubtitles/raw/lines/')

print(filez[0],filez[1])

import glob
files = glob.glob( '/home/jack/Desktop/PAV/opensubtitles/raw/lines/*' )

cat

import glob
files = glob.glob( '/home/jack/Desktop/PAV/opensubtitles/raw/lines/*' )

with open( 'result.txt', 'w' ) as result:
    for file_ in files:
        for line in open( file_, 'r' ):
            result.write( line )

result.close()



filenames = ['file1.txt', 'file2.txt']
  
# Open file3 in write mode
with open('file3.txt', 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")

import os  
import string
import io

from ruamel.yaml import YAML
from ruamel.yaml.reader import Reader

yaml = YAML(typ='safe')

a = ""
b=""
c=""
d=""
e=""
f=""

def strip_invalid(s):
    res = ''
    for x in s:
        if Reader.NON_PRINTABLE.match(x):
            # res += '\\x{:x}'.format(ord(x))
            continue
        res += x
    return res


def convert(filename) :
    count = 0
    #ALL = [] 
    
    #f = io.open(filename, mode="r", encode("latin_1"),decode("utf_8")).readlines()
    f = io.open(filename, mode="r", encoding="utf-8").readlines()
    #f = open(filename, "r").readlines()
    for line in f:
        line = line.encode('utf8').decode('latin1')
        line = line.replace("\n","")
        line =line.replace("\"","'")
        line=line.replace("\\","")
        line=line.replace("{","")
        line=line.replace("}","")
        line = strip_invalid(line)
        count=count+1
        newline =[]
        txt = "[\""
        if(count % 2 != 0):
            newline.append(""+line +"")
            txt2 = txt+line
        if(count % 2 == 0):
            newline.append(""+line +"")
            txt3 = txt2 +"\",\n\""+ line +"\"],\n"
            
    return #print("--\n",ALL)
subb=[a,b,c,d,e,f]
print (subb) 
for AA in subb:
    print(AA)
    cnt=0
    SUB = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for sub in SUB:
         FS = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
         for L in FS:
             #def savjson(data):
             filez= (+subb+sub+L+SAjson.jsonS)
             print (filez)
             datain = open("test/("+subb+sub+L+"json.json","w")
             datain.write("{\n \"conversations\": \n[\n")
             convert("/home/jack/Desktop/PAV/opensubtitles/raw/lines/lines-"+subb+"sub+L+") 
             print('XXXXX,',convert)
             print (convert)
             datain.write("]}")
             datain.close() 
             file = "test/"+subb+sub+L+"json.json"
             print(file)
    
    
             data = open(file).readlines()
             newfile = "test/C"+os.path.basename(file)
             clean = open(newfile, "w")
             count = 0
             for line in data:
                 count=count+1
                 if count<4999:
                     #print(line)
                    clean.write(line)
                 if count>4998:
                     line = line.replace("],","]")
                     clean.write(line)
                     #print(line)

      
         clean.close()        


import os
subb=['a','b','c','d','e','f']
sub = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
SUB = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
#print (subb) 
for A in subb:
    for B in sub:
        for C in SUB:
            print(A+B+C)

#os.path.join(p

subb=['a','b','c','d','e','f']
#print (subb) 
for AA in subb:
    #print(AA)
    cnt=0
    SUB = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for sub in SUB:
         FS = ['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
         for L in FS:
             #def savjson(data):
             filez= str(subb)+str(sub)+str(L)+str('SAjson.json')
             print (os.path.join(filez))



