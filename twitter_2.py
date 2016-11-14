import oauth2 as oauth
import os
import json
import urllib
keyPath="C:/Users/DB400T2A/Documents/src/key.properties"
f=open(keyPath,'r')
lines = f.readlines()
def getKey(keyPath):
    d=dict()
    for line in lines:
        row = line.split('=')
        d[row[0]]=row[1].strip()
    return d
key = getKey(keyPath)
keyPath=os.path.join(os.path.expanduser("~"),'Code/git/bb/sd','twitter4j.properties')
consumer = oauth.Consumer(key=key['Consumer_Key'], secret=key['Consumer_Secret'])
token=oauth.Token(key=key['Access_Token'], secret=key['Access_Token_Secret'])
client = oauth.Client(consumer, token)
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'In Python'})
response,content=client.request(url,method='POST',body=mybody)

url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 1611090528'})
response,content=client.request(url,method='POST',body=mybody)
import io
with io.open('documents/src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)
from pymongo import MongoClient
_mclient=MongoClient()
_mclient['ds_twitter']
_db=_mclient.ds_twitter
_col=_db.home_timeline
client = oauth.Client(consumer, token)
url="https://api.twitter.com/1.1/statuses/home_timeline.json"
response,content = client.request(url)
home_timeline=json.loads(content)
for tweet in home_timeline:
    print tweet['id'],tweet['text']
    _col.insert_one(tweet)