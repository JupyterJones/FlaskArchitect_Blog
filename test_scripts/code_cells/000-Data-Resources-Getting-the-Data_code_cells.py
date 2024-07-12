import requests as req
import time
DATE = time.strftime("%m-%d-%H_")
URL ="https://covid.ourworldindata.org/data/owid-covid-data.csv"
#create a date oriented filename and print it
filename="csv/"+URL.split("/")[-1]
print(filename)

import os.path
import os
DirName = 'csv'    
# Create 'DirName' if don't exist
if not os.path.exists(DirName):
    os.mkdir(DirName)
    print('Directory ' , DirName ,  ' Created.')
else:    
    print('Directory ' , DirName ,  ' already exists.')

import requests as req
URL="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
resp = req.get(URL)
text = resp.content
#create a date oriented filename and print it
filename="csv/"+URL.split("/")[-1]
STAT =filename[:-4]
TEMP = open(filename,"wb")
TEMP.write(text)
TEMP.close()
print(filename)

import requests as req
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
resp = req.get(URL)
text = resp.content
#create a date oriented filename and print it
filename="csv/"+URL.split("/")[-1]
TEMP = open(filename,"wb")
TEMP.write(text)
TEMP.close()
print(filename)

from datetime import datetime
from datetime import date, timedelta
def GETYGMT():
    yesterday = datetime.utcnow() - timedelta(days=1)
    YesterdaysGMT=yesterday.strftime('%m-%d-%y')
    return YesterdaysGMT

%%writefile GETGMT.py
"""
# USAGE:
# for yesterday's GMT 
from GETGMT import *
print(GETYGMT())
>>> 05-14-2020
#todays GMT 
from GETGMT import *
print(GETGMT())
>>> 05-15-2020
"""
from datetime import datetime
from datetime import date, timedelta
def GETYGMT():
    """
    # USAGE:
    # Yesterdays GMT 
    from GETGMT import *
    print(GETYGMT())
    >>> 05-14-2020
    """
    yesterday = datetime.utcnow() - timedelta(days=1)
    YesterdaysGMT=yesterday.strftime('%m-%d-%Y')
    return YesterdaysGMT
def GETGMT():
    """
    # USEAGE:
    #Todays GMT 
    from GETGMT import *
    print(GETGMT())
    >>> 05-15-2020
    """
    GMT=datetime.utcnow().strftime('%m-%d-%Y')
    return GMT

from GETGMT import *
print(GETGMT())
print(GETYGMT())
help(GETGMT)

import requests as req
import time
from datetime import date, timedelta
yesterday = datetime.utcnow() - timedelta(days=2)
YesterdaysGMT=yesterday.strftime('%m-%d-%Y')

URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+YesterdaysGMT+".csv"

resp = req.get(URL)
content = resp.text

#create a date oriented filename and print it
filename="csv/"+URL[-14:]
print(filename)
#content=content.lstrip(",")
content=content.replace(",,,","null,")
content=content.replace(",,","null,")
content=content.replace("(","")
content=content.replace(")","")
content=content.replace("\"","")
#print(content)
# Open a file using the new filename and write the content of the 'gitfile' to it.
# Update one time daily
TEMP = open(filename,"w")
TEMP.write(content)
TEMP.close()

# List the files in the csv directory
!ls -rant csv

import requests as req
URL="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
resp = req.get(URL)
OWID = []
text = resp.content
data=text.splitlines()
cnt=0
for line in data:
    cnt=cnt+1
    if cnt<5:
        # remove the b' before the line
        line = line.decode('utf-8') 
        OWID.append([line])

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

print(CSSEGIS[4])

cnt= 0
for i in range(0, len(CSSEGIS)):
    cnt=cnt+1
    if cnt<5:
        print(CSSEGIS[i])
    

import requests as req
import time
from datetime import date, timedelta
yesterday = datetime.utcnow() - timedelta(days=2)
YesterdaysGMT=yesterday.strftime('%m-%d-%Y')
DailyReports =[]
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+YesterdaysGMT+".csv"

resp = req.get(URL)
content = resp.text
#clean the data
content = content.splitlines()
for Lines in content:
    Lines=Lines.replace(",,,","null,")
    Lines=Lines.replace(",,","null,")
    Lines=Lines.replace("(","")
    Lines=Lines.replace(")","")
    Lines=Lines.replace("\"","")
    Lines= Lines.split(",")
    DailyReports.append(Lines)

!pwd

import os
import shutil 
import os.path
NOTEBOOKS = []
allbooks =[]
PATH="/home/jack/Desktop/COVID-19-Jupyter-Notebooks"
for filename in os.listdir("/home/jack/Desktop/COVID-19-Jupyter-Notebooks"):
    if filename[-6:] == ".ipynb":
        NOTEBOOKS.append(filename)
for file in NOTEBOOKS:
    FIND=open(file, "r").readlines()
    for line in FIND:
        enter =line.replace("\n","")
        enter=enter.encode("ascii","replace")
        allbooks.append([file,enter])
search = input("Search all notebooks for the term:")
cnt=0
CNT=0
for line in allbooks:
    cnt=cnt+1
    text = str(line[1].decode('ascii'))
    text =text.replace("\\n","")
    text =text.replace("\\n","")
    if search in text:
        CNT=CNT+1
        if CNT<50:
            if len(text)<200:
                print(line[0],text)

print(len(allbooks))

cnt=0
CNT=0
search = "import"
for line in allbooks:
    cnt=cnt+1
    text = str(line[1].decode('ascii'))
    text =text.replace("\\n","")
    text =text.replace("\\n","")
    if search in text:
        CNT=CNT+1
        if CNT<50:
            print(line[0],text)


for name in sorted(NOTEBOOKS):
    print(name)

len(DailyReports)

# https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/
# example:
print(DailyReports[3])

