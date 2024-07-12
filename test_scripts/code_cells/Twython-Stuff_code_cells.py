%%writefile /home/jack/hidden/xxAPIkey.py
def APIkey():
    #removed keys for privacy reasons
    CONSUMER_KEY = '123456'
    CONSUMER_SECRET = 'abcdefg'
    ACCESS_KEY = 'A large monkey in a cherry tree'
    ACCESS_SECRET = 'How to hide secrets'
    keys = (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    return keys

from xxAPIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

print(CONSUMER_KEY)
print(CONSUMER_SECRET)
print(ACCESS_KEY)
print(ACCESS_SECRET)

import twython
from twython import Twython
import time
import os
import sys
import shutil
from randtext import randTXT
#removed keys for privacy reasons
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Path to Image to be posted
PATH = "images/useresult.png"
timestr = time.strftime("%Y%m%d-%H%M%S")
#python program to check if a directory exists
savepath = "posted"
# Check whether the specified path exists or not
isExist = os.path.exists(savepath)
if not isExist:
    # Create a new directory because it does not exist
    os.makedirs(savepath)
    print("The new directory is created!")
# Every image posted will be copied into savepath with datetime string    
shutil.copy(PATH, "posted/"+timestr+".png")
# 1 , 2, 3, 12, 5, 15, 8, 6
#photo = open('/home/jack/Desktop/deep-dream-generator/notebooks/images/'+file_list[rnd]+'.jpg','rb')

photo = open(PATH,'rb')
#photo = open("images/waves1.gif","rb")
#response = twitter.upload_media(media=photo)
#twitter.update_status(status=STR, media_ids=[response['media_id']])
im = Image.open(PATH)
STR0 = randTXT()
STRu= STR0[:180]
print(STRu)
im

message ="Working with Python Mahotas. Mahotas is a computer vision and image processing library for Python. Mahotas currently has over 100 functions for image processing and computer vision and it keeps growing."

print (len(message))

from APIkey import APIkey
twitter = APIkey()[:3]
print(twitter)

import twython
from twython import Twython
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

def post(message):
    #twitter.update_status(status='See how easy using Twython is!')
    twitter.update_status(status=message)#, in_reply_to_status_id=twitter_id)


message ="""What a retired life I live. Playing Game of Thrones winter is coming. 
#GameOfThrones on the computer to my right. The computer in front I program process
images withPython and Tweet from my #Jupyternotebook"""
print(len(message))


post(message)

from twython
import Twython
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

photo = open('/path/to/file/image.jpg', 'rb')
response = twitter.upload_media(media = photo)
twitter.update_status(status = 'Checkout this cool image!', media_ids = [response['media_id']])

video = open('/path/to/file/video.mp4', 'rb')
response = twitter.upload_video(media = video, media_type = 'video/mp4')
twitter.update_status(status = 'Checkout this cool video!', media_ids = [response['media_id']])

response = twitter.upload_media(media=photo)
twitter.update_status(status=STRu, media_ids=[response['media_id']])

from twython import Twython, TwythonError
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

search_results = twitter.search(count=1, q='aiartcommunity')

try:
    for tweet in search_results['statuses']:
        print ('Tweet ID: ', tweet['id'])
except TwythonError as e:
    print(e)

status = twitter.show_status(id="1579675608816447488")
print(status)

def tweetstuff(STRINGS):
    tweetstuff = open("tweetstuff.txt", "a")
    tweetstuff.write(STRINGS)
works = status
works = str(works)
work = works.split("{")
cnt = 0
for lines in work:
    if len(lines)>3:
        cnt=cnt+1
        STRINGS = str(cnt)+": "+lines+"\n"
        tweetstuff(STRINGS)
        print (str(cnt),lines,"\n")


works = twitter.get_home_timeline()
works = status
works = str(works)
work = works.split("{")
cnt = 0
for lines in work:
    if len(lines)>3:
        cnt=cnt+1
        STRINGS = str(cnt)+": "+lines+"\n"
        tweetstuff(STRINGS)
        print (str(cnt),lines,"\n")

from twython import Twython
#twitter = Twython()
import datetime
from twython import Twython, TwythonError
from APIkey import APIkey
CONSUMER_KEY = APIkey()[0]
CONSUMER_SECRET = APIkey()[1]
ACCESS_KEY = APIkey()[2]
ACCESS_SECRET = APIkey()[3]

# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
results = twitter.cursor(twitter.search, q="#aiartcommunity", result_type='recent', count=25, tweet_mode='extended')

max_str_id = None
for _result in results:
    str_id = _result['id_str']
    #if str_id > max_str_id:
    #   max_str_id = str_id

    # if tweet_mode='extended', use _result['full_text']
    text = _result['text'] if 'text' in _result else _result['full_text']

    # check if is retweet
    is_retweet = True if 'retweeted_status' in _result or 'quoted_status' in _result else False

    # generate tweet url
    user_id = _result['user']['id_str']
    username = _result['user']['screen_name']
    post_id = _result['id_str']
    url = "https://twitter.com/{}/status/{}".format(username, post_id)

    # Mon Sep 24 03:35:21 +0000 2012
    created = datetime.datetime.strptime(_result['created_at'], '%a %b %d %H:%M:%S +0000 %Y')    

    # hashtags
    hashtags = [_hashtag['text'].lower() for _hashtag in _result['entities']['hashtags']]
    print(hashtags)
# you might want to save max_str_id if you plan to use since_id in next query.

def tweetstuff(STRINGS):
    tweetstuff = open("tweetstuff.txt", "a")
    tweetstuff.write(STRINGS)

print(len(results))



