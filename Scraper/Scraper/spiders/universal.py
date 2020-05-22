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
        # 'FEED_FORMAT': 'json',
        # 'FEED_URI': 'universal_robots.json',
        'ITEM_PIPELINES': {'scrapy.pipelines.images.ImagesPipeline': 1,
                           'Scraper.pipelines.ScraperPipeline': 300,
                           'Scraper.pipelines.MongoPipeline': 400},
        'IMAGES_STORE': './ur_images'
    }

    def parse(self, response):

        cases = response.xpath("//a[@class='iconteaser']")

        for case in cases:

            applications = case.xpath('./p[2]/text()').get().split(",")
            applications = [value.lower() for value in applications]
            url_relative = case.xpath('./@href').get()
            url = urljoin(response.url, url_relative)

            yield scrapy.Request(url, callback=self.parse_case, meta={'applications': applications})

    def parse_case(self, response):

        sanitizer = Sanitizer()

        case = ScraperItem()

        case['provider'] = 'Universal Robots'
        case['basic_info'] = {}
        case['basic_info'].update(
            {'applications': response.meta['applications']})

        basic_info = response.xpath('//div[@class="hero-info"]/div/div')

        for item in basic_info:
            key, value = item.xpath('./span/text()').getall()
            key = key.strip().replace(" ", "_").lower()
            value = value.strip().lower()
            if key == 'company':
                key = 'customer'
            case['basic_info'].update({key: value})

        case['content'] = {}

        article_title = response.xpath(
            '//span[@class="title title--narrow"]/text()').get()

        article_sections = []

        section_titles = response.xpath(
            '//h3[@class="titlelabel grid-gap1-below" and normalize-space()!=""]')

        for s in section_titles:
            title = s.xpath('.//text()[2]').get().strip()
            # content = s.xpath('./following-sibling::*//text()[normalize-space() != ""]').getall()
            content = s.xpath('./following-sibling::*').getall()
            content = [sanitizer.sanitize(value) for value in content]
            article_sections.append({'title': title, 'content': content})
            # article_sections[title] = list(
            #     map(lambda x: sanitizer.sanitize(x), content))

        bullet_points = []

        bullet_titles = response.xpath('//section[@class="contentbox"]')

        for b in bullet_titles:
            title = b.xpath('./span/text()').get()
            content = b.xpath('./ul').get()
            content = sanitizer.sanitize(content)
            bullet_points.append({'title': title, 'content': content})
            # bullet_points[title] = sanitizer.sanitize(content)

        case['content'].update({'article_title': article_title,
                                'article_sections': article_sections, 'bullet_points': bullet_points})

        images = response.xpath(
            '//div[@class="grid-span10 grid-shift1"]//img/@src').getall()

        case['image_urls'] = [response.urljoin(i) for i in images]
        case['status'] = 'active'

        return case
