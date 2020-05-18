# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScraperItem
from html_sanitizer import Sanitizer


class YaskawaSpider(CrawlSpider):
    name = 'yaskawa'
    allowed_domains = ['yaskawa.eu.com']
    # start_urls = ['https://www.yaskawa.eu.com/en/solutions/application/handling-assembly/',
    #                 'https://www.yaskawa.eu.com/en/solutions/application/painting/',
    #                 'https://www.yaskawa.eu.com/en/solutions/application/welding-cutting/',
    #                 'https://www.yaskawa.eu.com/en/solutions/application/packaging-palletising/']

    start_urls = ['https://www.yaskawa.eu.com/en/']

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'yaskawa.json',
        'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1,
                           'Scraper.pipelines.ScraperPipeline': 300,
                           'Scraper.pipelines.MongoPipeline': 400},
        'IMAGES_STORE': './yaskawa_images'
    }

    rules = (
        Rule(LinkExtractor(allow=r'application|industry'), follow=True),
        Rule(LinkExtractor(allow=r'case-studies'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # self.logger.info(response.url)

        sanitizer = Sanitizer()

        case = ScraperItem()

        # case['url'] = response.url
        case['basic_info'] = {}

        basic_info = response.xpath(
            "//div[@class='rightCol']/div//h2[contains(text(), 'Customer') or contains(text(), 'Industry') or contains(text(), 'Application')]")

        # headers = response.xpath('//h2[text()!="Pictures"]')

        if not basic_info:
            return

        for item in basic_info:
            key = item.xpath('./text()').get()
            value = (item.xpath(
                './following-sibling::*[not(self::h2)]//text()[normalize-space() != ""]').getall())

            if not value:
                value = item.xpath(
                    './parent::div/following-sibling::div[1]/ul/li/text()').getall()

            case['basic_info'].update({key: value})

        # item['images'] = []

        case['content'] = {}

        article_title = response.xpath(
            "//div[@id='sliderSmall']/h1/text()").get()

        article_sections = []

        section_titles = response.xpath(
            '//div[@class="floatLeft leftCol"]/div[1]/h2')

        for s in section_titles:
            title = s.xpath('.//text()').get().strip()
            # content = s.xpath('./following-sibling::*//text()[normalize-space() != ""]').getall()
            content = s.xpath('./following-sibling::*[1]').get()
            content = sanitizer.sanitize(content)
            article_sections.append({'title': title, 'content': content})
            # article_sections[title] = sanitizer.sanitize(content)

        case['content'].update(
            {'article_title': article_title, 'article_sections': article_sections})

        images = response.xpath('//div[@data-csc-images]//a/@href').getall()

        if not images:
            images = response.xpath(
                '//div[@data-csc-images]//img/@src').getall()

        case['image_urls'] = [response.urljoin(i) for i in images]

        return case
