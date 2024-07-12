#%%writefile claim_search
#!/usr/bin/python2
import os
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completed import track_download
import sqlite3
import watchVID
database = '5279.db'
conn = sqlite3.connect(database)
# text_factory deals with the non-asci characters
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT, url TEXT, unique (url));'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
search=raw_input("SEARCH : ")
data = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"text": search,  "page_size":75}}).json()
LINES = (json.dumps(data, indent=2 * ' '))
Lin =str(LINES)
L = Lin.split("\n")
cnt = 0
for line in L:
    DES = []
    URL = []
    line= line.replace('\\n',' ')
    if "permanent_url" in line and "@" not in line:
        cnt= cnt+1
        Url = line.lstrip()
        URL.append(Url) 
        #print Url
        #print Url[25:-4]
        TEXT=Url[25:-4]+":::"
        #print TEXT
    if "description" in line:
        Des=line.lstrip()
        if len(Des)<5:Des="----------------No Description Given--"
        DES.append(Des)
        #print Des
        TEXT = str(TEXT)+(Des[16:-2])
        #print TEXT        
        #print Des[16:-2]
        TEXT = TEXT.split(":::")
        try:
            print TEXT[0]+"------"+TEXT[1]
            c.execute("INSERT INTO LBRY VALUES (?,?)", (TEXT[0],TEXT[1]))
        except:
            pass
conn.commit()
conn.close()

%%writefile watchVID.py
import subprocess
import glob
import os
def WATCH():
    # detox: remove all spaces from filenames Linux: apt install detox
    #PYTHON3 use: subprocess.run(["detox", "/home/jack/Downloads"])
    THIS_dir = os.getcwd()
    subprocess.call(["detox", THIS_dir])
    list_of_files = glob.glob(THIS_dir+"/*.mp4") # * means all if need specific format then *.csv
    src = max(list_of_files, key=os.path.getctime)
    bashCommand ="vlc --preferred-resolution 240 "+src 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate() 
    return 



#%%writefile search_data 
#!/usr/bin/python2
import sqlite3
database = '/home/jack/Desktop/LBRY-toolbox/5279.db'
conn = sqlite3.connect(database)
conn.text_factory = str
cnt = 0
Search = raw_input("SEARCH: ")
c = conn.cursor()
for row in c.execute("select * from LBRY"):
    cnt=cnt+1
    if Search in row[0] or Search in row[1]:
        print "Download Link: ",row[0]
        print row[1]
        print "-------------------------------"
print cnt    

requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"claim_ids": [], "channel": "@channel", "channel_ids": [], "not_channel_ids": [], "has_channel_signature": false, "valid_channel_signature": false, "invalid_channel_signature": false, "is_controlling": false, "stream_types": [], "media_types": [], "any_tags": [], "all_tags": [], "not_tags": [], "any_languages": [], "all_languages": [], "not_languages": [], "any_locations": [], "all_locations": [], "not_locations": [], "order_by": []}}).json()

    name    optionalstr
    claim name (normalized)
    text    optionalstr    full text search
    claim_id    optionalstr    full or partial claim id
    claim_ids    optionallist
    list of full claim ids
    txid    optionalstr
    transaction id    nout    optionalstr
    position in the transaction
    channel    optionalstr
    claims signed by this channel (argument is a URL which automatically gets resolved), see --channel_ids if you need to filter by multiple channels at the same time, includes claims with invalid signatures, use in conjunction with --valid_channel_signature
    channel_ids   optionallist  claims signed by any of these channels (arguments must be claim ids of the channels), includes claims with invalid signatures, implies --has_channel_signature, use in conjunction with --valid_channel_signature
    not_channel_ids   optionallist  exclude claims signed by any of these channels (arguments must be claim ids of the channels)
    has_channel_signature  optionalbool
    claims with a channel signature (valid or invalid)
    valid_channel_signature
    optionalbool
    claims with a valid channel signature or no signature, use in conjunction with --has_channel_signature to only get claims with valid signatures
    invalid_channel_signature
    optionalbool
    claims with invalid channel signature or no signature, use in conjunction with --has_channel_signature to only get claims with invalid signatures
    is_controlling
    optionalbool
    winning claims of their respective name
    public_key_id
    optionalstr
    only return channels having this public key id, this is the same key as used in the wallet file to map channel certificate private keys: {'public_key_id': 'private key'}
    height              optionalint    last updated block height (supports equality constraints)
    timestamp           optionalint    last updated timestamp (supports equality constraints)
    creation_height     optionalint    created at block height (supports equality constraints)
    creation_timestamp  optionalint
    created at timestamp (supports equality constraints)
    activation_height   optionalint     height at which claim starts competing for name (supports equality constraints)
    expiration_height   optionalint    height at which claim will expire (supports equality constraints)
    release_time        optionalint    limit to claims self-described as having been released to the public on or after this UTC timestamp, when claim does not provide a release time the publish time is used instead (supports equality constraints)
    amount              optionalint    limit by claim value (supports equality constraints)
    support_amount      optionalint    limit by supports and tips received (supports equality constraints)
    effective_amount    optionalint    limit by total value (initial claim value plus all tips and supports received), this amount is blank until claim has reached activation height (supports equality constraints)
    trending_group      optionalint    group numbers 1 through 4 representing the trending groups of the content: 4 means content is trending globally and independently, 3 means content is not trending globally but is trending independently (locally), 2 means it is trending globally but not independently and 1 means it's not trending globally or locally (supports equality constraints)
    trending_mixed      optionalint    trending amount taken from the global or local value depending on the trending group: 4 - global value, 3 - local value, 2 - global value, 1 - local value (supports equality constraints)
    trending_local      optionalint    trending value calculated relative only to the individual contents past history (supports equality constraints)
    trending_global     optionalint    trending value calculated relative to all trending content globally (supports equality constraints)
    reposted_claim_id   optionalstr    all reposts of the specified original claim id
    reposted            optionalint    claims reposted this many times (supports equality constraints)
    claim_type          optionalstr    filter by 'channel', 'stream' or 'unknown'
    stream_types        optionallist   filter by 'video', 'image', 'document', etc
    media_types         optionallist   filter by 'video/mp4', 'image/png', etc
    fee_currency        optionalstring specify fee currency: LBC, BTC, USD
    fee_amount          optionaldecimal    content download fee (supports equality constraints)
    any_tags            optionallist    find claims containing any of the tags
    all_tags            optionallist    find claims containing every tag
    not_tags            optionallist    find claims not containing any of these tags
    any_languages       optionallist    find claims containing any of the languages
    all_languages       optionallist    find claims containing every language
    not_languages       optionallist    find claims not containing any of these languages
    any_locations       optionallist    find claims containing any of the locations
    all_locations       optionallist    find claims containing every location
    not_locations       optionallist    find claims not containing any of these locations
    page                optionalint     page to return during paginating
    page_size           optionalint     number of items on page during pagination
    order_by            optionallist    field to order by, default is descending order, to do an ascending order prepend ^ to the field name, eg. '^amount' available fields: 'name', 'height', 'release_time', 'publish_time', 'amount', 'effective_amount', 'support_amount', 'trending_group', 'trending_mixed', 'trending_local', 'trending_global', 'activation_height'
    no_totals  optionalbool
    do not calculate the total number of pages and items in result set (significant performance boost)
    wallet_id optionalstr 

import urllib
import simplejson as json
import requests
import sys
SEARCH = raw_input("Search: ")
data = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"text": SEARCH,  "page_size":50}}).json()

print data

DATA =str(data)
Data =DATA.split("{")
for line in Data:
     print line

print json.dumps(data)

print(json.dumps(data, sort_keys=True, indent=2 * ' '))

import urllib
import simplejson as json
import requests
import sys
search =raw_input("Search Term: ")
data = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"text": search,  "page_size":25}}).json()
LINES = (json.dumps(data, indent=2 * ' '))
LIST =[]
#print LINES
Lin =str(LINES)
L = Lin.split("\n")
cnt = 0
for line in L:
    line= line.replace('\\n',' ')
    if "media_type" in line:
        print line.lstrip()
        LIST.append(line)
    if "permanent_url" in line and "@" not in line:
        cnt= cnt+1
        print cnt,line.lstrip()
        LIST.append(line)

!lbrynet get testing-file-download-functionality#f4e9cd3bc78b481ca62e06f1ae1a29b602255292 --download_directory=/home/jack/Desktop/JupyterNotebooks-languages

import urllib
import simplejson as json
import requests
import sys
search =raw_input("Search Term: ")
data = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"text": search, "page_size":60}}).json()
LINES = (json.dumps(data, indent=2 * ' '))
LIST =[]
#print LINES
Lin =str(LINES)
L = Lin.split("\n")
cnt = 0
for line in L:
    line= line.replace('\\n',' ')
    if "description" in line:
        print line.lstrip()
        LIST.append(line)
    if "permanent_url" in line and "@" not in line:
        cnt= cnt+1
        print cnt,line.lstrip()
        LIST.append(line)

