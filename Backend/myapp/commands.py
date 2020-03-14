import click 
from flask.cli import with_appcontext

from .models import *


@click.command('add-usecase')
@click.argument('country')
@with_appcontext
def add_usecase(country):
    test = UseCase(country=country)
    test.other = 'other'
    test.save()
    print(UseCase)
    click.echo("SUCCESS")