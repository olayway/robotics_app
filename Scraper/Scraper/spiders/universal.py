# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from ..items import ScraperItem
from html_sanitizer import Sanitizer


class UniversalSpider(scrapy.Spider):
    name = 'universal'
    allowed_domains = ['universal-robots.com']
    start_urls = ['https://www.universal-robots.com/case-stories/']

    custom_settings = {
        'FEED_FORMAT' : 'json',
        'FEED_URI' : 'universal_robots.json',
        'ITEM_PIPELINES' : {'scrapy.pipelines.images.ImagesPipeline': 1,
                            'Scraper.pipelines.ScraperPipeline': 300,
                            'Scraper.pipelines.MongoPipeline': 400},
        'IMAGES_STORE' : './ur_images'
    }    

    def parse(self, response):
        
        cases = response.xpath("//a[@class='iconteaser']")

        for c in cases:

            applications = c.xpath('./p[2]/text()').get().split(",")
            url_relative = c.xpath('./@href').get()
            url = urljoin(response.url, url_relative)

            yield scrapy.Request(url, callback=self.parse_case, meta={'applications': applications})
    
    def parse_case(self, response):

        sanitizer = Sanitizer()

        case = ScraperItem()
        
        case['url'] = response.url

        case['filter_tags'] = {}
        case['filter_tags'].update({'applications': response.meta['applications']})

        filter_tags = response.xpath('//div[@class="hero-info"]/div/div')

        for tag in filter_tags:
            title, text = tag.xpath('./span/text()').getall()
            title = title.strip().replace(" ", "_").lower()
            text = text.strip()
            case['filter_tags'].update({title: text})


        case['content'] = {}

        article_title = response.xpath('//span[@class="title title--narrow"]/text()').get()

        # article_sections = response.xpath('//*[@class="grid-outer-container item item--UR2StepText"]')

        # for s in article_sections:
        #     title = s.xpath('(.//h3/span[2]/text() | .//h3/text()[normalize-space() != ""])').get().strip()
        #     content = s.xpath('.//p//text()').getall()
        #     item[title] = content   

        article_sections = {}
        
        section_titles = response.xpath('//h3[@class="titlelabel grid-gap1-below" and normalize-space()!=""]')

        for s in section_titles:
            title = s.xpath('.//text()[2]').get().strip()
            # text = s.xpath('./following-sibling::*//text()[normalize-space() != ""]').getall()
            content = s.xpath('./following-sibling::*').getall()
            article_sections[title] = list(map(lambda x: sanitizer.sanitize(x), content)) 


        bullet_points = {}

        bullet_tiles = response.xpath('//section[@class="contentbox"]')

        for t in bullet_tiles:
            title = t.xpath('./span/text()').get()
            points = t.xpath('./ul').get()
            bullet_points[title] = sanitizer.sanitize(points)


        case['content'].update({'article_title': article_title, 'article_sections': article_sections, 'bullet_points': bullet_points})

        images = response.xpath('//div[@class="grid-span10 grid-shift1"]//img/@src').getall()

        case['image_urls'] = [response.urljoin(i) for i in images]

        return case

