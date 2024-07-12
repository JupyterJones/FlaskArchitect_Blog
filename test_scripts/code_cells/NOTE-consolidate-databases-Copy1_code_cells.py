# %load /usr/local/bin/pw
#!/usr/bin/python3

import sys
import sqlite3
import datetime
# get the current datetime and store it in a variable
currentDateTime = datetime.datetime.now()
current=str(currentDateTime)
conn = sqlite3.connect("/home/jake/Desktop/pas.bak/pas.db")
conn.text_factory = str
c = conn.cursor()
if len(sys.argv) < 3:
     print ("\n******* NED - Notes Editor **************")
     print ("Not enough options were passed.")     
     print ("NED requires 2 arguments. the first -H , -R , -I , -D or -S .\nThe second can be a period.")
     print ("If printing the database -T also add a filename of your choice ( no quotes required ):")
     print (" Example: NED -T Data2Text.txt")   
     print ("If wanting to read all entries use -R . (use the period)") 
     print ("even use the period with help.  -H .   must be entered.")
     print ("******************************************\n")
     sys.exit()
mod = sys.argv[1]
def create():

    import sqlite3
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/pas.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE PROJECT using FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text

def insert(data,conn=conn, c=c):
    c.execute("INSERT into PROJECT values (?)", (data+": \n"+current,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
    conn.close()
    return data

def search(data,conn=conn, c=c):
    #for row in c.execute("SELECT ROWID,* FROM PROJECT WHERE input MATCH ?",(data,)):
    #    print ("\nINFO Found Here:",row[0],row[1])
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        if data in row[1]:    
            print ("\nINFO Found Here:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
def delete(rowid,conn=conn, c=c):
    c.execute("DELETE FROM PROJECT WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()
    text = "ROWID "+rowid+" Deleted"
    return text

def main():
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/pas.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])

def prtmain(filename):
    fn = open(filename, "w")
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/pas.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        TEXT = "id:"+str(row[0])+"\n"+str(row[1])
        TEXT = str(TEXT)
        TEXT = TEXT.replace('\\n','\n')
        TEXT = "".join(TEXT)
        fn.write(TEXT+'\n----\n')

def HELP():
    TXT = """
    USE: NED argv[1] argv[2]
    argv[1] sets the mod:
    -I insert / -D delete / -R read / -H help
    examples:
    Notice the entry is in parenthese.
    -I  to insert "STUFF to be inserted"
    NED -I "STUFF to be inserted"
    -D to delete where rowid is 3
    NED -D 3
    Notice the period after -R . 
    -R . read all
    To search for the term "current project"
    NED -S 3
    -S "current project"
    NED -R .
    -H help on options
    NED -H .
    """
    print (TXT)

if mod == "-H" or mod == "h":
    HELP()        
if mod == "-R" or mod == "-r":
    main()
if mod == "-I" or mod == "-i":
    data = sys.argv[2]
    insert(data)
if mod == "-D" or mod == "-d":
    rowid = sys.argv[2]
    delete(rowid) 
if mod == "-S" or mod == "-s":
    data = sys.argv[2]
    search(data)       
if mod == "-T":
    filename = sys.argv[2]
    prtmain(filename)
if mod == "-C" or mod == "-c":
    create()
    print (create)
else:
    print ("_________________\n")
    print (sys.argv[2],"Command Completed")
    


!rm pas.data

!locate pas.db >> pas.data

# %load pas.data
/home/jack/Desktop/Pas.bak/pas.db
/home/jack/Desktop/Pas.bak/xpas.db
/home/jack/Desktop/Pas.bak/pas.bak/pas.db
/home/jack/Desktop/ReactMultiPageWebsite/pas.db
/home/jack/Desktop/pas.bak/pas.db
/home/jake/Desktop/pas.bak/opas.db
/home/jake/Desktop/pas.bak/pas.db
/home/jake/pas.bak/pas.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/Pas.bak/pas.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Downloads/pas.bak/pas.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Downloads/xvid/pas.bak/pas.db
/mnt/73777e11-76da-4fee-ba95-e731ac3ca459/pas.bak/pas.db


DATA = open("pas.data", "r").readlines()
for line in DATA:
    line=line.replace("\n","")
    print (line)


import sys
import sqlite3
def main(dbasename):
    conn = sqlite3.connect(dbasename)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])
dbasename = "/home/jake/Desktop/pas.bak/pas.db"
#dbasename = "/home/jake/Desktop/pas.bak/junk.db"
main(dbasename)

LIST = []
def dbaselist():
    DATA = open("pas.data", "r").readlines()
    for line in DATA:
        line=line.replace("\n","")
        print (line)
        LIST.append(line)
dbaselist()        

print(LIST)

