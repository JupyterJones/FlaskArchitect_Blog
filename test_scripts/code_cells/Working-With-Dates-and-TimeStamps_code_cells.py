import M2D
help(M2D)

%%writefile M2D.py
"""Month2Num(month)
span(timestamp1, timestamp2): This will show the span in hours between two timestamps.
Date = "April 09 2020 10:00:00"
DateEpoch(Date)"""
from __future__ import division
import time
def Month2Num(month):
    number=""
    months=["January","February","March","April","May","June","July",\
            "August","September","October","November","December"]
    Numbers=["01","02","03","04","05","06","07","08","09","10","11","12"]
    if month==months[0]:number=Numbers[0]
    if month==months[1]:number=Numbers[1]
    if month==months[2]:number=Numbers[2]
    if month==months[3]:number=Numbers[3]
    if month==months[4]:number=Numbers[4]
    if month==months[5]:number=Numbers[5]
    if month==months[6]:number=Numbers[6]
    if month==months[7]:number=Numbers[7]
    if month==months[8]:number=Numbers[8]
    if month==months[9]:number=Numbers[9]
    if month==months[10]:number=Numbers[10]
    if month==months[11]:number=Numbers[11]    
    return number

def span(timestamp1, timestamp2):
    SPAN = timestamp2-timestamp1
    res =SPAN/3600
    result = round(res,2)
    return result

def DateEpoch(Date):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    timestamp = int(time.mktime(time.strptime(date_ti, pattern)))
    return timestamp

def Date2Epoch(Date,last=1583621400):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    print(DATE[0],DATE[1],DATE[2],DATE[3])
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #Recognized pattern
    #16/03/2020 02:48:20
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(date_ti, pattern)))
    #print ("dt_ti, epochs",dt_ti, epochs)
    Epoch = (date_ti, epochs,span(int(last),int(epochs)))
    #EPOCHS.append(int(epochs))
    return Epoch

from M2D import *
Date = "January 01 1970 08:00:00"
print(Date2Epoch(Date,last=1))
print("----------- One day later (24 hours) ------------")
Date = "January 02 1970 08:00:00"
print(Date2Epoch(Date,last=0))
print("24 hours is a '86400' value as a timestamp and 24.0 hours have passed.")

from M2D import Date2Epoch
Date = "April 09 2020 10:00:00"
Date2Epoch(Date,last=1586390400)

from M2D import Date2Epoch
Date = "April 09 2020 10:00:00"
print(Date2Epoch(Date,last=1586390400))
print("\nNotice the result has three elements.")
print("A, B, C = Date2Epoch(Date,last=1586390400)")
A, B, C = Date2Epoch(Date,last=1586390400)
print("I can then use them independently.\n")
print("A: ",A)
print("B: ",B)
print("C: ",C)
print("The variables A B C may use any names.")
print("Example: LastD, LastT, Lastspan = Date2Epoch(Date,last=1586390400)")
LastD, LastT, Lastspan = Date2Epoch(Date,last=1586390400)
print("LastD: ",LastD)
print("LastT: ",LastT)
print("Lastspan: ",Lastspan)
print("---------------------------------")
last=1586397600
Date = "April 10 2020 10:30:00"
D,T,span = Date2Epoch(Date,last)
print(" The time passed hours has a",T-LastT,"value as a timestamp and",span,"hours have passed \
\n since",LastD,"and today,", D)
print("---------------------------------")
print(D)
print(T)
print(span)
print(span/8600)

%%writefile DTE.py
from M2D import *
import time
def Date2Epoch(Date,last=1583621400):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    print(DATE[0],DATE[1],DATE[2],DATE[3])
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(date_ti, pattern)))
    Epoch = (date_ti, epochs,span(int(last),int(epochs)))
    return Epoch


from DTE import Date2Epoch
Date = "January 01 1970 08:00:00"
Date2Epoch(Date,last=1)

from M2D import *
month = "June"
print (month+" is month ",Month2Num(month))
timestamp1 = 1586390400
timestamp2 = 1586397600
print("The span between",timestamp1,"and",timestamp2,"is",span(timestamp1, timestamp2),"hours.")
Date = "April 09 2020 10:00:00"
print("The date/time of",Date+", is the same as timestamp",DateEpoch(Date),".")

def DateEpoch(Date):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #03-16-2020 02:48,3777
    pattern = '%d/%m/%Y %H:%M:%S'
    timestamp = int(time.mktime(time.strptime(date_ti, pattern)))
    return timestamp
Date = "April 09 2020 10:00:00"
DateEpoch(Date)

from M2D import *
month = "June"
Month2Num(month)

#%%writefile DTE.py
from M2D import *
import time
def Date2Epoch(Date,last=1583621400):
    dt = time.strftime(Date)
    Date= Date.replace(",",'')
    DATE = Date.split(" ")
    print(DATE[0],DATE[1],DATE[2],DATE[3])
    date_ti = DATE[1]+"/"+Month2Num(DATE[0])+"/"+DATE[2]+" "+DATE[3]#[:-3]
    #Recognized pattern
    #16/03/2020 02:48:20
    pattern = '%d/%m/%Y %H:%M:%S'
    #pattern = '%m/%d/%Y %H:%M:%S'
    epochs = int(time.mktime(time.strptime(date_ti, pattern)))
    #print ("dt_ti, epochs",dt_ti, epochs)
    Epoch = (date_ti, epochs,span(int(last),int(epochs)))
    #EPOCHS.append(int(epochs))
    return Epoch

