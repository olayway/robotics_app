import click 
from flask.cli import with_appcontext

from .extensions import db
from .models import *


@click.command('add-usecase')
@click.argument('url')
@click.argument('filter_tags')
@with_appcontext
def add_usecase(url, filter_tags=None):
    test = UseCase(url=url, filter_tags=filter_tags)
    test.other = 'other'
    test.save()
    click.echo("SUCCESS")