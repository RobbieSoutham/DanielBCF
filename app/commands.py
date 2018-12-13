import os
import click
from getpass import getpass
from flask import Flask
from flask.cli import AppGroup

from . import app
from .database.user import User
from . import PATH, CONFIG


db_cli = AppGroup('db')
app.cli.add_command(db_cli)

user_cli = AppGroup('user')
app.cli.add_command(user_cli)

@db_cli.command('init')
def initdb():
    os.system("""
    cd app &&
    cat {}/database/schema.sql |
    yasha -v {} - |
    mysql -uroot
    """.format(PATH, CONFIG))

@user_cli.command("create")
@click.argument('email')
def create_user(**values):
    values['first_name'] = raw_input("Enter first name: ")
    values['surname'] = raw_input("Enter surname: ")
    values['password'] = getpass("Enter password (hidden): ")
    User.new_user(**values)
    print("{} created.".format(values['email']))


@user_cli.command("delete")
@click.argument('email')
def delete_user(email):
    User.delete_user(email)
    print("{} deleted.".format(email))

@user_cli.command("details")
@click.argument('email')
def delete_user(email):
    user = User(email)
    print(
"""\
email: {}
first_name: {}
surname: {}
verification: {}
password: {} """.format(
        user.email, user.first_name, user.surname,
        user.verified, user.password
    ))
    