import sys
import sqlite3
info = set()
cnt =0
def main(Dbase):
    conn = sqlite3.connect(Dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        #print (row[1])
        info.add(row[1])

#Dbase = "/home/jack/Desktop/Pas.bak/junk.db"
Dbase = "/home/jake/Desktop/pas.bak/pas.db"
for Dbase in LIST:
    cnt=cnt+1
    try:
        main(Dbase)
        print("CNT: ",cnt,"  ","Dbase: ", Dbase)
    except:
        print(Dbase)
        
        

print(len(info))

!rm /home/jack/Desktop/pas.bak/ALLPAS.db

!fuser /home/jack/Desktop/pas.bak/junk.db

!DD=$(fuser /home/jack/Desktop/pas.bak/junk.db)
!echo $DD

!echo $DD

sudo kill -9 `sudo lsof -t -i:27017`

# %load /usr/local/bin/unlockdb
echo "USE: unlockdb name.db"
DD=$(fuser $1)
echo $DD
kill -9 $DD


!unlockdb /home/jack/Desktop/pas.bak/junk.db

!fuser /home/jack/Desktop/pas.bak/ALLPAS.db



#kill -9 5430

import sqlite3
def verify(dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY input"):
        print (str(row[0])+": "+row[1])
    return 
#dbase = "/home/jack/Desktop/pas.bak/ALLPAS.db" 
dbase = "/home/jack/Desktop/pas.bak/junk.db" 
verify(dbase) 

import sqlite3
def insert(dbase):
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    for data in info:
        c.execute("INSERT into PROJECT values (?)", (data,))
        conn.commit()
def verify():
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    return 
#dbase = "/home/jack/Desktop/pas.bak/ALLPAS.db" 
dbase = "/home/jack/Desktop/pas.bak/junk.db"  
insert(dbase)
verify()

def verify():
    conn = sqlite3.connect(dbase)
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID asc"):
        print (row[0],": ",row[1])
    return 
dbase = "/home/jack/Desktop/pas.bak/ALLPAS.db"    
verify()

conn.close()

!pw -r . >> pw-r.results

# %load pw-r.results
1 :  https://localhost MakeAPassword
2 :  https://app.arukas.io jahral@yahoo.com tr4356hyFrt##
3 :  https://accounts.firefox.com jahral@yahoo.com ThinkPadT$#4848 
4 :  https://developer.vuforia.com jahral@yahoo.com URXH9uE4
5 :  https://www-947.ibm.com jahral@yahoo.com ppXYACKJS22
6 :  https://id.unity.com jahral@yahoo.com URXH9uE4Jd34 
7 :  https://99designs.com jahral@yahoo.com Th#@grte
8 :  https://passport.twitch.tv jacknorthrup PX#xyackjs44 
9 :  https://www.noip.com jackln Hgyt$3$4#RFg 
10 :  https://postimage.org jahral@yahoo.com URXH9uE4Jd34 
11 :  https://signup.wordpress.com myrareyes huhThinkPadT$# 
12 :  https://support.mozilla.org jahral@yahoo.com 54s#@3453fgs445354$#@
13 :  http://127.0.0.1 root ThinkPadT$#
14 :  https://www.sitepoint.com Uyhtg%$3er87uhk 
15 :  https://sso.godaddy.com madhatt3 Mad4stamps
16 :  https://www.db4free.net dbjsengine jURXH9uE4Jd34
17 :  https://www.instagram.com jlnorthrup pxyackjs22
18 :  https://www.ibm.com jahral@yahoo.com ppXYACKJS22
19 :  http://www.gimpusers.com jacknorthrup GCFBq7WzWSOhucujw2D1 
20 :  https://apps.ionic.io jahral@yahoo.com nKnVe3C2nKnVe3C2
21 :  https://adobeid.services.adobe.com jahral@yahoo.com Hgfsr$#32 
22 :  http://localhost localhost ThinkPadT$#
23 :  https://mlab.com jacknorthrupjr Uyhtg3er87
24 :  https://www.bikerplay.net jack.northrup.ph@gmail.com movies4me 
25 :  https://secure.photobucket.com jahral@yahoo.com bucket4ME 
26 :  https://my.justhost.com madhatterstamps.com Mad4stamps
27 :  https://www.codeschool.com jahral@yahoo.com GF54eDe2#$
28 :  https://www.linkedin.com jahral@yahoo.com ThinkPadT$#
29 :  https://www.kelloggsfamilyrewards.com jahral@yahoo.com rrrtttyyy 
30 :  https://login.skype.com northrupjl call2myra1948 
31 :  https://www.free-ebooks.net Pxyackkk
32 :  https://www.xoom.com jahral@yahoo.com +jhTy@@sho$@3# 
33 :  https://signup.netflix.com jahral@yahoo.com movies4me 
34 :  http://www.myspace.com jahral@yahoo.com space6me
35 :  https://www.justhost.com jack@freehandjack.com Mad4stamps
36 :  https://login.yahoo.com gorillajack_2012 gorilla4me
37 :  https://twitter.com ThinkPadT$#
38 :  https://secure.tagged.com biancaakira80@yahoo.com lovely321 
39 :  https://www.showsplash.com jahral@yahoo.com movies4me 
40 :  http://localhost:8000 Jack jacknorthrup 
41 :  http://www.opendiary.com @jacklnorthrup Pxyackjs48
42 :  https://www.redbubble.com jacknorthrup ThinkThinkt43
43 :  https://www.zazzle.com madhatter@madhatterstamps.com Pxyack1948
44 :  https://twitter.com JackLNorthrup tweetIT4me
45 :  https://login.justhost.com jackn@madhatterstamps.com ThinkPadT$#43
46 :  https://login.yahoo.com jahral@yahoo.com Ppxyackjs22Ppxyackjs22@1212
47 :  https://www.evernote.com Pxyackjs
48 :  https://www.networksolutions.com jacknorthrup Pxyackjs23
49 :  https://www.justhost.com sales@vintagecollage.com ThinkPadT$#
50 :  https://secure-beta.photobucket.com bucket4ME 
51 :  https://publisher.ebaypartnernetwork.com 479 7150734 ThinkPadT$#
52 :  https://secure.tagged.com jack@blogblocks.net rubadubdub4
53 :  http://www.quora.com jahral@yahoo.com ThinkPad
54 :  https://cloud.digitalocean.com jahral@yahoo.com HG654Frd123$@
55 :  https://www.stumbleupon.com jahral@yahoo.com movies4me 
56 :  http://quacker.hopto.org:8000 jacknorthrup jacknorthrup 
57 :  https://kunaki.com jahral@yahoo.com Pxyackjs22
58 :  http://112.204.33.155 adminpldt ThinkPadT$#
59 :  https://secure.istockphoto.com thinkpadt43
60 :  http://localhost:3000 jahral password
61 :  http://192.168.1.1 adminpldt 1234567890
62 :  https://publisher.ebaypartnernetwork.com 479 313 1379 PxyackjS22
63 :  http://www.tweetyjill.com 20493 tgs0293k
64 :  http://www.livinginthephilippines.com jahral@yahoo.com pXYACKJS22
65 :  http://www.veoh.com jacklnorthrup movies4me 
66 :  https://idp.godaddy.com jnhaglund Jonkoping13
67 :  https://sellercentral.amazon.com madhatter@madhatterstamps.com PPxyackj24
68 :  https://pragprog.com jahral@yahoo.com PPxyackj24
69 :  https://www.kelloggsfamilyrewards.com jack@jacknorthrup.com rrrtttyyy 
70 :  https://www.zazzle.com Madhatterstamps Pxyack1948
71 :  https://www.linkedin.com Linked4ME 
72 :  https://dotster.com jill@tweetyjill.com Panther53 
73 :  https://login.yahoo.com 54s#@3453fgs445354$#@
74 :  https://www.alibris.com jahral@yahoo.com books4me
75 :  https://secure.dotster.com tweetyjill.com Panther53 
76 :  https://members.cafepress.com sales@vintagecollage.com ThinkPadt43
77 :  https://www.comixology.com jahral ThinkThinkT43
78 :  https://www.playbug.net barbaralynmolnar.com mail4me 
79 :  https://login.yahoo.com hakomi_serye 09304623594
80 :  https://www.free-ebooks.net jahral@yahoo.com xyjmzc 
81 :  http://www.typetrigger.com password type4me 
82 :  https://my.justhost.com jackn ThinkPadT$#43
83 :  https://secure.tagged.com just4you@atcmadness.com ThinkPadT$#
84 :  https://openshift.redhat.com madhatterstamps@gmail.com yt6%r4#4errTT
85 :  http://www.mobileread.com jacknorthrup reedit4me 
86 :  https://login.yahoo.com miz_honeybear1948 MR3954HS
87 :  https://accounts.google.com rick@tweetyjill.com panther53 
88 :  https://www.zazzle.com madhatter ThinkPadT$#
89 :  http://localhost:8000 Myra myrareyes 
90 :  http://www.noip.com jackln Hgyt$3$4#RFg 
91 :  https://publisher.ebaypartnernetwork.com jahral@yahoo.com ThinkPadT$#
92 :  http://www.simplesite.com pictures4U
93 :  https://www.consumeraffairs.com jahral@yahoo.com cricketzte
94 :  http://www.trepstar.com jahral@yahoo.com PPxyackj24
95 :  https://www.npmjs.com jacknorthrup YHt54rd#eE3
96 :  http://localhost:3000 jack quack
97 :  https://login.live.com jahral@yahoo.com 245xbgsT%ytro78f
98 :  https://www.dropbox.com jack@jacknorthrup.com GO@LOWERcase 
99 :  https://www.dropbox.com jahral@yahoo.com GO@LOWERcase 
100 :  https://www.scoop.it jack@jacknorthrup.com tweet4metwo
101 :  https://idp.godaddy.com 30024758 Mad4stamps
102 :  http://localhost:3000 Mreyes ThinkThink
103 :  https://cart.godaddy.com madhatt3 Mad4stamps
104 :  https://weblink.freedomvoice.com calls4USA 
105 :  https://secure.tagged.com taggen_u@yahoo.com mailit4me 
106 :  https://account.live.com 245xbgsT%ytro78f
107 :  https://instagram.com jacklnorthrup Pxyackjs22
108 :  http://www.myrareyes.com jahral@yahoo.com myrat43T$#
109 :  https://www.playbug.net barbaralynmolnar@yahoo.com mail4me 
110 :  https://instagram.com pxyackjs22
111 :  https://adobeid-na1.services.adobe.com Pxyackjs22
112 :  http://epistlerblogs.com @DUSTYdogs
113 :  https://secure.tagged.com mio_corazon@rocketmail.com 0515MYRA
114 :  https://www.ecatmedia.net jack@jacknorthrup.com pxyackjs
115 :  http://112.204.33.155:8000 jacklnjr jacklnjr
116 :  https://cloud.docker.com jahral@yahoo.com chiHI654#hgh 
117 :  https://www.alumniclass.com jahral@yahoo.com ThinkThinkT43
118 :  https://www.zazzle.com ThinkT$#t43
119 :  https://www.facebook.com Mg091192
120 :  https://www.stumbleupon.com jacklnorthrup movies4me 
121 :  https://login.yahoo.com biancaakira80@yahoo.com lovely123 
122 :  https://en.wikipedia.org jacklnorthrup PPxyz2424 
123 :  http://www.xsusenet.com jahral30552 huyivcvn
124 :  https://idaas.iam.ibm.com jahral@yahoo.com HG54@eerF43
125 :  https://www.evernote.com jahral ThinkPadT$#
126 :  https://riouxsvn.com jacknorthrup Shair2u2
127 :  https://step.state.gov jahral22 1little2little 
128 :  https://www.lumosity.com jahral@yahoo.com Shair2u2
129 :  http://www.useralbum.com jahral@yahoo.com lg500g 
130 :  https://idp.godaddy.com madhatt3 Mad4stamps
131 :  http://www.renderosity.com Shair2u2
132 :  https://login.justhost.com jenny@burninglady.com Alady4me2 
133 :  https://login.justhost.com jenny@ladyinnogen.com Alady4me2 
134 :  https://247vidz.com jahral@yahoo.com movies4me 
135 :  http://www.businesscards.com.ph jack@pdfpaperpacks.com Shair2u2
136 :  https://accounts.autodesk.com Shair2u2
137 :  http://tweetychix.com tweetyjill Panther1953
138 :  https://www.dnsstuff.com jacknorthrup tryin4free
139 :  http://jacknorthrup.com @big1ststep
140 :  https://id.heroku.com jahral@yahoo.com Pxyackjs2525 
141 :  https://grubba.net jahral Pxyackjs22
142 :  https://login.justhost.com info@ladyinnogen.com Alady4me2 
143 :  http://kickass.to sunsonic2 sunsonic2 
145 :  https://www.amazingmail.com jack@jacknorthrup.com Pxyackjs@22
146 :  https://accounts.google.com pANTHER@1953 
147 :  http://www.useralbum.com Northrup lg500g 
148 :  http://tweetychix.com admin Panther53 
149 :  http://philippinemarbledpaper.com jahral@yahoo.com ThinkPadT$#
150 :  http://cd-fulfillment.com jahral@yahoo.com PPxyackj24
151 :  http://philippinemarbledpaper.com jack northrup ThinkPADt43
152 :  http://localhost jacknorthrup Shair2u2
153 :  https://www.zazzle.com sales@vintagecollage.com Pxyack1948
154 :  http://www.infectiousvideos.com jacknorthrup_0 Shair2u2
155 :  https://dotster.com jill Panther53 
156 :  http://newrelic.com jahral@yahoo.com Shair2u2
157 :  https://www.facebook.com jill@tweetyjill.com panther53 
158 :  http://www.pdfpaperpacks.com Jack Northrup Shair2u2
159 :  https://secure.ipage.com air2u2@U@ 
160 :  https://www.lwks.com jahral@yahoo.com Think4Think
161 :  https://www.openfilm.com jack@jacknorthrup.com movies4me 
162 :  http://localhost esrybe 1234 
163 :  http://www.the-blueprints.com jacknorthrup ThinkPADt43
164 :  http://www.snotr.com jahral movies4me 
165 :  https://www.keenplay.com jahral@yahoo.com Shair2u2
166 :  http://cpanel.1freehosting.com jahral@yahoo.com Pxyackjs23
167 :  http://localhost Jack Northrup Shair2u2
168 :  http://www.veoh.com jahral movies4me 
169 :  https://my.justhost.com alicein2 ?=84TX7P
170 :  https://riouxsvn.com jacknorthrup Shair2u2
171 :  http://www.lwks.com jahral 23deDR% 
172 :  http://www.ffiles.com jahral ffiles41948
173 :  http://jsfiddle.net Shair2u2
174 :  https://disqus.com madhatterstamps@gmail.com Shair2u2
175 :  https://login.justhost.com jack@myrareyes.com Mad4stamps
176 :  https://sellfy.com jahral@yahoo.com CD-RKING
177 :  http://www.free-ebooks.net jahral@yahoo.com books4me
178 :  https://accounts.google.com jack.northrup.ph@gmail.com Pxyackjs22
179 :  https://portalln.mybro.pldthome.com 1011501685 0720855070
180 :  http://www.wikispaces.com jacknorthrup Shair2u2
181 :  http://www.veoh.com jahral@yahoo.com movies4me 
182 :  http://jacknorthrup.com jack Y(CI0iiK2ydUi6%SOQ
183 :  https://login.justhost.com madhatt3 stAJJ@st13#48two 
184 :  http://www.mysqlforfree.com jacknorthrup Pxyackjs22
185 :  https://account.99designs.com Th#@grte
186 :  https://www.myspace.com space6me
187 :  https://just36.justhost.com:2083 ph OPEN4me 
188 :  http://businesscards.com.ph jack@pdfpaperpacks.com Shair2u2
189 :  http://www.zazzle.com sales@vintagecollage.com aaaaaaaa
190 :  http://localhost admin22 Shair2u2
191 :  https://login.justhost.com jenny@ladyinnogen.com Alady4me2 
192 :  http://pdfpaperpacks.com Jack Northrup Shair2u2
193 :  http://community.mybb.com jacknorthrup MyBB4un4ME
194 :  http://192.168.10.1 admin admin
195 :  http://bookza.org jahral@yahoo.com Shair2u2
196 :  http://www.justcloud.com. jahral@yahoo.com Shair2u2
197 :  http://www.ipage.com jack@pdfpaperpacks.com Shair2u2
198 :  https://my.smart.com.ph wisepro25@%
199 :  http://www.flixya.com jahral@yahoo.com Shair2u2
200 :  http://burninglady.com imalady2ME
201 :  https://www.openstreetmap.org Pxyackjs1919 
202 :  https://www.pinterest.com jack@jacknorthrup.com tseretniP 
203 :  http://www.pdfpaperpacks.com jacknorthrup jn2525dh2 
204 :  http://www.jacknorthrup.com admin PLubVOOC
205 :  http://localhost admin ppxyackjs 
206 :  http://localhost myra@myrareyes.com Shair2u2
207 :  https://gumroad.com jahral@yahoo.com Shair2u2
208 :  https://secure.tagged.com jack@madhatterjack.com time4achange 
209 :  https://market.renderosity.com jahral@yahoo.com Shair2u2
210 :  https://login.justhost.com jacknorthrup@philippinemarbledpaper.com Mad4stamps
211 :  http://www.freehandjack.com jacklnorthrup Pxyackjs22
212 :  http://philippineblogdesign.com admin Pxyackjs22
213 :  http://publisher.dailymotion.com 1000 motionmistress 
214 :  http://www.dailymotion.com jack@jacknorhrup.com Pxyackjs22
215 :  http://www.justcloud.com jack@jacknorthrup.com Shair2u2
216 :  http://panel.byethost.com b32_13770908 bc0dg14h
217 :  https://www.zend.com jahral@yahoo.com #$TdaPknihT
218 :  https://github.com blogblocks Shair2u2
219 :  http://www.gigabyteupload.com jahral movies4me 
220 :  http://philippineblogdesign.com admin22 Pxyackjs22
221 :  http://www.photojeepney.com pdfpaperpacks Shair2u2
222 :  http://www.infectiousvideos.com jacknorthrup Shair2u2
223 :  http://pictify.com jahral@yahoo.com Pxyackjs23
224 :  https://my.justhost.com theadve6 Panther@1953 
225 :  http://www.dailymotion.com jack@jacknorthrup.com Pxyackjs22
226 :  http://www.hotscripts.com jack@blogblocks.net ThinkPadT$#
227 :  http://tweetychix.com Panther53 
228 :  https://streamup.com Movies4me 
229 :  http://blogblocks.net jahral @ThinkPad2
230 :  https://just63.justhost.com:2083 jack Mad5stamps
231 :  http://maggbox.com dex phpphpphp 
232 :  https://secure.webhostinghub.com greenf19 Nov232013!@!@
233 :  http://www.blogblocks.net @ThinkPad2
234 :  http://localhost password
235 :  https://www.facebook.com darwin_northrup@yahoo.com @yam15niwraD 
236 :  http://burninglady.com jenny imaLADY2me#37
237 :  http://www.pdfpaperpacks.com admin nBvrTuy0
238 :  http://www.jacknorthrup.com jack@blog bewye7^%T 
239 :  https://accounts.google.com adelyn.torres.2014 $!)@ADT2
240 :  http://localhost 1234 1234 
241 :  https://secure.webhostinghub.com greenfoodgreenthumb@gmail.com Nov232013!@!@
242 :  http://byethost.com JACKNORTHRUP SHAIR2you2
243 :  http://blogblocks.net jack blogblocks4un4me
244 :  http://99designs.com jahral@yahoo.com Th3@grte
245 :  https://learnable.com jahral@yahoo.com Shair2u2
246 :  http://www.pdfpaperpacks.com Shair2u2pdf
247 :  http://www.jennynorthrup.com jenniferhnorthrup@gmail.com imaFISHER#37 
248 :  http://www.justcloud.com jack@blogblocks.org hp1702hp1702 
249 :  http://blogblocks.org Jack-Northrup @333##ThinkPad 
250 :  https://just63.justhost.com:2083 jack2 TIME4achange 
251 :  http://blogblocks-notetaker.hostei.com @ThinkPad2
252 :  https://scanmyserver.com jack@blogblocks.net aa53f4 
253 :  http://www.openfilm.com jacknorthrup movies4me 
254 :  https://just63.justhost.com:2083 jack1 time4achange 
255 :  https://www.tumblr.com jack@jacknorthrup.com 4u2btumbled
256 :  http://localhost jennynorthrup imaLADY2me#37
257 :  https://mongolab.com jacknorthrup shsh34rTF 
258 :  https://roymondous.wordpress.com jacknorthrup Shair2u2
259 :  https://twitter.com jack@blogblogs.net Mad5stamps
260 :  http://blogblocks.org admin Nov232013!@!@ 
261 :  http://official.dailymotion.com jack@jacknorthrup.com Pxyackjs22
262 :  http://w3schools.invisionzone.com jahral@yahoo.com tryntry2
263 :  http://www.tinymce.com mouseb4mice
264 :  https://secure.ipage.com blogblocksorg GF54eDe2#$
265 :  https://rubyforge.org jacknorthrup PPxyackjs22
266 :  http://www.tagged.com Password Ninasepa@2012
267 :  https://just36.justhost.com:2083 repair imaLADY2me#37
268 :  https://twitter.com jack@blogblocks.net Mad5stamps
269 :  https://just36.justhost.com:2083 wor2 5CK4io19
270 :  https://www.quora.com jahral@yahoo.com ThinkPad
271 :  https://fyp.ebay.com @Shair2u2 
272 :  https://disqus.com jack@jacknorthrup.com 123456zz
273 :  https://www.ipage.com jahral ThinkPadT$#1948 
274 :  https://accounts.google.com blogblocks.org@gmail.com ThinkPadT$#
275 :  https://twitter.com @blogblocks Mad5stamps
276 :  http://www.reddit.com jahral@yahoo.com movies4me 
277 :  https://www.deviantart.com jack@jacknorthrup.com 34gdh89(#&ddt
278 :  http://spoon.net jacknorthrup Shair2u2
279 :  http://dashboard.bloglines.com jack@blogblocks.net @thinkpadT43 
280 :  http://localhost jacklnorthrup 123456 
281 :  https://www.canva.com jahral@yahoo.com canva4more
282 :  http://mail.kazocapital.com jack@jacknorthrup.co movies4me 
283 :  https://just36.justhost.com:2083 scriber Pxyackjs2525 
284 :  http://members.000webhost.com jack@blogblocks.net pxyackjs1212 
285 :  https://just36.justhost.com:2083 Jenny imaLADY2me#37
286 :  https://just63.justhost.com:2083 Mad5stamps
287 :  https://code.tutsplus.com jack@jacknorthrup.com 123456zz
288 :  https://secure.ipage.com amouryacom 4Iam2$%$%dw6 
289 :  https://about.me jack@blogblocks.net hp1702hp1702 
290 :  https://www.facebook.com adelyn.torres2014@gmail.com $!)@ADT2
291 :  http://www.ustream.tv jahral@yahoo.com Movies4me 
292 :  https://login.yahoo.com manilyn.guimbarda Mg091192
293 :  http://liveweave.com jacknorthrup Shair2u2
294 :  https://just63.justhost.com:2083 exp Mad5stamps
295 :  https://secure.ipage.com jennynorthrup.com Jennifer2001@30 
296 :  https://www.tiberiumalliances.com jahral@yahoo.com North1948 
297 :  https://www.justhost.com madhatt3 @Mad4stamps
298 :  http://www.dailymotion.com motionmistress movies4me 
299 :  https://just63.justhost.com:2083 user time4achange 
300 :  http://file-manager.000webhost.com a4828022 pxyackjs1212 
301 :  http://greenfoodgreenthumb.com admin Greece2014!@#!@#
302 :  https://www.4shared.com jsl376sj7UG
303 :  http://filefactory.com @fileit4me
304 :  https://login.yahoo.com hanz.erica Anonymous098 
305 :  http://blogblocks.org JackNorthrup BlogBlocksT$#
306 :  https://disqus.com jahral@yahoo.com PX#xyackjs44 
307 :  http://blogblocks.org admin Nov232013!@!@
308 :  http://blogblocks.org @ThinkPad2
309 :  https://ssl.reddit.com movies4me 
310 :  http://www.surfing-waves.com jacknorthrup Newsit4me 
311 :  http://blogblocks.org phpuser Php4#21Z1948 
312 :  https://www.ipage.com blocks ThinkPadT$#1948 
313 :  https://login.justhost.com epistler_jack1 time4achange 
314 :  http://www.pdfpaperpacks.com jahral@yahoo.com nLK51v8Hjz
315 :  https://just63.justhost.com:2083 videos @time4TUBE
316 :  https://sourceforge.net jacklnorthrup Thinkhp1702
317 :  http://ph.godaddy.com madhatt3 Mad4stamps
318 :  http://login.myappmanager.com jahral@yahoo.com shair2u2
319 :  https://sourceforge.net jacknorthrup Thinkhp1702
320 :  https://www.ipage.com blogblocksorg ThinkPadT$#1948 
321 :  http://liveweave.com jahral@yahoo.com Shair2u2
322 :  https://bitnami.com jahral@yahoo.com Shair2u2
323 :  http://jennynorthrup.com jennynorthrup @run4MUSIC2@rwsm
324 :  http://www.000webhost.com jack@blogblocks.net pxyackjs1212 
325 :  https://www.facebook.com adelyn.torres2014@gmail.com $!)@ADT2
326 :  https://just36.justhost.com:2083 madhatt3_jack 67ygTF54$3rrr
327 :  https://wordpress.com jacknorthrup words4me
328 :  https://secure.webhostinghub.com greenfoodgreenthumb@gmail.com Greece2014!@#!@#
329 :  http://lists.automattic.com Jack Northrup blogblocksT$#
330 :  https://just63.justhost.com:2083 epistler_jackll iueyeryIYG%$^&*&TJJ
331 :  http://jacknorthrup.com @JHu76%fg#dS@33#
332 :  http://jacknorthrup.com jack@blog bewye7^%T 
333 :  https://accounts.google.com myra.n.reyes@gmail.com ThinkPadT$#
334 :  http://cpanel.serversfree.com jahral@yahoo.com shsh34rTF 
335 :  https://login.justhost.com jack 4me2mad 
336 :  https://myspace.com jahral@yahoo.com Uyhtg%$3er87uhk 
337 :  http://myrareyes.com Hakomi_S R2q58VmU0Y6XxqVQht
338 :  http://blogblocks.net JACKjack @DUSTYdogs
339 :  https://spoon.net jacknorthrup Shair2u2
340 :  https://signup.wordpress.com blogblockstwo BcuzIno#2 
341 :  https://accounts.google.com madhatterstamps @Mad4stamps$ 
342 :  https://www.alexa.com 34gdh89(#&ddt
343 :  https://accounts.google.com madhatterstamps@gmail.com @Mad4stamps$ 
344 :  https://ph.godaddy.com madhatt3 Mad4stamps
345 :  https://login.justhost.com madhatter@madhatterstamps.com @Mad4stamps
346 :  https://just36.justhost.com:2083 cpses_ma0BKBTsno 5TyLxgmc8U7ri0QlTI7cTa93sf9nqKQN
347 :  https://accounts.google.com anna.lisa.ph95@gmail.com @^^@li$@
348 :  https://signin.ebay.com madhatterjack @Shair2u2 
349 :  http://www.my-virtual-city.com aaaaaaa %$gajHt3huh
350 :  https://members.cj.com jack@jacknorthrup.com 8LqvCua@
351 :  http://blogblocks.net jacknorthrup @WORD4$3$48s 
352 :  https://ph.godaddy.com madhatt3 Mad4stamps
353 :  https://wordpress.org jacklnorthrup ThinkPadT$#
354 :  https://my.justhost.com host-146317 stAJJ@st13#48two
355 :  https://stackoverflow.com jack@blogblocks.net 34gdh89(#&ddt
356 :  http://localhost root ThinkPadT$#
357 :  http://cpanel.hostinger.ph 34gdh89(#&ddt
358 :  https://my.justhost.com myra@myrareyes.com @ThinkPadT$#22 
359 :  https://secure.ipage.com pdfpaperpackscom 45ytro78fxbgsT% 
360 :  https://login.yahoo.com jahral Ppxyackjs22Ppxyackjs22@1212
361 :  https://accounts.google.com tweetychix.news@gmail.com @Time4Achange
362 :  http://cpanel.hostinger.ph jack@jacknorthrup.com air2u2@U@ 
363 :  https://play.iflix.com jahral@yahoo.com movies4me 
364 :  https://login.mailchimp.com JACKLNORTHRUP air2u2@U@ 
365 :  https://just63.justhost.com:2083 epistler_dfdfsd 45ytro78fxbgs
366 :  https://signin.ebay.ph madhatterjack @Shair2u2 
367 :  http://www.vintagecollage.com admin vlKYOjvl
368 :  https://www.facebook.com hakomi_serye@yahoo.com ThinkPadT43
369 :  http://runningwithscissorsmusic.com jennynorthrup @run4MUSIC2@rwsm
370 :  http://jacknorthrup.com Jack Northrup @JHu76%fg#dS@33#
371 :  https://accounts.google.com blogblocks.org ThinkPadT$#
372 :  https://login.live.com @fgfg%$3JH2243 
373 :  https://www.facebook.com jahral@yahoo.com PPxyackjs22
374 :  http://www.jibjab.com jahral@yahoo.com hp1702hp1702 
375 :  https://my.justhost.com madhatt3 67ygTF54$3rrr
376 :  https://just63.justhost.com:2083 myra HG76gF%$dews 
377 :  https://login.skype.com jack.northrup48 call2myra 
378 :  http://www.webdeveloper.com jacknorthrup Shair2u2
379 :  https://secure.tagged.com hakomi_serye@yahoo.com O9304623594
380 :  https://my.justhost.com jack Thih^%4543f
381 :  https://just63.justhost.com:2083 jackll iueyeryIYG%$^&*&TJJ
382 :  https://just63.justhost.com:2083 epistler_jack Mad5stamps
383 :  https://just36.justhost.com:2083 ThinkPadT$#
384 :  https://my.justhost.com @ThinkPadT$#22 
385 :  https://www.paypal.com jahral@yahoo.com ThinkPadT$#
386 :  https://login.justhost.com jack@jacknorthrup.com Thih^%4543f
387 :  https://login.justhost.com jack2 JHu76%fg#dS@33# 
388 :  https://my.justhost.com host-1278248 34fgjgkHJ865^$ 
389 :  http://philippinemarbledpaper.net46.net air2u2@U@ 
390 :  http://www.my-virtual-city.com Jahral %$gajHt3huh
391 :  http://pdfpaperpacks.com jacknorthrup jn2525dh2 
392 :  http://blogblocks.net @BlogBlocks @WORD4$3$48s 
393 :  https://www.netteller.com dhy%$56hg6S
394 :  https://www.jibjab.com jahral@yahoo.com hp1702hp1702 
395 :  https://just36.justhost.com:2083 madhatt3 &y^jvg(Dfff88
396 :  https://www.amazon.com madhatter@madhatterstamps.com PPxyackj24
397 :  http://www.cj.com jack@jacknorthrup.com 8LqvCua@
398 :  https://codeanywhere.com gFT%458HG 
399 :  http://localhost jack ThinkPadT$#
400 :  https://www.dreamstime.com 34gdh89(#&ddt
401 :  http://eurekametalworks.com eurekametalworks Ready-Ore-Not14 
402 :  https://secure.e-onsoftware.com jahral@yahoo.com efac4b8b
403 :  https://accounts.icontem.com jlnorthrup 57hjg$#fv 
404 :  http://blogblocks.net @WORD4$3$48s 
405 :  https://login.skype.com 245xbgsT%ytro78f
406 :  http://localhost Jack Northrup @JHu76%fg#dS@33#v 
407 :  http://tweetychix.com jack khJ76gHnvbR%e2 
408 :  http://jacknorthrup.com jacknorthrup 556ghfds#$vD 
409 :  http://cpanel.1freehosting.com ajs^%$frF 
410 :  https://just63.justhost.com:2083 epistler_jack1 time4achange 
411 :  https://my.justhost.com myra HG76gF%$dews 
412 :  http://localhost:8080 jacknorthrup 556ghfds#$vD 
413 :  https://www.codeproject.com jack@blogblocks.net GHTY675s
414 :  https://accounts.pandasecurity.com 57hjg$#Fv 
415 :  https://accounts.google.com arkansasgirlfishing@gmail.com wind2theeast 
416 :  https://accounts.google.com jack.northrup.ph Pxyackjs22
417 :  http://www.lwks.com 23deDR% 
418 :  http://presshereeureka.com jennynorthrup #@ALADY2me2$ 
419 :  https://www.deviantart.com jahral@yahoo.com 34gdh89(#&ddt
420 :  http://pdfpaperpacks.com @ThinkPad2
421 :  http://www.cj.com jack@blogblocks.net UyQEi%cE
422 :  https://login.justhost.com myra@myrareyes.com HG76gF%$dews 
423 :  https://secure.tagged.com jahral@yahoo.com ThinkPadT$#
424 :  https://my.pldthome.com ThinkPadT$#
425 :  https://127.0.0.1 password
426 :  http://places.csail.mit.edu jacknorthrup places4me 
427 :  https://sso.redhat.com jahral@yahoo.com ThinkThinkT43
428 :  https://openshift.redhat.com jahral@yahoo.com ThinkThinkT43
429 :  https://gumroad.com 7734 
430 :  https://deepdreamgenerator.com jahral@yahoo.com luciddreams
431 :  https://id.docker.com jacknorthrup chiHI654#hgh 
432 :  https://community.ardour.org jacknorthrup biW5FesXjz
433 :  https://dreamscopeapp.com jahral@yahoo.com neatdreampictures 
434 :  http://www.blogblocks.org @DUSTYdogs
435 :  http://documentslide.com jahral@yahoo.com Documents1948
436 :  https://freemusicarchive.org jacknorthrup publicdomainmusic 
437 :  https://freemusicarchive.org jahral@yahoo.com PUBLICKDOMAINMUSIC
438 :  http://www.fractalforums.com jahral@yahoo.com shyta545dsr
439 :  https://my.justhost.com joann Ninay@2012
440 :  https://secure.tagged.com ninasepa@yahoo.com Ninasepa@2012
441 :  http://127.0.0.1:9000 admin Shair2u2
442 :  http://localhost:8888 password
443 :  https://readthedocs.org madhatterstamps@gmail.com hiphiu54D#
444 :  https://www.linkedin.com jack@blogblocks.net ThinkPadT$#
445 :  https://algorithmia.com jahral@yahoo.com ^5tRf455gh#
446 :  https://www.grammarly.com %%writefile
447 :  https://www.pexels.com jahral@yahoo.com df65SR@r
448 :  https://luarocks.org jacklnorthrup ^5tRf455gh#
449 :  http://interactivepython.org jahral@yahoo.com 42LearnPython
450 :  https://nteract.slack.com df65SR@r
451 :  https://leanpub.com jacklnorthrup 123jacklnorthrup
452 :  https://www.codeproject.com jahral@yahoo.com hnDFMLSd8kkT
453 :  https://www.perlego.com jahral@yahoo.com Freebooks4me 
454 :  https://www.pythonanywhere.com madhatterstamps@gmail.com Think$Me
455 :  https://www.openstreetmap.org 3774190 jack1948lloyd
456 :  https://urs.earthdata.nasa.gov jacknorthrup Lloyd1948 
457 :  https://urs.earthdata.nasa.gov jacklnorthrup Lloyd1948 
458 :  https://www.reddit.com jacklnorthrup Thinkit0ut
459 :  https://just63.justhost.com:2083 jaclnorthrut stAJJ@st13lloy$3
460 :  http://www.ripplear.com madhatterstamps@gmail.com ThinkPip4me
461 :  http://www.ripplear.com a5e4d 
462 :  https://www.eyrieplay.com madhatterstamps@gmail.com Think43 
463 :  https://www.gitbook.com jacknorthrup WeDream4545
464 :  https://forum.processing.org jacknorthrup WeDream4545
465 :  https://www.shadertoy.com jacknorthrup ThinkT$#
466 :  https://www.shadertoy.com jahral@yahoo.com ThinkT$#
467 :  https://www.openprocessing.org jahral@yahoo.com thinkT$#
468 :  https://www.deviantart.com jacknorthrup 34gdh89(#&ddt
469 :  https://login.live.com northrupjl call2myra 
470 :  https://web15.secureinternetbank.com jl222n dhy%$5w6hg6S 
471 :  https://www.genymotion.com jahral@yahoo.com auto43menu
472 :  https://signup.na.leagueoflegends.com jack 437Discover
473 :  https://signup.na.leagueoflegends.com jacklnorthrup 437Discover
474 :  https://dashboard.ionicjs.com jacknorthrup nKnVe3C2nKnVe3C2
475 :  https://dashboard.heroku.com 4ef90f20-8c66-4eab-9b59-7c371ae386ad 
476 :  https://expo.io ExpoStuff expo4me 
477 :  https://expo.io jacklnorthrup ExpoStuff 
478 :  https://snack.expo.io jacklnorthrup ExpoStuff 
479 :  https://clients.databasemart.com jahral@yahoo.com dydyNOT4$##48
480 :  https://www.gigarocket.net jacknorthrup dydyNOT4$##48
481 :  http://www.htaccesstools.com GohartKahanas dydyNOT4$##48
482 :  http://blogblocks.net GohartKahanas MonkMonkENTER
483 :  https://www.sslforfree.com jahral@yahoo.com MonkMonkENTER
484 :  https://just63.justhost.com:2083 blogblocks GtfR433#454
485 :  https://just63.justhost.com:2083 newblock GtfR433#454
486 :  https://cloud.canister.io jacknorthrup GtfR433#454
487 :  https://sourcecontribute.wordpress.com jacknorthrup words4me
488 :  https://www.openstack.org jahral@yahoo.com GtfR433#454
489 :  https://www.openstack.org jahral GtfR433#454
490 :  https://openstackid.org jahral@yahoo.com GtfR433#454
491 :  https://witsbits.com jahal@yahoo.com GtfR433#454
492 :  https://witsbits.com madhatterstamps@gmail.om GtfR433#454
493 :  https://hubic.com jahral@yahoo.com GtfR433#454GtfR433#454 
494 :  http://127.0.0.1:5000 jacknorthrup password
495 :  chrome://FirefoxAccounts 04181e302f8f48e6b83a5c351715d429 {"version":1,"accountData":{"kA":"a5c29234f25c5ca813992f80daf4637a93c51340a75c34d5b96ddc39c60c3a01","kB":"bc7c5cad8317505f84f97697c33332711ecb0dc5bc80ad70da3f38cd1d36432d"}}
496 :  https://www.facebook.com 09568127671 mercedes11
497 :  https://secure.tagged.com manilyn1992guimbarda@gmail.com lovely12345
498 :  https://accounts.google.com manilyn1992guimbarda lovely12345
499 :  https://manage.realvnc.com jahral@yahoo.com ThinkTank@1948 
500 :  https://crm.vpscheap.net jahral@yahoo.com G22tfR433#454
501 :  http://jacknorthrup.com root ThinkPadT$#
502 :  http://www.jacknorthrup.com root ThinkPadT$#
503 :  http://www.jacknorthrup.com root ThinkT2524collage 
504 :  https://www.freelancer.ph jacknorthrup 34gtUH5636$^ 
505 :  https://www.name.com jahral@yahoo.com HgtfR45$3asdd
506 :  http://112.202.78.211 admin 1234 
507 :  http://5jelly.info Northrup Ndmoe1948 
508 :  http://vintagecollage.com JACKjack @DUSTYdogs
509 :  https://www.namecheap.com jacknorthrup JUY65H6ytYt54346
510 :  https://demo.iredmail.org postmaster@test.com iredmail
511 :  https://192.250.236.160:943 openvpn ThinkT2524collage 
512 :  https://portal.privatetunnel.com jahral@yahoo.com ThinkT2524collage 
513 :  https://www.name.com jacknorthrup HgtfR45$3asdd
514 :  http://www.jacknorthrup.com jack ThinkT2524collage 
515 :  https://www.jacknorthrup.com jack ThinkT2524collage 
516 :  http://developer.goibibo.com jacklnorthrup 123password4me 
517 :  https://goibibo.3scale.net jacklnorthrup 123password4me 
518 :  http://freedns.afraid.org jacknorthrup SavenIT!($*) 
519 :  http://localhost:8100 Think!($*)andBORN 
520 :  https://www.floydhub.com jacklnorthrup Y(CI0iiK2ydUi6%SOQ
521 :  https://twitter.com jahral@yahoo.com tweetIT4me
522 :  https://cloud.scaleway.com jahral@yahoo.com 1948dosomething1948
523 :  http://100GBFreeCloudDrivefromDegoo madhatterstamps@gmail.com Mad4Store
524 :  http://blogblocks.net GohartKahanas MonkMonkENTER
525 :  http://genymotion.com jahral@yahoo.com auto43menu
526 :  http://gigarocket.net jacknorthrup dydyNOT4$##48
527 :  http://github.com  blogblocks Shair2u2
528 :  http://Netflix jahral@yahoo.com movies4me
529 :  http://openprocessing.org madhatterstamps@gmail.com openit4me
530 :  http://twitter.com jacklnorthrup tweetIT4me
531 :  http://yahoo.com jahral Ppxyackjs22Ppxyackjs22@1212
532 :  https://www.paperspace.com jahral@yahoo.com Y(CI0iiK2ydUi6%SOQ -Active :Apr 8, 2018')
533 :  https://www.paperspace.com jahral@yahoo.com Y(CI0iiK2ydUi6%SOQ -Active :Apr 8, 2018')
534 :  ftp://epistlerblogs.com jack@epistlerblogs.com ThinkPadT$#43')
535 :  ssh -L 8100:localhost:8888 jack@192.250.236.207 ThinkT2524collage')
536 :  mega hubic GtfR433#454GtfR433#454 ')
537 :  router   B4ihad1212ANdmoe19488491  B4ihad1YCI0iiK2ydUi6SOQ212ANdmoe19488491YCI0iiK2ydUi6SOQdde23234 ')
538 :  1234567890')
539 :  0987654321jack')
540 :  jack-testing123')
541 :  Myra facebook facebook ')
542 :  Myra facebook facebook May 15 1984 ThinkPadT$#43 army seyer')
543 :  http://jsfiddle.net Shair2u2 jahral@yahoo.com')
544 :  iphone user password jahral@yahoo.com ThinkPadT$#43')
545 :  GET PASSWORD: apple https://iforgot.apple.com ThinkPadT$#43 \\ ')
546 :  
@THINKpad4ME  Udemy.com
548 :  
account - burninglady
user - Dad
password - MyKidMadeMeDoIt!
AWS aws Amazon amazon 
549 :  
  https://privacy.com/signup/confirm-email
550 :  
  https://privacy.com/signup/confirm-email
551 :  
  https://privacy.com/signup/confirm-email
552 :  
$x5e$PH4CRKCey5  https://privacy.com/signup/confirm-email
553 :  
https://profile.w3schools.com/
jack.northrup.ph@gmail.com
@tryW3website

554 :  new router: NNP-SQ121 THINKjn1948
555 :  
facebook yorsky_ed@yahoo.com 12131415

556 :  
https://game.gtarcade.com/game/?sid=2625310001&gameId=346
blogblocks.org@gmail.com
@thinkGam3

557 :   
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
https://beta.openai.com/account/api-keys
jacknorthrup.ph@gmail.com
org-VBX7nxFdDknqQWAAYYZbgJiL
jahral

558 :  
https://console.apify.com/sign-up
HYcP4gtM64dfmDg
jahral@yahoo.com

559 :   think@1948PAD
oracle jahral@yahoo.com java '

560 :  
password 4meDiscord1948 jack.northup.ph@gmail.com
JackNorthrup

561 :   twitch Twitch  mylinuxtoybox PX#xyackjs44
562 :   twitch Twitch  mylinuxtoybox PX#xyackjs44
live_134441555_BQlf1HI0SaOykwb48uNdqkLhzcOFmB stream 
563 :   twitch Twitch  mylinuxtoybox PX#xyackjs44
live_134441555_BQlf1HI0SaOykwb48uNdqkLhzcOFmB stream 
access token k6qa770hu3bwg6j17jtlr90k2e9smd
refresh token   ufo6dk51j2nf4rktgfav6ftlk0mjv328x01s8vuafkakwxml49
client id   gp762nuuoqcoxypju8c569th9wz7q5

564 :  
Pxyackjs1948
lbry - jahral@yahoo.com
odysee.com : 
2022-07-12 09:45:12.015811
565 :  github key:
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
ThinkReact: 
2022-07-21 06:45:26.526466
566 :  
jacknort35456GT 
archive.org : 
2022-07-24 12:46:53.228179
567 :  
Get Your S3-Like API Keys
Your S3 access key: zNTF2kiWolLuxRDC
Your S3 secret key: mIO87RqyBjl9afXn
: 
2022-07-24 13:25:44.944206
568 :  ##ThinkPad22TT246479##
What was the model of your first car?
What is the name of the street where you grew up?
ford bond: 
2022-07-26 12:17:02.329357
569 :  ##ThinkPad22TT246479##
What was the model of your first car?
What is the name of the street where you grew up?
ford bond
APple id : 
2022-07-26 12:17:35.281384
_________________

. Command Completed


def insert(data):
    conn.text_factory = str
    c = conn.cursor()
    c.execute("INSERT into PROJECT values (?)", (data+": \n"+current,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])

import sys
import sqlite3
info = set()
def main():
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])
main()

