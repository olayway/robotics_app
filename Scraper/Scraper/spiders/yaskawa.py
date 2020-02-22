# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScraperItem

class YaskawaSpider(CrawlSpider):
    name = 'yaskawa'
    allowed_domains = ['yaskawa.eu.com']
    # start_urls = ['https://www.yaskawa.eu.com/en/solutions/application/handling-assembly/',
    #                 'https://www.yaskawa.eu.com/en/solutions/application/painting/',
    #                 'https://www.yaskawa.eu.com/en/solutions/application/welding-cutting/',
    #                 'https://www.yaskawa.eu.com/en/solutions/application/packaging-palletising/']

    start_urls = ['https://www.yaskawa.eu.com/en/']

    custom_settings = {
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'yaskawa.json',
        'ITEM_PIPELINES' : {'scrapy.pipelines.images.ImagesPipeline': 1},
        'IMAGES_STORE' : '../images'
    }

    rules = (
        Rule(LinkExtractor(allow=r'application|industry'), follow=True),
        Rule(LinkExtractor(allow=r'case-studies'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # self.logger.info(response.url)
        # item = ScraperItem()

        item = {}
        item['url'] = response.url

        headers = response.xpath('//h2[text()!="Pictures"]')

        for h in headers:
            title = h.xpath('./text()').get()
            content = h.xpath('./following-sibling::*[not(self::h2)]//text()[normalize-space() != ""]').getall()

            if not content:
                content = h.xpath('./parent::div/following-sibling::div[1]/ul/li/text()').getall()

            item[title] = [i.strip() for i in content]

        # item['images'] = []

        images = response.xpath('//div[@data-csc-images]//a/@href').getall()

        if not images:
            images = response.xpath('//div[@data-csc-images]//img/@src').getall()

        item['image_urls'] = [response.urljoin(i) for i in images]

        return item
