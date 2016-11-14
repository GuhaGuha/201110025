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
import twitter
auth = twitter.oauth.OAuth(key['Access_Token'],key['Access_Token_Secret'],
                            key['Consumer_Key'], key['Consumer_Secret'])
_client = twitter.Twitter(auth=auth)
_client.statuses.update(status="Hello Twitter 1 1611090527")