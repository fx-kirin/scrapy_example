# -*- coding: utf-8 -*-

import scrapy

class StockItem(scrapy.Item):
    name = scrapy.Field()
    stock_id = scrapy.Field()