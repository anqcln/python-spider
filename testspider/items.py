# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    xinzi = scrapy.Field()
    gongsi = scrapy.Field()
    weizhi = scrapy.Field()
    zige = scrapy.Field()
    fuli = scrapy.Field()
    zhize = scrapy.Field()
    url = scrapy.Field()
