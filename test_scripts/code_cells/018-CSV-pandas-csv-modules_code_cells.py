https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-15-2020.csv

import pandas as pd
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
df = pd.read_csv(url)   
df.to_csv('test_global.csv')
df.head()


df = pd.read_csv('test_global.csv')
# Locate the row the US is in:
df[df['Country/Region'].str.match('US')]

df.iloc[225, 4:-1]

# Total number of deaths un the USA ( index locate )
df.iloc[225, -2:-1]

# Total number of deaths un the USA
df.loc[225, '5/14/20']

import pandas as pd
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

df = pd.read_csv(data)

print(df)

print(df.loc[[225]])



import pandas as pd
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
#data = StringIO(req.text)
data = req.text
COUNTRIES = []
cnt=0
#if data[0] =","
#print(data)
#ndata = str(data).replace(",,","null")
ndata = data.splitlines()
for line in ndata:
    if cnt ==0:print(line,"\n----\n")
    cnt=cnt+1    
    if len(line)>5 and cnt>1:
        line= line.replace('"','')
        line = line.replace(",,",",NaN,")
        nline= line.split(",")
        if nline[0]=="":
            nline.pop(0)
            nline.insert(0,'NaN')
        dist = nline[0]
        country = nline[1]
        long=float(nline[3])
        lat=float(nline[2])
        ndata = nline[4:]
        intdata = list(map(int,ndata))
        '''
        try:
            intdata = list(map(int,nline[4:]))
        except Exception as ex:
            print(ex)
            print ("Error: %s.\n" % str(ex))
            print(cnt,nline[1])
            pass
        '''    
        #print(nline[0],nline[1],nline[2],nline[3],intdata)
        #print("cnt,space,dist,country,long,lat,intdata")
        print(dist,country,long,lat,intdata)
        COUNTRIES.append([dist,country,long,lat,intdata])

AllCountryList = []

cnt=0
for line in COUNTRIES:
    cnt=cnt+1
print("Total Countries Listed:",cnt)
cnt=0
AllCountryList = []
for line in COUNTRIES:
    cnt=cnt+1
    print (line,"\n")
    AllCountryList.append([line])
    

i = 143
for line in AllCountryList:
    print(line)

print(len(AllCountryList))





