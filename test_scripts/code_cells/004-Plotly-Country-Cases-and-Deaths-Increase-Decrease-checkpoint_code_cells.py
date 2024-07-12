import requests as req
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
CSSEGIS =[]
resp = req.get(URL)
text = resp.content
data=text.splitlines()
cnt=0
for line in data:
    cnt=cnt+1
    # remove the b' befor the line
    line = line.decode('utf-8')
    line=line.lstrip(",")
    CSSEGIS.append(line)

import plotly.graph_objects as go
import time
from PIL import Image
#SEARCH = input("SEARCH: ")
#SEARCH = "Brazil"
#SEARCH = "Spain"
#SEARCH = "Philippine"
#SEARCH = "Ecuador"
#SEARCH = "Germany"
#SEARCH = "Japan"
SEARCH = "US"
#SEARCH="Mexico"
cnt = 0
CNTS=0
counts=[]
for line in CSSEGIS:
    if cnt==0:print(line)
    cnt=cnt+1
    line=line.lstrip(",")
    #if SEARCH in line:print(line)
    if SEARCH in line:
        line=line.split(",0,0",1)[-1]
        line = "0,0"+line
        print(line)
        entry = line
        entry=entry.split(",")
        for num in entry:
            counts.append(int(num))
            
filename0 = time.strftime("images/"+SEARCH+"_Deaths_%Y%m%d%H%M%S.png")            
fig = go.Figure()
fig.add_trace(go.Scatter(y=counts))
fig.add_trace(go.Bar(y=counts))
fig.update_layout(title = SEARCH+' CONDID-19 Deaths')
fig.show() 



IncreasePerDay=[]
All = (len(counts))
for x in range(0,All):
    try:
        Sum = (counts[x+1]-counts[x])
        print(Sum, end = " ")
        IncreasePerDay.append(Sum)
    except:
        pass
    
filename1 = time.strftime("images/"+SEARCH+"_IncreasePerDay"+"_%Y%m%d%H%M%S.png")
fig = go.Figure()
fig.add_trace(go.Scatter(y=IncreasePerDay))
fig.add_trace(go.Bar(y=IncreasePerDay))
fig.update_layout(title = SEARCH+' Increase Each day CONDID-19 Cases')
fig.show() 


import plotly.graph_objects as go
import time
from PIL import Image

import requests as req
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
CSSEGIS =[]
resp = req.get(URL)
text = resp.content
data=text.splitlines()
cnt=0
for line in data:
    cnt=cnt+1
    # remove the b' befor the line
    line = line.decode('utf-8')
    line=line.lstrip(",")
    CSSEGIS.append(line)

#SEARCH = input("SEARCH: ")
#SEARCH = "Brazil"
#SEARCH = "Spain"
SEARCH = "Philippine"
#SEARCH = "Ecuador"
#SEARCH = "Germany"
#SEARCH = "Japan"
#SEARCH = "US"
SEARCH="Mexico"
cnt = 0
CNTS=0
counts=[]
for line in CSSEGIS:
    if cnt==0:print(line)
    cnt=cnt+1
    line=line.lstrip(",")
    #if SEARCH in line:print(line)
    if SEARCH in line:
        line=line.split(",0,0",1)[-1]
        line = "0,0"+line
        print(line)
        entry = line
        entry=entry.split(",")
        for num in entry:
            counts.append(int(num))
            
filename0 = time.strftime("images/"+SEARCH+"_"+STAT+"Deaths_%Y%m%d%H%M%S.png")            
fig = go.Figure()
fig.add_trace(go.Scatter(y=counts))
fig.add_trace(go.Bar(y=counts))
fig.update_layout(title = SEARCH+' CONDID-19 Deaths')
fig.show() 



IncreasePerDay=[]
All = (len(counts))
for x in range(0,All):
    try:
        Sum = (counts[x+1]-counts[x])
        print(Sum, end = " ")
        IncreasePerDay.append(Sum)
    except:
        pass
    
filename1 = time.strftime("images/"+SEARCH+"_"+STAT+"IncreasePerDay"+"_%Y%m%d%H%M%S.png")
fig = go.Figure()
fig.add_trace(go.Scatter(y=IncreasePerDay))
fig.add_trace(go.Bar(y=IncreasePerDay))
fig.update_layout(title = SEARCH+' Increase Each day CONDID-19 Cases')
fig.show() 

import requests as req
import time
from datetime import datetime
from datetime import date, timedelta
yesterday = datetime.utcnow() - timedelta(days=2)
YesterdaysGMT=yesterday.strftime('%m-%d-%Y')

import requests as req
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
CSSEGIS =[]
resp = req.get(URL)
text = resp.content
filename="csv/"+URL.split("/")[-1]
TEMP = open(filename,"wb")
TEMP.write(text)
TEMP.close()
print(filename)

import plotly.graph_objects as go
import time
from PIL import Image

LASTFILE="csv/time_series_covid19_deaths_global.csv"


STAT =LASTFILE[57:-4]
DataIn = open(LASTFILE).readlines()

#SEARCH = input("SEARCH: ")
#SEARCH = "Brazil"
#SEARCH = "Spain"
#SEARCH = "Philippine"
#SEARCH = "Ecuador"
SEARCH = "Germany"
#SEARCH = "Japan"
#SEARCH = "US"
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    if cnt==0:print(line)
    cnt=cnt+1
    line=line.lstrip(",")
    #if SEARCH in line:print(line)
    if SEARCH in line:
        line=line.split(",0,0",1)[-1]
        line = "0,0"+line
        print(line)
        entry = line
        entry=entry.split(",")
        for num in entry:
            counts.append(int(num))
            
filename0 = time.strftime("images/"+SEARCH+"_"+STAT+"Deaths_%Y%m%d%H%M%S.png")            
fig = go.Figure()
fig.add_trace(go.Scatter(y=counts))
fig.add_trace(go.Bar(y=counts))
fig.update_layout(title = SEARCH+' CONDID-19 Deaths')
fig.show() 



IncreasePerDay=[]
All = (len(counts))
for x in range(0,All):
    try:
        Sum = (counts[x+1]-counts[x])
        print(Sum, end = " ")
        IncreasePerDay.append(Sum)
    except:
        pass
    
filename1 = time.strftime("images/"+SEARCH+"_"+STAT+"IncreasePerDay"+"_%Y%m%d%H%M%S.png")
fig = go.Figure()
fig.add_trace(go.Scatter(y=IncreasePerDay))
fig.add_trace(go.Bar(y=IncreasePerDay))
fig.update_layout(title = SEARCH+' Increase Each day CONDID-19 Cases')
fig.show() 

data="Ecuador,-1.8312,-78.1834,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,3,5,7,14,18,27,28,34,36,48,58,60,75,93,120,145,172,180,191,191,242,272,297,315,333,355,369,388,403,421,456,474,507,520,537,560,576,576"

data=data.split(",0,0",1)[-1]
print ("0,0"+data)



