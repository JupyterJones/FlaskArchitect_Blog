!pwd

from TwitterAPI import TwitterAPI

data_in = open("Tweetsfull.txt","w")
data_in.close()

data_in = open("Tweetsfull.txt","a")
from APIkey import APIkey
consumer_key=APIkey()[0]
consumer_secret=APIkey()[1]
access_token_key=APIkey()[2]
access_token_secret=APIkey()[3]
from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', {'q':'Trump',
        'query':'Ukrain',
        'tweet.fields':'author_id',
        'expansions':'author_id'})
for item in r:
        print(item)
        data_in.write("______________________________")
        data_in.write(str(item))
        data_in.write("______________________________")

data_in = open("Tweets.txt","a")
from APIkey import APIkey
consumer_key=APIkey()[0]
consumer_secret=APIkey()[1]
access_token_key=APIkey()[2]
access_token_secret=APIkey()[3]
from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
r = api.request('search/tweets', {'q':'freedom'})
for item in r:
        text = item['text']
        #name = item['screen_name']
        #data_in.write(name)
        data_in.write(text)
        print(text,"\n")


from APIkey import APIkey
APIkey()[0]
APIkey()[1]
APIkey()[2]
APIkey()[3]

text = my_dict['text']

import os
from twython import Twython
from APIkey import APIkey
# Election Democrates Republicans 
SEARCH = 'Republicans'
filename = SEARCH+'_TwitterTwython.txt'
if os.path.exists(filename):
    append_write = 'a' # append if already exists
else:
    append_write = 'w' # make a new file if not
dData = open(filename,append_write)
APP_KEY = APIkey()[0]
APP_SECRET = APIkey()[1]
twitter= Twython(app_key=APP_KEY,app_secret=APP_SECRET)
for status in twitter.search(q= SEARCH ,count =100)["statuses"]:
    user =status["user"]["screen_name"].encode('utf-8')
    text =status["text"]
    data = "{0} {1} {2}".format(user ,text,'\n')
    print(data)
    dData.write(data)
dData.close()    