import sys
import sqlite3
#info = set()
def main():
    conn = sqlite3.connect("/home/jack/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])
main()

!sudo updatedb

import sys
import sqlite3
#info = set()
def main():
    conn = sqlite3.connect("mnt/73777e11-76da-4fee-ba95-e731ac3ca459/Desktop/WORKING/reactwithprisma/starter/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[1])
        info.add(row[1])
main()

# %load NOTE
#!/usr/bin/python3
import sys
import sqlite3
conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
conn.text_factory = str
c = conn.cursor()
if len(sys.argv) < 3:
     print ("\n******* NOTE - Notes Editor **************")
     print ("Not enough options were passed.")     
     print ("NOTE requires 2 arguments. the first -H , -R , -I , -D or -S .\nThe second can be a period.")
     print ("If printing the database -T also add a filename of your choice ( no quotes required ):")
     print (" Example: NOTE -T Data2Text.txt")   
     print ("If wanting to read all entries use -R . (use the period)") 
     print ("even use the period with help.  -H .   must be entered.")
     print ("******************************************\n")
     sys.exit()
mod = sys.argv[1]
def create():

    import sqlite3
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute("CREATE VIRTUAL TABLE PROJECT using FTS4 (input)")
    conn.commit()
    text = "Database Created"
    return text

def insert(data,conn=conn, c=c):
    c.execute("INSERT into PROJECT values (?)", (data,))
    for row in c.execute("SELECT ROWID,* FROM PROJECT ORDER BY ROWID DESC LIMIT 1"):
        print ("\nPOST VERIFIED:\n",row[0],row[1])
    conn.commit()
    conn.close()
    return data

def search(data,conn=conn, c=c):
    #for row in c.execute("SELECT ROWID,* FROM PROJECT WHERE input MATCH ?",(data,)):
    #    print ("\nINFO Found Here:",row[0],row[1])
    for row in c.execute("SELECT ROWID,* FROM PROJECT"):
        if data in row[1]:    
            print ("\nINFO Found Here:\n",row[0],row[1])
    #conn.commit()
    #conn.close()
def delete(rowid,conn=conn, c=c):
    c.execute("DELETE FROM PROJECT WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()
    text = "ROWID "+rowid+" Deleted"
    return text

def main():
    conn = sqlite3.connect("/home/jake/Desktop/pas.bak/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        print (row[0],": ",row[1])

def prtmain(filename):
    fn = open(filename, "w")
    conn = sqlite3.connect("/home/jake/Desktop/notes.db")
    conn.text_factory = str
    c = conn.cursor()
    for row in c.execute("SELECT rowid, * FROM PROJECT"):
        TEXT = "id:"+str(row[0])+"\n"+str(row[1])
        TEXT = str(TEXT)
        TEXT = TEXT.replace('\\n','\n')
        TEXT = "".join(TEXT)
        fn.write(TEXT+'\n----\n')

def HELP():
    TXT = """
    USE: NOTE argv[1] argv[2]
    argv[1] sets the mod:
    -I insert / -D delete / -R read / -H help
    examples:
    Notice the entry is in parenthese.
    -I  to insert "STUFF to be inserted"
    NOTE -I "STUFF to be inserted"
    -D to delete where rowid is 3
    NOTE -D 3
    Notice the period after -R . 
    -R . read all
    To search for the term "current project"
    NOTE -S 3
    -S "current project"
    NOTE -R .
    -H help on options
    NOTE -H .
    """
    print (TXT)

if mod == "-H" or mod == "h":
    HELP()        
if mod == "-R" or mod == "-r":
    main()
if mod == "-I" or mod == "-i":
    data = sys.argv[2]
    insert(data)
if mod == "-D" or mod == "-d":
    rowid = sys.argv[2]
    delete(rowid) 
if mod == "-S" or mod == "-s":
    data = sys.argv[2]
    search(data)       
if mod == "-T":
    filename = sys.argv[2]
    prtmain(filename)
if mod == "-C" or mod == "-c":
    create()
    print (create)
else:
    print ("_________________\n")
    print (sys.argv[2],"Command Completed")
    




