import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'bigfeedfts.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS bbctech 
USING FTS3(head, feed);
""")
count=0
while count<35:
    count=count+1
    # This is for posting my actual list has 35 sources
    if count==1:feed='http://feeds.bbci.co.uk/news/technology/rss.xml'
    if count==2:feed='http://www.cbn.com/cbnnews/us/feed/'
    d = feedparser.parse(feed)
    for post in d.entries:
        aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
        bb = `post.title + ": " + post.link + ""`
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
        conn.commit()
        conn.close()
        
        
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    count=count+1
    print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'bigfeedfts.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
#c.execute('''
#CREATE TABLE IF NOT EXISTS bbctech
#(head text, feed text)
#''');
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS bbctech 
USING FTS3(head, feed);
""")
count=0
while count<35:
    count=count+1
    if count==1:feed='http://feeds.bbci.co.uk/news/technology/rss.xml'
    if count==2:feed='http://www.cbn.com/cbnnews/us/feed/'
    if count==3:feed='http://feeds.reuters.com/Reuters/worldNews'
    if count==4:feed='http://feeds.bbci.co.uk/news/technology/rss.xml'
    if count==5:feed='http://news.sky.com/info/rss'
    if count==6:feed='http://www.cbn.com/cbnnews/us/feed/'
    if count==7:feed='http://feeds.reuters.com/Reuters/domesticNews'
    if count==8:feed='http://news.yahoo.com/rss/'
    if count==9:feed='http://www.techradar.com/rss'
    if count==10:feed='https://www.wired.com/feed/rss'
    if count==11:feed='http://www.zdnet.com/zdnet.opml'
    if count==12:feed='http://www.computerweekly.com/rss/All-Computer-Weekly-content.xml'
    if count==13:feed='http://gadgets.ndtv.com/rss/feeds'
    if count==14:feed='http://feeds.arstechnica.com/arstechnica/index'        
    if count==15:feed='https://www.techworld.com/news/rss'
    if count==16:feed='https://www.infoworld.com/index.rss'        
    if count==18:feed='https://www.pcworld.com/index.rss'   
    if count==19:feed='http://tech.economictimes.indiatimes.com/rss/technology'
    if count==20:feed='https://www.technologyreview.com/stories.rss'        
    if count==21:feed='http://tech.economictimes.indiatimes.com/rss/topstories'
    if count==22:feed='http://feeds.feedburner.com/digit/latest-from-digit'
    if count==23:feed='http://feeds.techsoup.org/TechSoup_Articles'
    if count==24:feed='http://rss.sciam.com/ScientificAmerican-News?format=xml'
    if count==25:feed='https://www.sciencedaily.com/rss/all.xml'    
    if count==26:feed='http://feeds.nanowerk.com/nanowerk/agWB'
    if count==27:feed='http://feeds.nanowerk.com/NanowerkNanotechnologySpotlight'
    if count==28:feed='http://feeds.nanowerk.com/feedburner/NanowerkRoboticsNews'
    if count==29:feed='http://feeds.nanowerk.com/NanowerkSpaceExplorationNews'
    if count==30:feed='http://www.npr.org/rss/rss.php?id=1019'
    if count==31:feed='http://feeds.nature.com/news/rss/news_s16?format=xml'
    if count==32:feed='http://feeds.latimes.com/latimes/technology?format=xml'
    if count==33:feed='http://feeds.feedburner.com/BadAstronomyBlog?format=xml'
    if count==34:feed='http://feeds.newscientist.com/physics-math'
    if count==35:feed='http://rss.slashdot.org/Slashdot/slashdotMain'
    d = feedparser.parse(feed)
    for post in d.entries:
        aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
        bb = `post.title + ": " + post.link + ""`
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
        conn.commit()
        conn.close()
        
        
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    count=count+1
    print"\nNumber :",count," -----\n",(row)

import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
count=0
req = 5000
for row in c.execute('SELECT * FROM bbctech'):    
    count=count+1
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    print"\nNumber :",count," -----\n",(row)    
    if count > req:
        conn.close()
        sys.exit()
        

