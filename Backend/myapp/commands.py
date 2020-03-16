import click 
from flask.cli import with_appcontext
from mongoengine.context_managers import switch_collection
from .models import UseCase


@click.command('add-usecase')
@click.argument('url')
@with_appcontext
def add_usecase(url):
    with switch_collection(UseCase, 'test_collection'):
        UseCase(url=url).save()
        click.echo("SUCCESS")
