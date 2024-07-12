info = open("list.html", "r").read()
print(info)

!pwd

AustralianAnimals = []
info1 = info.replace("<h1>","xxx\n<h1>")
info2 = info1.replace("</h1>","</h1>\nxxx")
info3 = info2.split("\n")
for line in info3:
    if "<h2>" in line and "span" not in line and "<br>" not in line:
        line = line.replace("<h2>","")
        line = line.replace("</h2>","")
        #print (line)
        AustralianAnimals.append(line)

import re

#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

[x.group() for x in re.finditer( r'h (.*?) h', info)]
# Output: ['all cats are', 'all dogs are']

print(AustralianAnimals)

import re
s = info
pattern = "<h1>(.*?)</h2>"

substring = re.search(pattern, s).group(1)
print(substring)

import re
sequence = 'aaabbbaaacccdddeeefff'
query = 'aaa'
r = re.compile(query)
[[m.start(),m.end()] for m in r.finditer(sequence)]

import re
start = '<h1>'
end = '</h1>'
s = info
txt= re.findall(start)+len(start),s


print(txt)

# Open file
count=0
f = info
lines = f.split("\n")
for line in lines:
    count=count+1
    if "h1" in line:
        print("\n",count,line,"\n")

    

# Open file
count=0
f = open('list.html', 'r').read()
lines = f.split("\n")
for line in lines:
    if "<h1>" in line:
            count=count+1
            print("\n",count,line,"\n")

    

#[x.group() for x in re.finditer(r'{.*}', s)]
[x.group() for x in re.finditer(r'<h1>.*', s)]

result = re.findall(r'var="(.*?)"', test)
print(result)  # ['this', 'that']

re.findall( r'h1 (.*?) h1', s)
# Output: ['cats', 'dogs']

re.findall( r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')
# Output: ['cats', 'dogs']

[x.group() for x in re.finditer( r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')]
# Output: ['all cats are', 'all dogs are']

s = info

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""


print (find_between( s, "<h1>", "</h1>" ))
print (find_between_r( s, "<h1>", "</h1>" ))

cnt=0
info1 = info.split("\n")
for line in info1:
    cnt=cnt+1
    if "<h1>" in line: # and "</h1>" in line:
        print(cnt,line,"\n")

str = '<h1>purple</h1> alice-b@google.com monkey <h1>dishwasher</h1> alice-b@google.com monkey dishwasher'


str = '<h1>purple</h1> alice-b@google.com monkey <h1>dishwasher</h1> alirce -b@google.com monkey dishwasher'
match = re.search(r'\w+r\w+', str)
if match:
    print(match.group())  ## 'b@google'

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group()) ## 'found word:cat'
else:
    print('did not find')

import re

str = info
match = re.search(r'word:Animal', str)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group()) ## 'found word:cat'
else:
    print('did not find')

match = re.search("h1", s)
for mat in match:
    print (mat)



