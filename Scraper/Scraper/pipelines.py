# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import logging
from bson.binary import Binary
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
            return Binary(byte_content)

        if item['images']:
            # thumbnail
            main_path = './ur_images/{}'.format(item['images'][0]['path'])
            img = Image.open(main_path, mode='r')
            ideal_ratio = 1.7778
            width = img.size[0]
            height = img.size[1]
            ratio = width/height
            if ratio > ideal_ratio:
                new_width = int(ideal_ratio*height)
                offset = (width - new_width) / 2
                resize = (offset, 0, width - offset, height)
            else:
                new_height = int(width / ideal_ratio)
                offset = (height - new_height) / 2
                resize = (0, offset, width, height - offset)
            img = img.crop(resize)
            size = 500, 500
            img.thumbnail(size)
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            thumbnail_byte = buffer.getvalue()
            item['main_thumbnail'] = Binary(thumbnail_byte)

            # all images
            item['images'] = list(
                map(lambda x: encoded(x['path']), item['images']))

            item['main_image'] = item['images'].pop(0)

        del item['image_urls']

        self.db['use_cases'].insert_one(dict(item))
        # self.db[spider.name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item
