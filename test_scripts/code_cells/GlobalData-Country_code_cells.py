allcountries = []

%%writefile GlobalData.py
'''
Usage:
from GlobalData import *
print(HELP)

To get Zambia Population-2019 
from GlobalData import *
X=GlobalData("Zambia")
x=X.split(",")
print(x[4])

To get Zambia Population Change
from GlobalData import *
X=GlobalData("Zambia")
x=X.split(",")
print(x[5])

from GlobalData import *
print(DATA[4])
>>> ['American Samoa,Oceania,Polynesia,55465,55312,−0.28%']

from GlobalData import *
data=str(DATA[4]).split(",")
print(data[3])
>>> 55465
'''
DATA='''Country,UN Continental,Unstatistical,Population-2018,Population-2019,Population Change
Afghanistan,Asia,Southern Asia,37171921,38041754,+2.34%
Albania,Europe,Southern Europe,2882740,2880917,−0.06%
Algeria,Africa,Northern Africa,42228408,43053054,+1.95%
American Samoa,Oceania,Polynesia,55465,55312,−0.28%
Andorra,Europe,Southern Europe,77006,77142,+0.18%
Angola,Africa,Middle Africa,30809787,31825295,+3.30%
Anguilla,Americas,Caribbean,14731,14869,+0.94%
Antigua and Barbuda,Americas,Caribbean,96286,97118,+0.86%
Argentina,Americas,South America,44361150,44780677,+0.95%
Armenia,Asia,Western Asia,2951745,2957731,+0.20%
Aruba,Americas,Caribbean,105845,106314,+0.44%
Australia,Oceania,Australia and New Zealand,24898152,25203198,+1.23%
Austria,Europe,Western Europe,8891388,8955102,+0.72%
Azerbaijan,Asia,Western Asia,9949537,10047718,+0.99%
Bahamas,Americas,Caribbean,385637,389482,+1.00%
Bahrain,Asia,Western Asia,1569446,1641172,+4.57%
Bangladesh,Asia,Southern Asia,161376708,163046161,+1.03%
Barbados,Americas,Caribbean,286641,287025,+0.13%
Belarus,Europe,Eastern Europe,9452617,9452411,0.00%
Belgium,Europe,Western Europe,11482178,11539328,+0.50%
Belize,Americas,Central America,383071,390353,+1.90%
Benin,Africa,Western Africa,11485044,11801151,+2.75%
Bermuda,Americas,Northern America,62756,62506,−0.40%
Bhutan,Asia,Southern Asia,754388,763092,+1.15%
Bolivia,Americas,South America,11353142,11513100,+1.41%
Bosnia and Herzegovina,Europe,Southern Europe,3323925,3301000,−0.69%
Botswana,Africa,Southern Africa,2254068,2303697,+2.20%
Brazil,Americas,South America,209469323,211049527,+0.75%
British Virgin Islands,Americas,Caribbean,29802,30030,+0.77%
Brunei,Asia,South-eastern Asia,428963,433285,+1.01%
Bulgaria,Europe,Eastern Europe,7051608,7000119,−0.73%
Burkina Faso,Africa,Western Africa,19751466,20321378,+2.89%
Burundi,Africa,Eastern Africa,10524117,10864245,+3.23%
Cambodia,Asia,South-eastern Asia,16249792,16486542,+1.46%
Cameroon,Africa,Middle Africa,25216267,25876380,+2.62%
Canada,Americas,Northern America,37074562,37411047,+0.91%
Cape Verde,Africa,Western Africa,543767,549935,+1.13%
Caribbean Netherlandst,Americas,Caribbean,25711,25979,+1.04%
Cayman Islands,Americas,Caribbean,64174,64948,+1.21%
Central African Republic,Africa,Middle Africa,4666368,4745185,+1.69%
Chad,Africa,Middle Africa,15477729,15946876,+3.03%
Chile,Americas,South America,18729160,18952038,+1.19%
Chinaa,Asia,Eastern Asia,1427647786,1433783686,+0.43%
Colombia,Americas,South America,49661048,50339443,+1.37%
Comoros,Africa,Eastern Africa,832322,850886,+2.23%
Congo,Africa,Middle Africa,5244359,5380508,+2.60%
Cook Islands,Oceania,Polynesia,17518,17548,+0.17%
Costa Rica,Americas,Central America,4999441,5047561,+0.96%
Croatia,Europe,Southern Europe,4156405,4130304,−0.63%
Cuba,Americas,Caribbean,11338134,11333483,−0.04%
Curaçao,Americas,Caribbean,162752,163424,+0.41%
Cyprus,Asia,Western Asia,1170125,1179551,+0.81%
Czech Republic,Europe,Eastern Europe,10665677,10689209,+0.22%
Denmark,Europe,Northern Europe,5752126,5771876,+0.34%
Djibouti,Africa,Eastern Africa,958923,973560,+1.53%
Dominica,Americas,Caribbean,71625,71808,+0.26%
Dominican Republic,Americas,Caribbean,10627141,10738958,+1.05%
DR Congo,Africa,Middle Africa,84068091,86790567,+3.24%
East Timor,Asia,South-eastern Asia,1267974,1293119,+1.98%
Ecuador,Americas,South America,17084358,17373662,+1.69%
Egypt,Africa,Northern Africa,98423598,100388073,+2.00%
El Salvador,Americas,Central America,6420746,6453553,+0.51%
Equatorial Guinea,Africa,Middle Africa,1308975,1355986,+3.59%
Eritrea,Africa,Eastern Africa,3452786,3497117,+1.28%
Estonia,Europe,Northern Europe,1322920,1325648,+0.21%
Eswatini,Africa,Southern Africa,1136281,1148130,+1.04%
Ethiopia,Africa,Eastern Africa,109224414,112078730,+2.61%
F.S. Micronesia,Oceania,Micronesia,112640,113815,+1.04%
Falkland Islands,Americas,South America,3234,3377,+4.42%
Faroe Islands,Europe,Northern Europe,48497,48678,+0.37%
Fiji,Oceania,Melanesia,883483,889953,+0.73%
Finland,Europe,Northern Europe,5522576,5532156,+0.17%
France,Europe,Western Europe,64990511,65129728,+0.21%
French Guiana,Americas,South America,275713,282731,+2.55%
French Polynesia,Oceania,Polynesia,277679,279287,+0.58%
Gabon,Africa,Middle Africa,2119275,2172579,+2.52%
Gambia,Africa,Western Africa,2280094,2347706,+2.97%
Georgia,Asia,Western Asia,4002942,3996765,−0.15%
Germany,Europe,Western Europe,83124418,83517045,+0.47%
Ghana,Africa,Western Africa,28206728,28833629,+2.22%
Gibraltar,Europe,Southern Europe,33718,33701,−0.05%
United Kingdom,Europe,Northern Europe,67141684,67530172,+0.58%
Greece,Europe,Southern Europe,10522246,10473455,−0.46%
Greenland,Americas,Northern America,56564,56672,+0.19%
Grenada,Americas,Caribbean,111454,112003,+0.49%
Guadeloupes,Americas,Caribbean,446928,447905,+0.22%
Guam,Oceania,Micronesia,165768,167294,+0.92%
Guatemala,Americas,Central America,17247849,17581472,+1.93%
Guernsey and  Jersey,Europe,Northern Europe,170499,172259,+1.03%
Guinea,Africa,Western Africa,12414293,12771246,+2.88%
Guinea-Bissau,Africa,Western Africa,1874303,1920922,+2.49%
Guyana,Americas,South America,779006,782766,+0.48%
Haiti,Americas,Caribbean,11123178,11263770,+1.26%
Honduras,Americas,Central America,9587522,9746117,+1.65%
Hong Kong,Asia,Eastern Asia,7371730,7436154,+0.87%
Hungary,Europe,Eastern Europe,9707499,9684679,−0.24%
Iceland,Europe,Northern Europe,336713,339031,+0.69%
India,Asia,Southern Asia,1352642280,1366417754,+1.02%
Indonesia,Asia,South-eastern Asia,267670543,270625568,+1.10%
Iran,Asia,Southern Asia,81800188,82913906,+1.36%
Iraq,Asia,Western Asia,38433600,39309783,+2.28%
Ireland,Europe,Northern Europe,4818690,4882495,+1.32%
Isle of Man,Europe,Northern Europe,84077,84584,+0.60%
Israel,Asia,Western Asia,8381516,8519377,+1.64%
Italy,Europe,Southern Europe,60627291,60550075,−0.13%
Ivory Coast,Africa,Western Africa,25069230,25716544,+2.58%
Jamaica,Americas,Caribbean,2934847,2948279,+0.46%
Japan,Asia,Eastern Asia,127202192,126860301,−0.27%
Jordan,Asia,Western Asia,9965318,10101694,+1.37%
Kazakhstan,Asia,Central Asia,18319618,18551427,+1.27%
Kenya,Africa,Eastern Africa,51392565,52573973,+2.30%
Kiribati,Oceania,Micronesia,115847,117606,+1.52%
Kuwait,Asia,Western Asia,4137312,4207083,+1.69%
Kyrgyzstan,Asia,Central Asia,6304030,6415850,+1.77%
Laos,Asia,South-eastern Asia,7061507,7169455,+1.53%
Latvia,Europe,Northern Europe,1928459,1906743,−1.13%
Lebanon,Asia,Western Asia,6859408,6855713,−0.05%
Lesotho,Africa,Southern Africa,2108328,2125268,+0.80%
Liberia,Africa,Western Africa,4818973,4937374,+2.46%
Libya,Africa,Northern Africa,6678559,6777452,+1.48%
Liechtenstein,Europe,Western Europe,37910,38019,+0.29%
Lithuania,Europe,Northern Europe,2801264,2759627,−1.49%
Luxembourg,Europe,Western Europe,604245,615729,+1.90%
Macau,Asia,Eastern Asia,631636,640445,+1.39%
Madagascar,Africa,Eastern Africa,26262313,26969307,+2.69%
Malawi,Africa,Eastern Africa,18143217,18628747,+2.68%
Malaysia,Asia,South-eastern Asia,31528033,31949777,+1.34%
Maldives,Asia,Southern Asia,515696,530953,+2.96%
Mali,Africa,Western Africa,19077749,19658031,+3.04%
Malta,Europe,Southern Europe,439248,440372,+0.26%
Marshall Islands,Oceania,Micronesia,58413,58791,+0.65%
Martinique,Americas,Caribbean,375673,375554,−0.03%
Mauritania,Africa,Western Africa,4403313,4525696,+2.78%
Mauritius,Africa,Eastern Africa,1189265,1198575,+0.78%
Mayotte,Africa,Eastern Africa,259531,266150,+2.55%
Mexico,Americas,Central America,126190788,127575529,+1.10%
Moldova,Europe,Eastern Europe,4051944,4043263,−0.21%
Monaco,Europe,Western Europe,38682,38964,+0.73%
Mongolia,Asia,Eastern Asia,3170216,3225167,+1.73%
Montenegro,Europe,Southern Europe,627809,627987,+0.03%
Montserrat,Americas,Caribbean,4993,4989,−0.08%
Morocco,Africa,Northern Africa,36029093,36471769,+1.23%
Mozambique,Africa,Eastern Africa,29496004,30366036,+2.95%
Myanmar,Asia,South-eastern Asia,53708320,54045420,+0.63%
Namibia,Africa,Southern Africa,2448301,2494530,+1.89%
Nauru,Oceania,Micronesia,10670,10756,+0.81%
Nepal,Asia,Southern Asia,28095714,28608710,+1.83%
Netherlands,Europe,Western Europe,17059560,17097130,+0.22%
New Caledonia,Oceania,Melanesia,279993,282750,+0.98%
New Zealand,Oceania,Australia and New Zealand,4743131,4783063,+0.84%
Nicaragua,Americas,Central America,6465501,6545502,+1.24%
Niger,Africa,Western Africa,22442822,23310715,+3.87%
Nigeria,Africa,Western Africa,195874683,200963599,+2.60%
Niue,Oceania,Polynesia,1620,1615,−0.31%
North Korea,Asia,Eastern Asia,25549604,25666161,+0.46%
North Macedonia,Europe,Southern Europe,2082957,2083459,+0.02%
Northern Mariana Islands,Oceania,Micronesia,56882,56188,−1.22%
Norway,Europe,Northern Europe,5337962,5378857,+0.77%
Oman,Asia,Western Asia,4829473,4974986,+3.01%
Pakistan,Asia,Southern Asia,212228286,216565318,+2.04%
Palau,Oceania,Micronesia,17907,18008,+0.56%
Palestinen,Asia,Western Asia,4862979,4981420,+2.44%
Panama,Americas,Central America,4176869,4246439,+1.67%
Papua New Guinea,Oceania,Melanesia,8606323,8776109,+1.97%
Paraguay,Americas,South America,6956066,7044636,+1.27%
Peru,Americas,South America,31989260,32510453,+1.63%
Philippines,Asia,South-eastern Asia,106651394,108116615,+1.37%
Poland,Europe,Eastern Europe,37921592,37887768,−0.09%
Portugal,Europe,Southern Europe,10256193,10226187,−0.29%
Puerto Rico,Americas,Caribbean,3039596,2933408,−3.49%
Qatar,Asia,Western Asia,2781682,2832067,+1.81%
Réunion,Africa,Eastern Africa,882526,888927,+0.73%
Romania,Europe,Eastern Europe,19506114,19364557,−0.73%
Russia,Europe,Eastern Europe,145734038,145872256,+0.09%
Rwanda,Africa,Eastern Africa,12301970,12626950,+2.64%
Saint Helena Ascension and Tristan da Cunha,Africa,Western Africa,6035,6059,+0.40%
Saint Kitts and Nevis,Americas,Caribbean,52441,52823,+0.73%
Saint Lucia,Americas,Caribbean,181889,182790,+0.50%
Saint Pierre and Miquelon,Americas,Northern America,5849,5822,−0.46%
Saint Vincent and the Grenadines,Americas,Caribbean,110211,110589,+0.34%
Samoa,Oceania,Polynesia,196129,197097,+0.49%
San Marino,Europe,Southern Europe,33785,33860,+0.22%
São Tomé and Príncipe,Africa,Middle Africa,211028,215056,+1.91%
Saudi Arabia,Asia,Western Asia,33702756,34268528,+1.68%
Senegal,Africa,Western Africa,15854323,16296364,+2.79%
Serbiak,Europe,Southern Europe,8802754,8772235,−0.35%
Seychelles,Africa,Eastern Africa,97096,97739,+0.66%
Sierra Leone,Africa,Western Africa,7650150,7813215,+2.13%
Singapore,Asia,South-eastern Asia,5757499,5804337,+0.81%
Sint Maarten,Americas,Caribbean,41940,42388,+1.07%
Slovakia,Europe,Eastern Europe,5453014,5457013,+0.07%
Slovenia,Europe,Southern Europe,2077837,2078654,+0.04%
Solomon Islands,Oceania,Melanesia,652857,669823,+2.60%
Somalia,Africa,Eastern Africa,15008226,15442905,+2.90%
South Africa,Africa,Southern Africa,57792518,58558270,+1.33%
South Korea,Asia,Eastern Asia,51171706,51225308,+0.10%
South Sudan,Africa,Eastern Africa,10975927,11062113,+0.79%
Spain,Europe,Southern Europe,46692858,46736776,+0.09%
Sri Lanka,Asia,Southern Asia,21228763,21323733,+0.45%
Sudan,Africa,Northern Africa,41801533,42813238,+2.42%
Suriname,Americas,South America,575990,581372,+0.93%
Sweden,Europe,Northern Europe,9971638,10036379,+0.65%
Switzerland,Europe,Western Europe,8525611,8591365,+0.77%
Syria,Asia,Western Asia,16945057,17070135,+0.74%
Taiwan,Asia,Eastern Asia,23726460,23773876,+0.20%
Tajikistan,Asia,Central Asia,9100835,9321018,+2.42%
Tanzaniac,Africa,Eastern Africa,56313438,58005463,+3.00%
Thailand,Asia,South-eastern Asia,68863514,69037513,+0.25%
Togo,Africa,Western Africa,7889093,8082366,+2.45%
Tokelau,Oceania,Polynesia,1319,1340,+1.59%
Tonga,Oceania,Polynesia,110589,110940,+0.32%
Trinidad and Tobago,Americas,Caribbean,1389843,1394973,+0.37%
Tunisia,Africa,Northern Africa,11565201,11694719,+1.12%
Turkey,Asia,Western Asia,82340088,83429615,+1.32%
Turkmenistan,Asia,Central Asia,5850901,5942089,+1.56%
Turks and Caicos Islands,Americas,Caribbean,37665,38191,+1.40%
Tuvalu,Oceania,Polynesia,11508,11646,+1.20%
U.S. Virgin Islands,Americas,Caribbean,104680,104578,−0.10%
Uganda,Africa,Eastern Africa,42729036,44269594,+3.61%
Ukraine,Europe,Eastern Europe,44246156,43993638,−0.57%
United Arab Emirates,Asia,Western Asia,9630959,9770529,+1.45%
United States,Americas,Northern America,327096265,329064917,+0.60%
US,Americas,Northern America,327096265,329064917,+0.60%
Uruguay,Americas,South America,3449285,3461734,+0.36%
Uzbekistan,Asia,Central Asia,32476244,32981716,+1.56%
Vanuatu,Oceania,Melanesia,292680,299882,+2.46%
Vatican City,Europe,Southern Europe,801,799,−0.25%
Venezuela,Americas,South America,28887118,28515829,−1.29%
Vietnam,Asia,South-eastern Asia,95545962,96462106,+0.96%
Wallis and Futuna,Oceania,Polynesia,11661,11432,−1.96%
Western Sahara,Africa,Northern Africa,567402,582463,+2.65%
Yemen,Asia,Western Asia,28498683,29161922,+2.33%
Zambia,Africa,Eastern Africa,17351708,17861030,+2.94%
Zimbabwe,Africa,Eastern Africa,14438802,14645468,+1.43%'''

