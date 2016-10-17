import os
KEY = "414946656e776f6f34357166526852"
TYPE = 'json'
SERVICE = 'SearchSTNBySubwayLineService'
START_INDEX = '1'
END_INDEX = '10'
LINE_NUM = '2'
_url = 'http://openapi.seoul.go.kr:8088/'
url = _url+KEY+'/'+TYPE+'/'+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX+'/'+LINE_NUM
import requests
data = requests.get(url)
print(data.text)
