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
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul', 'count' : 200, 'since_id':'754295227351871489'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)
f=open('ds_twitter_4.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    j = json.dumps([str(i),tweet['id'],tweet['text']])
    f.write(j)
    f.write("\n")
f.close()