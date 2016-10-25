import lxml.html
from lxml.cssselect import CSSSelector
import requests

r = requests.get('https://www.ieee.org/conferences_events/index.html')
html = lxml.html.fromstring(r.text)

c=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div a')
nodes = sel(html)

nodes = c(html)
for node in nodes:
    print node.text