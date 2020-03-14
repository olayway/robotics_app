from marshmallow import Schema, fields

class UseCaseSchema(Schema):
    id = fields.String()

    class Meta:
        # fields = ('url', 'filter_tags', 'content', 'image_urls', 'images')
        additional = ('url', 'filter_tags')
