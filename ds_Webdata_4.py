import urllib
keyword = '눈오는'
f=urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&target=track")
mydata = f.read()
pos = mydata.find("트랙 리스트")
pos1 = mydata.find("_title title NPI=",pos)
mydata.find("title=", pos+20)
import re
p=re.compile('title=".*눈.?오는.*"')
#res=p.search(data)
res=p.findall(mydata)
for item in res:
    print item