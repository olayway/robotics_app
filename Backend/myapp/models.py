from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, ListField, DictField, BooleanField, DateTimeField, ReferenceField, BinaryField
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
# from flask_security import UserMixin, RoleMixin

### CASES ###


class FilterTags(EmbeddedDocument):
    applications = ListField(StringField(), required=True)
    company = StringField(required=True)
    industry = StringField(required=True)
    country = StringField(required=True)
    company_size = StringField(required=True)


class Content(EmbeddedDocument):
    # title = StringField(db_field='article_title')
    # sections = DictField(db_field='article_sections')
    # bullets = DictField(db_field='bullet_points')
    article_title = StringField()
    article_sections = ListField(DictField())
    # article_sections = DictField()
    bullet_points = ListField(DictField())
    # bullet_points = DictField()


class Images(EmbeddedDocument):
    url = StringField()
    path = StringField()
    checksum = StringField()
    blob = BinaryField()


class UseCase(Document):
    """Model for use-case"""
    meta = {'collection': 'universal',
            'indexes':
            ['filter_tags.country', 'filter_tags.industry', 'filter_tags.applications']
            }
    options = ['active', 'inactive', 'draft']

    url = StringField()
    filter_tags = EmbeddedDocumentField(FilterTags)
    content = EmbeddedDocumentField(Content)
    image_urls = ListField(StringField())
    images = ListField(EmbeddedDocumentField(Images))
    status = StringField(choices=options)

    # meta = {'collection': 'universal',
    #         'indexes':
    #         ['tags.country', 'tags.industry', 'tags.applications']
    #         }
    # options = ['active', 'inactive', 'draft']

    # url = StringField()
    # tags = EmbeddedDocumentField(FilterTags)
    # content = EmbeddedDocumentField(Content)
    # image_urls = ListField(StringField())
    # images = ListField(EmbeddedDocumentField(Images))
    # status = StringField(choices=options)


### USERS ###
# class Role(Document, RoleMixin):
    # name = StringField(max_length=80, unique=True)
    # description = StringField(max_length=300)


class User(Document):
    # class User(Document, UserMixin):
    """Model for user account"""
    meta = {'collection': 'users'}

    username = StringField(required=True, unique=True)
    password = StringField(required=True, unique=True, max_length=200)
    email = StringField(required=True, unique=True)
    use_cases = ListField(ReferenceField(UseCase))
    active = BooleanField(default=True)
    # confirmed_at = DateTimeField()
    # roles = ListField(ReferenceField(Role), default=[]) # ? default

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.username = kwargs['username']
    #     self.password = generate_password_hash(
    #                         kwargs['password'],
    #                         method='sha256'
    #                     )

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def to_dict(self):
        return dict(id=self.id, username=self.username)

    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        print(username)
        print(password)
        try:
            user = cls.objects.get(username=username)
            print('user exists')
            print(user.password)
            print(password)
            auth = check_password_hash(user.password, password)
            print(auth)
            if auth:
                print('correct credentials')
                return user
            print('invalid password')
        except:
            print('exception')

        return None
