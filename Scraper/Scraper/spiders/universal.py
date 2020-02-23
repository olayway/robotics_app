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
        'IMAGES_STORE' : '../ur_images'
    }    


    rules = (
        Rule(LinkExtractor(allow=r'case-stories', restrict_css='.iconteaser'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # self.logger.info(response.url)
        item = {}
        item['url'] = response.url

        main_tags = response.xpath('//div[@class="hero-info"]/div/div')

        for tag in main_tags:
            title, text = tag.xpath('./span/text()').getall()
            item[title.strip()] = text.strip()

        item['article_title'] = response.xpath('//span[@class="title title--narrow"]/text()').get()

        # article_sections = response.xpath('//*[@class="grid-outer-container item item--UR2StepText"]')

        # for s in article_sections:
        #     title = s.xpath('(.//h3/span[2]/text() | .//h3/text()[normalize-space() != ""])').get().strip()
        #     content = s.xpath('.//p//text()').getall()
        #     item[title] = content   

        article_sections = response.xpath('//h3[@class="titlelabel grid-gap1-below" and normalize-space()!=""]')

        for s in article_sections:
            title = s.xpath('.//text()[2]').get().strip()
            content = s.xpath('./following-sibling::*//text()[normalize-space() != ""]').getall()
            item[title] = content   

        bullet_sections = response.xpath('//section[@class="contentbox"]')

        for b in bullet_sections:
            title = b.xpath('./span/text()').get()
            content = b.xpath('.//li/text()').getall()
            item[title] = content

        images = response.xpath('//div[@class="grid-span10 grid-shift1"]//img/@src').getall()

        item['image_urls'] = [response.urljoin(i) for i in images]

        return item