import sqlite3
import sys
conn = sqlite3.connect('collection.db')
c = conn.cursor()
count=0
# limits query to 1000
req=1000
search = raw_input("Search : ")

for row in c.execute('SELECT rowid,* FROM tweets WHERE text MATCH ?', (search,)):    
    count=count+1
    
    print count,"-",(row)[1]," -- by",(row)[2],"\n"
    if count > req:
        conn.close()
        sys.exit()

import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
count=0
req = 5000
search = raw_input("Search : ")

for row in c.execute('SELECT rowid,* FROM bbctech WHERE feed MATCH ?', (search,)):    
#for row in c.execute('SELECT * FROM bbctech WHERE feed LIKE "%phone%"'):    
    count=count+1
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    print"\nNumber :",count," -----\n",(row)    
    if count > req:
        conn.close()
        sys.exit()
        

import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
count=0
req = 5000
search = raw_input("Get by ROWID : ")

for row in c.execute('SELECT rowid,* FROM bbctech WHERE rowid=?', (search,)):    
#for row in c.execute('SELECT * FROM bbctech WHERE feed LIKE "%phone%"'):    
    count=count+1
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    print"\nNumber :",count," -----\n",(row)    
    if count > req:
        conn.close()
        sys.exit()
        

import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
count=0
req = 5000
for row in c.execute('SELECT * FROM bbctech WHERE feed LIKE "%phone%"'):    
    count=count+1
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    print"\nNumber :",count," -----\n",(row)    
    if count > req:
        conn.close()
        sys.exit()
        

# WORKS
import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
txt = raw_input("What are you looking for?")

for row in c.execute("SELECT * FROM bbctech WHERE feed MATCH ?", (txt,)):
    data = c.fetchall()
    data=data.replace('(u"(u','\n')
    print data,"\n-----\n","\n"

# WORKS
import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
count=0
# Limited Amount of Results
req=50
num = raw_input("What are you looking for?")

for row in c.execute("SELECT * FROM bbctech WHERE feed MATCH ?", (num,)):
    row=str(row)
    row=row.replace("(u\"(u","");row=row.replace("', u'","  ");
    row=row.replace("u'"," ");row=row.replace(')", u" ', "\n");
    row=row.replace(" http://","\nhttp://");row=row.replace('")','')
    row=row.replace("'","");row=row.replace("#tk.rss_all", "")
    count=count+1
    print "\n",count,"-----\n",(row)
    if count > req:
        conn.close()
        sys.exit()
        

!sqlite3 bigfeed2.db "PRAGMA integrity_check"

# WORKS
import sqlite3
import sys
conn = sqlite3.connect('bigfeedfts.db')
c = conn.cursor()# Never 
count=0
req=4
num = raw_input("What line are you looking for?")

for row in c.execute("SELECT * FROM bbctech WHERE feed MATCH ?", (num,)):
    count=count+1
    print(row),"\n-----\n"
    if count > req:
        conn.close()
        sys.exit()
        

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'test4.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');
count=0
while count<8:
    count=count+1
    if count==3:feed='http://www.zdnet.com/zdnet.opml'
    d = feedparser.parse(feed)
    for post in d.entries:
        aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
        bb = `post.title + ": " + post.link + ""`
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
        conn.commit()
        conn.close()
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    count=count+1
    print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'test3.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');
count=0
while count<8:
    count=count+1
    if count==1:feed='http://www.techradar.com/rss'
    if count==2:feed='https://www.wired.com/feed/rss'
    if count==3:feed='http://www.zdnet.com/zdnet.opml'
    if count==4:feed='http://www.computerweekly.com/rss/All-Computer-Weekly-content.xml'
    if count==5:feed='http://gadgets.ndtv.com/rss/feeds'
    if count==6:feed='http://feeds.arstechnica.com/arstechnica/index'
    if count==7:feed='https://www.techworld.com/news/rss'
    if count==8:feed='https://www.infoworld.com/index.rss'
    d = feedparser.parse(feed)
    for post in d.entries:
        aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
        bb = `post.title + ": " + post.link + ""`
        conn = sqlite3.connect(Dbase)
        c = conn.cursor()
        c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
        conn.commit()
        conn.close()
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never
count=0
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
    row=str(row)
    row=row.replace("(u","");row=row.replace('", u"u',"\n")
    row=row.replace("/', u'","   ");row=row.replace('"',"")
    row=row.replace("', u'","  ");row=row.replace("')","  ")
    row=row.replace("'","");row=row.replace("  , uu","\n")
    count=count+1
    print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
