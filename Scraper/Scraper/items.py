# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    url = scrapy.Field()
    challenge = scrapy.Field()
    solution = scrapy.Field()
    results = scrapy.Field()
    customer = scrapy.Field()
    product = scrapy.Field()
    industry = scrapy.Field()
    applications = scrapy.Field()
    components = scrapy.Field()
