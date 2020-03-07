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
        'ITEM_PIPELINES' : {'scrapy.pipelines.images.ImagesPipeline': 1,
                            'Scraper.pipelines.ScraperPipeline': 300,
                            'Scraper.pipelines.MongoPipeline': 400},
        'IMAGES_STORE' : './yaskawa_images'
    }

    rules = (
        Rule(LinkExtractor(allow=r'application|industry'), follow=True),
        Rule(LinkExtractor(allow=r'case-studies'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # self.logger.info(response.url)
        case = ScraperItem()

        case['url'] = response.url
        case['filter_tags'] = {}

        filter_tags = response.xpath("//div[@class='rightCol']/div//h2[contains(text(), 'Customer') or contains(text(), 'Industry') or contains(text(), 'Application')]")

        # headers = response.xpath('//h2[text()!="Pictures"]')

        if not filter_tags:
            return

        for t in filter_tags:
            title = t.xpath('./text()').get()
            text = t.xpath('./following-sibling::*[not(self::h2)]//text()[normalize-space() != ""]').getall()

            if not text:
                text = h.xpath('./parent::div/following-sibling::div[1]/ul/li/text()').getall()

            case['filter_tags'].update({title: text})

        # item['images'] = []

        case['content'] = {}

        article_title = response.xpath("//div[@id='sliderSmall']/h1/text()").get()

        article_sections = {}
        
        section_titles = response.xpath('//div[@class="floatLeft leftCol"]/div[1]/h2')

        for s in section_titles:
            title = s.xpath('.//text()').get().strip()
            # text = s.xpath('./following-sibling::*//text()[normalize-space() != ""]').getall()
            text = s.xpath('./following-sibling::*[1]').get()
            article_sections[title] = text

        case['content'].update({'Article_title': article_title, 'Article_sections': article_sections})

        images = response.xpath('//div[@data-csc-images]//a/@href').getall()

        if not images:
            images = response.xpath('//div[@data-csc-images]//img/@src').getall()

        case['image_urls'] = [response.urljoin(i) for i in images]

        return case
