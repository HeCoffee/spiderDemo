# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderdemoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    company = scrapy.Field()
    failAt = scrapy.Field()
    failReason = scrapy.Field()
    pass