LINES = (json.dumps(data, indent=2 * ' '))
LIST =[]
#print LINES
Lin =str(LINES)
L = Lin.split("\n")
cnt = 0
for line in L:
    line= line.replace('\\n',' ')
    if "description" in line:
        print line
        LIST.append(line)
    if "permanent_url" in line:
        cnt= cnt+1
        print cnt,line
        LIST.append(line)

for lines in LIST:
    if 'permanent_url' in lines:
        print lines

LINES = (json.dumps(data, indent=2 * ' '))
#print LINES
Lin =str(LINES)
L = Lin.split("\n")
cnt = 0
for line in L:
    line= line.replace('\\n',' ')
    if "description" in line:
        print line
    if "permanent_url" in line:
        cnt= cnt+1
        print cnt, line,"\n"
        print '----------------------'

print(json.dumps(data, indent=2 * ' '))

text ='''(1, '"permanent_url": "lbry://Intro_to_Python_Python_Basics_Part_1#4c1de7f251ad4bea5f9c5e09d3ab17918a2514ac",')'''
print text[30:-4]

!rm /home/jack/Desktop/LBRY-toolbox/5279.db

# %load LBRY_DLOAD
#!/usr/bin/python2
import os
from time import sleep
import urllib
import simplejson as json
import requests
import sys
import subprocess
from Completedpy2 import track_download
import sqlite3
import watchVID
database = '/home/jack/Desktop/LBRY-toolbox/5279.db'
conn = sqlite3.connect(database)
conn.text_factory = str
sql = '''create table if not exists LBRY(
description TEXT, url TEXT, unique (url));'''
conn.execute(sql) # shortcut for conn.cursor().execute(sql)
conn.commit()
c=conn.cursor()
search=raw_input("SEARCH : ")
data = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"text": search,  "page_size":50}}).json()
LINES = (json.dumps(data, indent=2 * ' '))
DES = ""
#print LINES
Lin =str(LINES)
L = Lin.split("\n")
cnt = 0
for line in L:
    DES = ""
    URL = ""
    line= line.replace('\\n',' ')
    if "description" in line:
        print line.lstrip()
        DES.append(line)
    if "permanent_url" in line:
        cnt= cnt+1
        print cnt,line.lstrip()
        URL.append(line)     
    
    
    
    try:
        c.execute("INSERT INTO LBRY VALUES (?,?)", (search, content))
    except:
        pass
conn.commit()
conn.close()
choice =int(raw_input("Enter the number you wish to download: Type 99 to exit "))
#if choice==99:raise SystemExit("Stop right there!")
if choice==99:raise SystemExit("Stopped by 99 !")    
print "You will be downloading:",(LIST[choice-1])

requests.post("http://localhost:5279", json={"method": "get", "params": {"uri": LIST[choice-1] }}).json()
print "Monitoring filesize increase of claim id "+LIST[choice-1][:-30]
'''
This is an alternative using " lbrynet "
bashCommand = "lbrynet get "+LIST[choice-1]+" --download_directory=/home/jack/Desktop/LBRY-cli/VIDEOS"
print bashCommand
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print "Monitoring filesize increase of claim id "+LIST[choice-1][:-30]
'''
track_download()

try:
    watchVID.WATCH()
except:
    sys.exit()




import os
HOME = os.environ['HOME']
print HOME

#%%writefile blobsize
#!/usr/bin/python2
import subprocess
import os
HOME = os.environ['HOME']

path = HOME+'/.local/share/lbry/lbrynet/blobfiles'
size = subprocess.check_output(['du','-sh' ,path]).split()[0].decode('utf-8')
print("Directory size: " + size)

# makes blobsize executeable
!chmod +x blobsize

import os
HOME = os.environ['HOME']
for r, d, f in os.walk(HOME+'/.local/share/lbry/lbrynet/blobfiles'):
    size = sum(os.path.getsize(os.path.join(r,n)) for n in f) / 1048576
    print "{} is {}{}".format(r, size, " Meg")

#!/home/jack/miniconda3/bin/python
# Script to get the size of the LBRY blobfiles directory
import subprocess
from os.path import expanduser
# Get HOME
HOME = expanduser("~")
# To the HOME add /.local/share/lbry/lbrynet/blobfiles
path = HOME+'/.local/share/lbry/lbrynet/blobfiles'
#get the directory size 
size = subprocess.check_output(['du','-sh' ,path]).split()[0].decode('utf-8')
print('Directory-size: lbrynet/blobfiles ' + size)



