/media/jack/HDD500/fonts

import os
import shutil

target = '/media/jack/HDD500/fonts/'
for source in FONTS:
    
    try:
        shutil.copy(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())
        pass



#assert not os.path.isabs(source)
#target = os.path.join(target, os.path.dirname(source))

# create the folders if not already exists
#os.makedirs(target)

# adding exception handling


FONTS = []
for fonts in open("fonts").readlines():
    fonts = str(fonts).replace("\n", "")
    FONTS.append(fonts)

print(len(FONTS))

words = ['docker','jack']
def locateem(words,fonts):
    TXT = []
    if any((words in words) for words in FONTS):
        TXT.append(TXT)
        TXT = fonts
        return TXT   

cnt = 0
words = ['docker','jack']
for fonts in FONTS:
    cnt = cnt + 1
    fnt = locateem(words,fonts)
  
    

print (len(fnt))

print(fnt)

lookingfor = "docker"
for cnt in range(0, len(FONTS)):
    if lookingfor in FONTS[cnt]:
        cnt = cnt+1
        if cnt<100:
            print(str(cnt) + ": " + FONT[cnt])

print(FONTS[35])

lookingfor = ["docker","config"]
cnts= 0
items = 0
for fonts in FONTS:
    for items in range(len(lookingfor)):
                dis = lookingfor[items]
                if dis not in fonts:
                    print (dis,fonts)
                    cnts = cnts+1
                    if cnts<10:print (fonts)

item = ["docker","config"]
cnt = 0
for font in FONTS:
    for element in item:
        if "config" not in font:
                cnt = cnt+1
                if cnt<100:print(font)

                


#[x for x in item if x not in z]
#or (if you don't mind losing duplicates of non-unique elements):

#set(item) - set(z)


sFONTS = set(FONTS)
len (set(sFONTS))

item = ["docker","config"]
set(FONTS) - set(item)

item = ["config",1,2,3,4,5,6,7,8,9]
SFONTS = FONTS[:200]
print(len((SFONTS)))
for cnt in range(0,len(SFONTS)):
    if "config" not in FONTS[cnt]:
          print(FONTS[cnt])#+"\n")

#But you could easily do this like:

#[x for x in item if x not in z]

#or (if you don't mind losing duplicates of non-unique elements):

#set(FONTS) - set(items)


item = [0,1,2,3,4,5,6,7,8,9]

print(item[:5])



