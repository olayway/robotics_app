from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, ListField, DictField
from werkzeug.security import generate_password_hash, check_password_hash

### CASES ###

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
    """Model for use-case"""
    meta = {'collection': 'universal',
            'indexes': 
            ['tags.country', 'tags.industry', 'tags.applications']
            }
    
    url = StringField(max_length=5)
    tags = EmbeddedDocumentField(FilterTags, db_field='filter_tags')
    content = EmbeddedDocumentField(Content)
    image_urls = ListField(StringField())
    images = ListField(EmbeddedDocumentField(Images))


### USERS ###

class User(Document):
    """Model for user account"""
    meta = {'collection': 'users'}

    username = StringField(required=True, unique=True)
    password = StringField(required=True, unique=True, max_length=200)
    email = StringField(required=True, unique=True)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return 'User {}'.format(self.username)
    








