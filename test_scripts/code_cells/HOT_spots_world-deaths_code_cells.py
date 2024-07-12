import requests as req
import time
DATE = time.strftime("%m-%d-%H_")
URL ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

resp = req.get(URL)
content = resp.text

#create a date oriented filename and print it
filename=str(DATE)+"_"+URL[-17:]
print(filename)
content=content.replace(",,",",Ex,")
content=content.replace("(","")
content=content.replace(")","")
content=content.replace("\"","")

print(content)
# Open a file using the new filename and write the content of the 'gitfile' to it.
# Update one time daily
TEMP = open(filename,"w")
TEMP.write(content)
TEMP.close() 


LASTFILE=filename

import requests as req
import time
DATA=[]
#LASTFILE="05-01-20__deaths_global.csv"
DataIn = open(LASTFILE).read()
ALLcountries=[]
DataIn = DataIn.split("\n")
Datain = DataIn[7:]
for line in Datain:
    lines = line.lstrip(",")
    lines=lines.split(",")
    ALLcountries.append(lines)
    data="0,0,"+str(line).split("0,0,",1)[-1]
    DATA.append(data)    

# Set N for threshhold
cnt=0
E=len(ALLcountries)
for lines in ALLcountries:
    cnt=cnt+1
    if cnt>=E:break
    linez=str(lines)
    linez=linez.replace("[","")
    linez=linez.replace("]","")
    linez=linez.replace("'","")
    lineZ=str(linez).split(",")
    if int(lineZ[-1])-int(lineZ[-2])>=150:
        print("\nID-"+str(cnt)+": In "+lineZ[0]+" there was a",int(lineZ[-2])-int(lineZ[-3]),"increase yesterday and",int(lineZ[-1])-int(lineZ[-2]),"increase today:\n",linez)

# Set N for threshhold

N=250
CNT=0
cnt=0
for line in ALLcountries:
    cnt=cnt+1
print("-------------------",cnt,len(ALLcountries),"---------------------")
cnt=0
for line in DATA:
    cnt=cnt+1
    if cnt==len(DATA):break
    lines=line.split(",")
    #print(cnt,lines[-2],lines[-1])
    #c=int(lines[-2]),int(lines[-1]),int(lines[-1])-int(lines[-2])
    if int(lines[-1])-int(lines[-2])>=N:
        CNT=CNT+1
        print("\n",CNT,"____",cnt,int(lines[-1])-int(lines[-2]))
        print(cnt,ALLcountries[cnt-1])
print(cnt)

COUNTRY="Brazil"

for lines in ALLcountries:
    linez=str(lines)
    linez=linez.replace("[","")
    linez=linez.replace("]","")
    linez=linez.replace("'","")
    lineZ=str(linez).split(",") 
    if COUNTRY==(lineZ[0]):print(linez)

cnt=0
for line in ALLcountries:
    cnt=cnt+1
print(cnt)
print(len(ALLcountries))
print("----------------------------------------")
cnt=0
for line in DATA:
    cnt=cnt+1
    lines=line.split(",")
    c=int(lines[-2]),int(lines[-1]),int(lines[-1])-int(lines[-2])
    if int(lines[-1])-int(lines[-2])>500:
        print("\n____",cnt,int(lines[-1])-int(lines[-2]))
        print(cnt,ALLcountries[cnt-1])
print(cnt)

LASTFILE="05-01-13__id19_confirmed_US.csv"
DataIn = open(LASTFILE).read()
ALLCASES=[]
DataIn = DataIn.split("\n")
Datain = DataIn[7:]
for line in Datain:
    if len(line)>80:
        line=line.replace('"','')
        #line=line.replace(',,',',XX,')
        #line=line.replace("\n","")
        line = line.lstrip(",")
        line = line.split(",")
        ALLCASES.append(line)

LASTFILE="05-01-13__id19_confirmed_US.csv"
DataIn = open(LASTFILE).read()
ALLCASES=[]
DataIn = DataIn.split("\n")
Datain = DataIn[7:]
for line in Datain:
    if len(line)>80:
        linez = line.split("US,",2)[-1]
        linez=linez.replace(",",", ")
        linez=linez.split(" ")
        if len(linez)!=100:
            linez = linez[:-1]
            ALLCASES.append(linez)
        if len(linez)==100:    
            ALLCASES.append(linez)


