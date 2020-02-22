# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UniversalSpider(CrawlSpider):
    name = 'universal'
    allowed_domains = ['universal-robots.com']
    start_urls = ['https://www.universal-robots.com/case-stories/']

    custom_settings = {
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'universal_robots.json',
        'ITEM_PIPELINES' : {'scrapy.pipelines.images.ImagesPipeline': 1},
        'IMAGES_STORE' : '../images'
    }    


    rules = (
        Rule(LinkExtractor(allow=r'case-stories', restrict_css='.iconteaser'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info(response.url)
        item = {}
        item['url'] = response.url

        main_tags = response.xpath('//div[@class="hero-info"]/div/div')

        for tag in main_tags:
            title, text = tag.xpath('./span/text()').getall()
            item[title] = text.strip()
        return item