HELP="""help,Usage:
from GlobalData import *
print(HELP)

To get Zambia Population-2019
from GlobalData import *
X=GlobalData("Zambia")
print(x[4])
\n
To get Zambia Population Change
from GlobalData import *
X=GlobalData("Zambia")
print(x[5])
\n
from GlobalData import *
print(DATA[4])
>>> [\'American Samoa,Oceania,Polynesia,55465,55312,−0.28%\']
\n
from GlobalData import *
data=str(DATA[4]).split(",")
print(data[3])
>>> 55465']]"""
Data=[]
DATA = DATA.replace("%","")
DATA = DATA.split("\n") 
cnt=0
for line in DATA:
    cnt=cnt+1
    line = line.split(",")
    if cnt>1:Data.append([line[0],line[1],line[2],int(line[3]),int(line[4]),round(float(line[5][1:])/100, 4)])
def GlobalData(country):
    if country=="HELP":
        print(HELP)
    for i in range(0,len(Data)):
        if country == Data[i][0]:
            res=Data[i]
            return res

from GlobalData import *
print(HELP)

from GlobalData import *
data=DATA[6]
print(data)

from GlobalData import *
print(DATA[4])

from GlobalData import *
X=GlobalData("Angola")
print(X[5])

for line in DATA:
    if "Spain" in line:
        print(line)

