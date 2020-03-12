from mongoengine import *

class UseCase(DynamicDocument):
    url = URLField(max_length=100)
    filter_tags = StringField()
    # content = DictField()
    # images = ListField(DictField())