# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import logging
from base64 import b64encode


class ScraperPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    # collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        def encoded(image_path):
            with open('../ur_images/{}'.format(image_path), 'rb') as image_file:
                # result of reading a file -> bytes
                byte_content = image_file.read()
            # result of b64 encoding -> bytes again
            base64_bytes = b64encode(byte_content)
            # result -> decoding bytes to utf-string
            base64_string = base64_bytes.decode('utf-8')
            return base64_string

        # self.db[self.collection_name].insert_one(dict(item))
        del item['image_urls']
        item['images'] = list(
            map(lambda x: encoded(x['path']), item['images']))
        self.db[spider.name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item
