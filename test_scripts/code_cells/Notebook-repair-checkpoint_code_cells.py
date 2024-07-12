!ls mouse*.*


import re
import json

s= open("mouse-sizing-n-cropping.ipynb","r")


while True:
    try:
        result = json.loads(s)   # try to parse...
        break                    # parsing worked -> exit loop
    except Exception as e:
        # "Expecting , delimiter: line 34 column 54 (char 1158)"
        # position of unexpected character after '"'
        unexp = int(re.findall(r'\(char (\d+)\)', str(e))[0])
        # position of unescaped '"' before that
        unesc = s.rfind(r'"', 0, unexp)
        s = s[:unesc] + r'\"' + s[unesc+1:]
        # position of correspondig closing '"' (+2 for inserted '\')
        closg = s.find(r'"', unesc + 2)
        s = s[:closg] + r'\"' + s[closg+1:]
print (result)


import re
import json
def fixjson(badjson):
    s = badjson
    idx = 0
    while True:
        try:
            start = s.index( '": "', idx) + 4
            end1  = s.index( '",\n',idx)
            end2  = s.index( '"\n', idx)
            if end1 < end2:
                end = end1
            else:
                end = end2
            content = s[start:end]
            content = content.replace('"', '\\"')
            s = s[:start] + content + s[end:]
            idx = start + len(content) + 6
        except:
            return s
badjson = open("mouse-sizing-n-cropping_mouse-sizing-n-cropping.ipynb","r")
newjson = open("new-mouse-sizing-n-cropping_mouse-sizing-n-cropping.ipynb","w")
TEXT = fixjson(badjson)

for line in TEXT:
    newjson.write(line)
  

newjson.close()  



