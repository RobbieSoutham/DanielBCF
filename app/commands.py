import os
import click
from getpass import getpass
from flask import Flask
from flask.cli import AppGroup

from . import app
from .database.user import User

@app.cli.command()
def initdb():
    os.system("cd app && cat schema.sql | yasha -v config.yaml - | mysql -uroot")
    

@app.cli.command("create_user")
@click.argument('email')
def create_user(**values):
    values['first_name'] = raw_input("Enter first name: ")
    values['surname'] = raw_input("Enter surname: ")
    values['password'] = getpass("Enter password (hidden): ")
    User.new_user(**values)
    print("{} created.".format(values['email']))

@app.cli.command("delete_user")
@click.argument('email')
def delete_user(email):
    User.delete_user(email)
    print("{} deleted.".format(email))


