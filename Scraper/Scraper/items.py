# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # url = scrapy.Field()
    provider = scrapy.Field()
    basic_info = scrapy.Field()
    content = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    status = scrapy.Field()
    main_image = scrapy.Field()
    main_thumbnail = scrapy.Field()
