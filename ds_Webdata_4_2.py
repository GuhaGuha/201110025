import lxml.html
from lxml.cssselect import CSSSelector
import lxml.html
import requests

keyword='눈오는'
r = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")

_html = lxml.html.fromstring(r.text)
sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
results = sel(_html)
_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
for item in results:
    #print lxml.html.tostring(item)
    _name=_selName(item)
    _artist=_selArtist(item)
    _album=_selAlbum(item)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content()