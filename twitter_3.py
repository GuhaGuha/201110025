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
url1 = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)

for i,tweet in enumerate(tsearch_json['statuses']):
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])