from marshmallow import Schema, fields
from base64 import b64encode


class Base64string(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        base64_bytes = b64encode(value)
        base64_string = base64_bytes.decode('utf-8')
        return base64_string


class UseCaseSchema(Schema):
    id = fields.String()
    images = fields.List(Base64string())
    main_image = Base64string()
    main_thumbnail = Base64string()

    class Meta:
        # fields = ('url', 'tags', 'content', 'image_urls', 'images')
        additional = ('provider', 'basic_info', 'content', 'status')