help(DATA)

from GlobalData import *
SEARCH="Angola"
X=GlobalData(SEARCH)
print(X)

from GlobalData import *
SEARCH="Germany"
X=GlobalData(SEARCH)
population=X[4]
print(SEARCH,"Population:", population)

from GlobalData import *
X=GlobalData("Angola")
print(X[5])



import plotly.graph_objects as go
import time
from PIL import Image
from GlobalData import *


LASTFILE="COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


STAT =LASTFILE[57:-4]
DataIn = open(LASTFILE).readlines()

#SEARCH = input("SEARCH: ")
SEARCH = "Brazil"
#SEARCH = "Spain"
#SEARCH = "Philippine"
#SEARCH = "Ecuador"
#SEARCH = "Germany"
#SEARCH = "Japan"
#SEARCH = "US"
X=GlobalData(SEARCH)
x=X
population=x[4]
print(SEARCH,"Population:", population)
cnt = 0
CNTS=0
counts=[]
for line in DataIn:
    if cnt==0:print(line)
    cnt=cnt+1
    line=line.lstrip(",")
    #if SEARCH in line:print(line)
    if SEARCH in line:

        line="0,0"+line.split("0,0",1)[-1]

        print
        entry=line.split(",")
        for num in entry:
            counts.append(int(num))
print(SEARCH," counts/population",int(counts[-1])/int(population)) 
allcountries.append([SEARCH," counts/population",int(counts[-1])/int(population)])
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

from GlobalData import *
data=str(DATA[4]).split(",")
print(data[3])



from GlobalData import *
X=GlobalData("Zambia")
x=X
print(x[4])

from GlobalData import *
GlobalData("Turkey")

from GlobalData import *
print(HELP)