Dbase = 'news.db'
conn = sqlite3.connect(Dbase)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');
A_In='http://feeds.bbci.co.uk/news/technology/rss.xml'
B_In='http://www.cbn.com/cbnnews/us/feed/'
C_In='http://feeds.reuters.com/Reuters/worldNews'
D_In='http://feeds.bbci.co.uk/news/technology/rss.xml'
E_In='http://news.sky.com/info/rss'
F_In='http://www.cbn.com/cbnnews/us/feed/'
G_In='http://feeds.reuters.com/Reuters/domesticNews'
H_In='http://news.yahoo.com/rss/'
count=0
d = feedparser.parse(A_In)
for post in d.entries:
    aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
    bb = `post.title + ": " + post.link + ""`
    conn = sqlite3.connect(Dbase)
    c = conn.cursor()
    c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
    conn.commit()
    conn.close()
conn = sqlite3.connect(Dbase)
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
        row=str(row)
        row=row.replace("(u","");row=row.replace('", u"u',"\n")
        row=row.replace("/', u'","   ");row=row.replace('"',"")
        row=row.replace("', u'","  ");row=row.replace("')","  ")
        row=row.replace("'","");row=row.replace("  , uu","\n")
        count=count+1
        print"\nNumber :",count," -----\n",(row)

import sqlite3
conn = sqlite3.connect('news.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid'):
        row=str(row)
        row=row.replace("(u"," ")
        row=row.replace('", u"u',"\n")
        print(row),"\n-----\n"

import sqlite3
import feedparser
import time
import sqlite3
conn = sqlite3.connect('news.db')
#conn = sqlite3.connect('testrss.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');

test01 = 'http://feeds.feedburner.com/TechCrunch/'
test02 = 'http://feeds.feedburner.com/crunchgear'
test03 = 'http://feeds.feedburner.com/TechCrunch/Twitter'
test04 = 'https://www.cnet.com/cnet-podcasts/'
test05 = 'https://www.cnet.com/rss/news/'
    
    
count=0
d = feedparser.parse(test01)
for post in d.entries:
    aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
    bb = `post.title + ": " + post.link + ""`
    conn = sqlite3.connect('newnews.db')
    c = conn.cursor()
    c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
    conn.commit()
    conn.close()
