from marshmallow import Schema, fields


class UseCaseSchema(Schema):
    id = fields.String()
    images = fields.List(fields.String())
    thumbnail = fields.String()

    class Meta:
        # fields = ('url', 'tags', 'content', 'image_urls', 'images')
        additional = ('provider', 'basic_info', 'content')
