import plotly.graph_objects as go
import time
from PIL import Image

LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


STAT =LASTFILE[57:-4]
DataIn = open(LASTFILE).readlines()

#SEARCH = input("SEARCH: ")
#SEARCH = "Brazil"
#SEARCH = "Spain"
#SEARCH = "Philippine"
SEARCH = "Ecuador"
#SEARCH = "Germany"
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
        print(line)
        print(line[31:-1])
        entry = line[31:-1]
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