conn = sqlite3.connect('newnews.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
        row=str(row)
        row=row.replace("(u","");row=row.replace('", u"u',"\n")
        row=row.replace("/', u'","   ");row=row.replace('"',"")
        row=row.replace("', u'","  ");row=row.replace("')","  ")
        row=row.replace("'","");row=row.replace("  , uu","\n")
        row=row.replace(" \\u2013", "")
        count=count+1
        print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
conn = sqlite3.connect('news.db')
#conn = sqlite3.connect('testrss.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');

test01 = 'http://feeds.feedburner.com/TechCrunch/'
test02 = 'http://feeds.feedburner.com/crunchgear'
test03 = 'http://feeds.feedburner.com/TechCrunch/Twitter'
test04 = 'https://www.cnet.com/cnet-podcasts/'
test05 = 'https://www.cnet.com/rss/news/'
    
    
count=0
d = feedparser.parse(test02)
for post in d.entries:
    aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
    bb = `post.title + ": " + post.link + ""`
    conn = sqlite3.connect('newnews.db')
    c = conn.cursor()
    c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
    conn.commit()
    conn.close()
conn = sqlite3.connect('newnews.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
        row=str(row)
        row=row.replace("(u","");row=row.replace('", u"u',"\n")
        row=row.replace("/', u'","   ");row=row.replace('"',"")
        row=row.replace("', u'","  ");row=row.replace("')","  ")
        row=row.replace("'","");row=row.replace("  , uu","\n")
        row=row.replace(" \\u2013", "")
        count=count+1
        print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
conn = sqlite3.connect('news.db')
#conn = sqlite3.connect('testrss.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');

test01 = 'http://feeds.feedburner.com/TechCrunch/'
test02 = 'http://feeds.feedburner.com/crunchgear'
test03 = 'http://feeds.feedburner.com/TechCrunch/Twitter'
test04 = 'https://www.cnet.com/cnet-podcasts/'
test05 = 'https://www.cnet.com/rss/news/'
    
    
count=0
d = feedparser.parse(test03)
for post in d.entries:
    aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
    bb = `post.title + ": " + post.link + ""`
    conn = sqlite3.connect('newnews.db')
    c = conn.cursor()
    c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
    conn.commit()
    conn.close()
conn = sqlite3.connect('newnews.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
        row=str(row)
        row=row.replace("(u","");row=row.replace('", u"u',"\n")
        row=row.replace("/', u'","   ");row=row.replace('"',"")
        row=row.replace("', u'","  ");row=row.replace("')","  ")
        row=row.replace("'","");row=row.replace("  , uu","\n")
        row=row.replace(" \\u2013", "")
        count=count+1
        print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
conn = sqlite3.connect('news.db')
#conn = sqlite3.connect('testrss.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');

test01 = 'http://feeds.feedburner.com/TechCrunch/'
test02 = 'http://feeds.feedburner.com/crunchgear'
test03 = 'http://feeds.feedburner.com/TechCrunch/Twitter'
test04 = 'https://www.cnet.com/cnet-podcasts/'
test05 = 'https://www.cnet.com/rss/news/'
    
    
count=0
d = feedparser.parse(test04)
for post in d.entries:
    aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
    bb = `post.title + ": " + post.link + ""`
    conn = sqlite3.connect('newnews.db')
    c = conn.cursor()
    c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
    conn.commit()
    conn.close()
conn = sqlite3.connect('newnews.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
        row=str(row)
        row=row.replace("(u","");row=row.replace('", u"u',"\n")
        row=row.replace("/', u'","   ");row=row.replace('"',"")
        row=row.replace("', u'","  ");row=row.replace("')","  ")
        row=row.replace("'","");row=row.replace("  , uu","\n")
        row=row.replace(" \\u2013", "")
        count=count+1
        print"\nNumber :",count," -----\n",(row)

import sqlite3
import feedparser
import time
import sqlite3
conn = sqlite3.connect('news.db')
#conn = sqlite3.connect('testrss.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS bbctech
(head text, feed text)
''');

test01 = 'http://feeds.feedburner.com/TechCrunch/'
test02 = 'http://feeds.feedburner.com/crunchgear'
test03 = 'http://feeds.feedburner.com/TechCrunch/Twitter'
test04 = 'https://www.cnet.com/cnet-podcasts/'
test05 = 'https://www.cnet.com/rss/news/'
    
    
count=0
d = feedparser.parse(test05)
for post in d.entries:
    aa = `d['feed']['title'],d['feed']['link'],d.entries[0]['link']`
    bb = `post.title + ": " + post.link + ""`
    conn = sqlite3.connect('newnews.db')
    c = conn.cursor()
    c.execute("INSERT INTO bbctech VALUES (?,?)", (aa,bb))
    conn.commit()
    conn.close()
conn = sqlite3.connect('newnews.db')
c = conn.cursor()# Never 
for row in c.execute('SELECT * FROM bbctech ORDER BY rowid DESC'):
        row=str(row)
        row=row.replace("(u","");row=row.replace('", u"u',"\n")
        row=row.replace("/', u'","   ");row=row.replace('"',"")
        row=row.replace("', u'","  ");row=row.replace("')","  ")
        row=row.replace("'","");row=row.replace("  , uu","\n")
        row=row.replace(" \\u2013", "")
        count=count+1
        print"\nNumber :",count," -----\n",(row)

