# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import logging
from bson.binary import Binary
from base64 import b64encode
from PIL import Image
from io import BytesIO


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
            with open('./ur_images/{}'.format(image_path), 'rb') as image_file:
                byte_content = image_file.read()
            base64_bytes = b64encode(byte_content)
            return Binary(base64_bytes)

        if item['images']:
            # thumbnail
            path = './ur_images/{}'.format(item['images'][0]['path'])
            img = Image.open(path, mode='r')
            size = 150, 150
            img.thumbnail(size)
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            thumbnail_byte = buffer.getvalue()
            thumbnail_base64 = b64encode(thumbnail_byte)
            item['thumbnail'] = Binary(thumbnail_base64)

            # all images
            item['images'] = list(
                map(lambda x: encoded(x['path']), item['images']))

        del item['image_urls']

        self.db['use_cases'].insert_one(dict(item))
        # self.db[spider.name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item
