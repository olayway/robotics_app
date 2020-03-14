from mongoengine import *
from .extensions import db

class FilterTags(db.EmbeddedDocument):
    applications = db.ListField(StringField(max_length=20), required=True)
    company = db.StringField(max_length=20, required=True)
    industry = db.StringField(max_length=20, required=True)
    country = db.StringField(max_length=20, required=True)
    company_size = db.StringField(max_length=20, required=True)

class Content(db.EmbeddedDocument):
    article_title = db.StringField(max_length=30)
    article_sections = db.DictField()
    bullet_points = db.DictField()

class UseCase(db.Document) :
    meta = {'collection': 'universal'}
    
    url = db.StringField(max_length=25, required=True)

    filter_tags = db.EmbeddedDocumentField(FilterTags)
    content = db.EmbeddedDocumentField(Content)

    image_urls = ListField()
    images = ListField()








