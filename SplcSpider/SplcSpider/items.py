# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SplcspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HzInternetCourtFaYuan(scrapy.Item):
    title = scrapy.Field()
    courtName = scrapy.Field()
    caseCode = scrapy.Field()
    trialName = scrapy.Field()
    prosecutionStr = scrapy.Field()
    defendantStr = scrapy.Field()
    causeAction = scrapy.Field()
    status = scrapy.Field()
