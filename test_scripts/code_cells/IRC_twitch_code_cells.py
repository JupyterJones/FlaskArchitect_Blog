#server = 'irc.chat.twitch.tv'
#port = 6667
server="irc.deft.com"
port=6667
nickname = 'jahral'
channel = '#experiments'

import socket

sock = socket.socket()

sock.connect((server, port))

#sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')

resp

#sock.close()

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

logging.info(resp)

#!pip install emoji 

from emoji import demojize

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:
        logging.info(demojize(resp))

import datetime
print (datetime.datetime.now())
print(datetime.date.today())



dt = datetime.datetime.now()

print(dt.strftime('%Y-%m-%d_%H:%M:%S'))
timenow=dt.strftime('%Y-%m-%d_%H:%M:%S')
print(timenow)

from datetime import datetime

time_logged = msg.split()[0].strip()
time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')
time_logged

#msg = '2018-12-10_11:26:40 — :spappygram!spappygram@spappygram.tmi.twitch.tv PRIVMSG #ninja :Chat, let Ninja play solos'
msg = timenow+" :jack PRIVMSG #experiments :Chat, let the games begin"
print (msg)

username_message = msg.split('—')[1:]
username_message = '—'.join(username_message).strip()

username_message

import re

username, channel, message = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message).groups()

print(f"Channel: {channel} \nUsername: {username} \nMessage: {message}")

import pandas as pd

def get_chat_dataframe(file):
    data = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n\n\n')
        
        for line in lines:
            try:
                time_logged = line.split('—')[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                username_message = line.split('—')[1:]
                username_message = '—'.join(username_message).strip()

                username, channel, message = re.search(
                    ':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message
                ).groups()

                d = {
                    'dt': time_logged,
                    'channel': channel,
                    'username': username,
                    'message': message
                }

                data.append(d)
            
            except Exception:
                pass
            
    return pd.DataFrame().from_records(data)
        
    
df = get_chat_dataframe('chat.log')

df.set_index('dt', inplace=True)

print(df.shape)

df.head()

