from mongoengine import *
from wtforms import Form, BooleanField, StringField, validators

class FilterTags(EmbeddedDocument):
    applications = ListField(StringField(), required=True)
    company = StringField(required=True)
    industry = StringField(required=True)
    country = StringField(required=True)
    company_size = StringField(required=True)

class Content(EmbeddedDocument):
    title = StringField(db_field='article_title')
    sections = DictField(db_field='article_sections')
    bullets = DictField(db_field='bullet_points')

class Images(EmbeddedDocument):
    url = StringField()
    path = StringField()
    checksum = StringField()

class UseCase(Document):
    meta = {'collection': 'universal',
            'indexes': [{'fields': ['$tags.country', '$tags.industry', '$tags.applications']}]}
    
    url = StringField(max_length=5)
    tags = EmbeddedDocumentField(FilterTags, db_field='filter_tags')
    content = EmbeddedDocumentField(Content)
    image_urls = ListField(StringField())
    images = ListField(EmbeddedDocumentField(Images))


###### USER AUTH ######

class User(Document):
    meta = {'collection': 'users'}
    username = StringField(required=True, unique=True)
    password = StringField(required=True, unique=True)
    # first_name = StringField(required=True)
    # last_name = StringField(required=True, unique_with=first_name)
    email = StringField(required=True, unique=True)
    created = DateTimeField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return True
        # should return a unicode that uniquely identifies the user, 
        # and can be used to load the user from the user_loader callback

##### REGISTRATION FORM ######

class RegForm(Form):
    username = StringField('Username', [validators.Length(min=5, max=20)])
    password = StringField('Password', [validators.Length(min=8, max=20)])
    # first_name = StringField('First Name', [validators.Length(min=2, max=20)])
    # last_name = StringField('Last Name', [validators.Length(min=2, max=20)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    # accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])








