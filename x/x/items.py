# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    URL = scrapy.Field()
    description = scrapy.Field()
    cover_image = scrapy.Field()
    Available_sizes = scrapy.Field()
    image_in_full_size = scrapy.Field()
    pass
