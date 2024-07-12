info = open("list.html", "r").read()
#print(info)

txt = "The rain in Spain"
print(txt[:3])

import re
cnt = 0
STRING =info
#Split the string at every white-space character:
x = re.split("\s", STRING[:500])
for word in x:
    cnt=cnt+1
    if cnt<100:
        print(x)

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object 

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) 

#Print the string passed into the function:
import re

txt = "The rain in Spain The regular expression looks for any words that starts with an upper case "
x = re.search(r"\bS\w+", txt)
print(x.string) 

import re

txt = "The rain in Spain The regular expression looks for any words that Starts with an upper case "
x = re.search(r"\bS\w+", txt)
print(x.group()) 

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 



