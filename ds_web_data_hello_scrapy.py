import scrapy

class myItem(scrapy.item.Item):
    title = scrapy.item.Field()

class myCrawler(scrapy.spiders.CrawlSpider):
    name = 'myAppName'
    start_urls = ['https://data.go.kr']
    def parse(self, response):
        item = myItem()
        #title = scrapy.selector.Selector(response).xpath('//title/text()')
        title = scrapy.selector.Selector(response).css('title').extract()
        print "---Hello---", title
        item['title']=title
        return item