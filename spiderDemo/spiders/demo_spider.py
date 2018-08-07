#_*_coding:utf-8_*_
import scrapy

from spiderDemo.items import SpiderdemoItem

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["demo.org"]
    start_urls = [
        "http://www.dailuopan.com/black/all"
    ]

    def parse(self, response):

        def jsonStr(itemStr) :
            new_str = itemStr[0] if len(itemStr) else ""
            return new_str

        for sel in response.css('#shujuList_table tbody tr'):
            item = SpiderdemoItem()
            item['name'] = jsonStr(sel.css('.td1 a::text').extract())
            item['url'] = jsonStr(sel.css('td:nth-child(2)::text').extract())
            item['province'] = jsonStr(sel.css('td:nth-child(3)::text').extract())
            item['city'] = jsonStr(sel.css('td:nth-child(4)::text').extract())
            item['company'] = jsonStr(sel.css('td:nth-child(5)::text').extract())
            item['failAt'] = jsonStr(sel.css('td:nth-child(7)::text').extract())
            item['failReason'] = jsonStr(sel.css('td:nth-child(6)::text').extract())
            yield item