694: 77 : ['0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '1,', '2,', '3,', '9,', '9,', '12,', '21,', '24,', '28,', '40,', '40,', '104,', '127,', '182,', '223,', '228,', '322,', '384,', '455,', '582,', '648,', '697,', '']
695: 24 : ['840,', '914,', '1010,', '1077,', '1126,', '1228,', '1283,', '1350,', '1433,', '1494,', '1566,', '1603,', '1643,', '1692,', '1736,', '1820,', '1885,', '2009,', '2060,', '2126,', '2173,', '2254,', '2369,', '2492']
2357: 97 : ['0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '1,', '4,', '8,', '22,', '27,', '29,', '43,', '45,', '59,', '59,', '65,', '81,', '95,', '135,', '148,', '176,', '200,', '224,', '242,', '298,', '311,', '340,', '340,', '417,', '452,', '479,', '494,', '494,', '535,', '548,', '579,', '612,', '626,', '652,', '657,', '657,', '725,', '736,', '766,', '787,', '837,', '']

cnt=0
for line in ALLCASES[1:]:
    cnt=cnt+1
    if cnt<5:print(line)


TOTAL=0
DATA = []
L=len(ALLCASES)
ALL = ALLCASES[6:]
print(len(ALL))

TOTAL=0
DATA = []
L=len(ALLCASES)
ALL = ALLCASES[1:]
DAILY=[]
cnt=0
for i in range(0,len(ALL)):
    if str(ALL[i]).count(",") !=109:
        print("XX",i,"XX",str(ALL[i]).count(","),ALL[i][-97:])
        print(len(ALL[i][-96:]),end=" ")

TOTAL=0
DATA = []
L=len(ALLCASES)
ALL = ALLCASES[1:]
DAILY=[]
cnt=0
for i in range(0,len(ALL)):
    print(ALL[i].count(","))
    L=int(len(ALL[i]))
    cnt=cnt+1
    if cnt==1:print(ALL[i][5],ALL[i][6],ALL[i][8],ALL[i][9],int(ALL[i][-2]),int(ALL[i][-1]))
    if len(ALL[i])>5:Daily = "'0', '0',"+str(ALL[i]).split("', '0', '0',",1)[-1]
    Daily=Daily.replace('\'','')
    Daily=Daily.replace(']','')
    Daily=Daily.replace('[','')
    Daily=Daily.replace(' ','')
    Daily=Daily.replace('"','')
    Dail=Daily.replace(',,',',X,')
    
    print(Dail)
    #print(Daily)
    daily = map(int,Dail.split(","))
    
    daily =(list(daily))
    DAILY.append(daily)
    inc= daily[-1]-daily[-2]
    #print(ALL[i])
    print("XXXXXX",i,ALL[i][3],ALL[i][4],ALL[i][5],ALL[i][6],ALL[i][9],ALL[i][10],daily,daily[-2],daily[-1],inc)
    #TOTAL=TOTAL+daily[-1]
    DATA.append([ALL[i][5],ALL[i][6],ALL[i][9],ALL[i][10],daily,daily[-2],daily[-1],inc])
print(cnt,TOTAL)        

line ="[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 9, 15, 18, 18, 21, 21, 23, 24, 25, 26, 28, 30, 29, 30, 31, 36, 36, 41, 42, 45, 49, 53, 59, 62, 67, 76, 76, 84]"
print(line.count(","))

line="[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 5, 5, 5, 5, 5, 5, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 14, 16, 16, 17]"
print(line.count(","))

TOTAL=0
DATA = []
L=len(ALLCASES)
ALL = ALLCASES[1:]
DAILY=[]
cnt=0
for i in range(0,len(ALL)):
    print(ALL[i].count(","))
    L=int(len(ALL[i]))
    cnt=cnt+1
    if cnt==1:print(ALL[i][5],ALL[i][6],ALL[i][8],ALL[i][9],int(ALL[i][-2]),int(ALL[i][-1]))
    if len(ALL[i])>5:
        Daily = "'0', '0',"+str(ALL[i]).split("', '0', '0',",1)[-1]

TOTAL=0
DATA = []
L=len(ALLCASES)
ALL = ALLCASES[1:]
DAILY=[]
cnt=0
for i in range(0,len(ALL)):
    print(ALL[i].count(","))
    L=int(len(ALL[i]))
    cnt=cnt+1

