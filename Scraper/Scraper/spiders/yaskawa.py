# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScraperItem

class YaskawaSpider(CrawlSpider):
    name = 'yaskawa'
    allowed_domains = ['yaskawa.eu.com']
    start_urls = ['https://www.yaskawa.eu.com/en/solutions/application/handling-assembly/']

    custom_settings = {
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'yaskawa.json',
        # 'ITEM_PIPELINES' : {'scrapy.pipelines.images.ImagesPipeline': 1},
        # 'IMAGES_STORE' : '/Users/Ola/Documents/scrapy_learning/amazon/amazon/images'
    }

    rules = (
        Rule(LinkExtractor(allow=r'case-studies'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # self.logger.info(response.url)
        # item = ScraperItem()

        item = {}
        item['url'] = response.url

        headers = response.xpath('//h2')

        for h in headers:
            title = h.xpath('./text()').get()
            content = h.xpath('./following-sibling::ul//*/text()').getall()
            item[title] = content


        return item
