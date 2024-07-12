import requests as req
URL="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
response = req.get(URL)
content = response.content

content=str(content)
DataIn = content.splitlines()

print DataIn[0]

cnt=0
ALLdata = []
for line in DataIn[1:]:
    cnt=cnt+1
    #print cnt,line
    line= line.replace(",,",",nan,")
    line= line.split(",")
    ALLdata.append(line)

print ALLdata[200][1]

history = []
for i in range(0,len(ALLdata)):
    #if "USA" == ALLdata[i][0]:
    if "United States" == ALLdata[i][1]:   
        history.append(ALLdata[i][3:7])
print len(history)        

print history[0:]

Summary.reverse()

for line in Summary:
    print line



cnt=0
filename = "36B9q1Ws.csv"
with open(filename) as f:
    lines = f.read().splitlines()
    for line in lines:
        cnt=cnt+1
        if cnt==1:print line
        if cnt==1:print "-----------------------------"
Summary=[]
cnt=0
Cases = []
Deaths = []
Population = []
with open(filename) as f:
    lines = f.read().splitlines()    
    for line in lines:
        item = line.split(",")
        if "United_States_of_America" == item[6]:
            Cases.append(int(item[4]))
            Deaths.append(int(item[5]))
            Population.append(int(item[9]))
            Summary.append([int(item[4]),int(item[5]),int(item[9]),str(item[0])])            

