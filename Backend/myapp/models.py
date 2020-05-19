from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, ListField, DictField, BooleanField, DateTimeField, ReferenceField, BinaryField, PULL
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
# from flask_security import UserMixin, RoleMixin

### CASES ###


class BasicInfo(EmbeddedDocument):
    applications = ListField(StringField(), required=True)
    company = StringField(required=True)
    industry = StringField(required=True)
    country = StringField(required=True)
    company_size = StringField(required=True)


class Content(EmbeddedDocument):
    article_title = StringField()
    article_sections = ListField(DictField())
    bullet_points = ListField(DictField())


class UseCase(Document):
    """Model for use-case"""
    meta = {'collection': 'use_cases',
            'indexes':
            ['basic_info.country', 'basic_info.industry', 'basic_info.applications']
            }
    options = ['active', 'inactive', 'draft']

    url = StringField()
    provider = StringField()
    basic_info = EmbeddedDocumentField(BasicInfo)
    content = EmbeddedDocumentField(Content)
    thumbnail = BinaryField()
    images = ListField(BinaryField())
    status = StringField(choices=options)


### USERS ###
# class Role(Document, RoleMixin):
    # name = StringField(max_length=80, unique=True)
    # description = StringField(max_length=300)


class User(Document):
    # class User(Document, UserMixin):
    """Model for user account"""
    meta = {'collection': 'users'}

    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    company_name = StringField(required=True)
    password = StringField(required=True, unique=True, max_length=200)
    use_cases = ListField(ReferenceField(
        'UseCase', reverse_delete_rule=PULL))
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
