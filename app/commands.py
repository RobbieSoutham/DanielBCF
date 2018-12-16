import os
import click
from getpass import getpass
from flask import Flask
from flask.cli import AppGroup

from . import app
from .database.user import User
from .database.product import Product
from .database.stock import Stock
from .database.sites import Sites

from . import PATH, CONFIG


db_cli = AppGroup('db')
app.cli.add_command(db_cli)

user_cli = AppGroup('user')
app.cli.add_command(user_cli)

product_cli = AppGroup('product')
app.cli.add_command(product_cli)

stock_cli = AppGroup('stock')
app.cli.add_command(stock_cli)

sites_cli = AppGroup('sites')
app.cli.add_command(sites_cli)

#DB commands
@db_cli.command('init')
def initdb():
    os.system("""
    cd app &&
    cat {}/database/schema.sql |
    yasha -v {} - |
    mysql -uroot
    """.format(PATH, CONFIG))


#Product commands
@product_cli.command("create")
@click.argument('id')
def create_product(**values):
    values['name'] = raw_input("Enter the name: ")
    values['order_qty'] = raw_input("Enter the order quantity: ")
    Product.new_product(**values)
    print("{} created.".format(values['id']))

@product_cli.command("delete")
@click.argument('id')
def delete_product(id):
    Product.delete_product(id)
    print("{} deleted.".format(id))

@product_cli.command("details")
@click.argument('id')
def product_details(id):
    product = Product(id)
    print(
"""\
id: {}
name: {}
order quantity: {} """.format(
        product.id, product.name, product.order_qty
    ))


#User commands
@user_cli.command("create")
@click.argument('email')
def create_user(email, **values):
    values['email'] = email
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
def user_details(email):
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


#Stock commands
@stock_cli.command("create")
@click.argument('id')
def create_stock(**values):
    values['product_id'] = raw_input("Enter the product ID: ")
    values['site_id'] =  raw_input("Enter the site ID: ")
    Stock.new_stock(**values)
    print("{} created.".format(values['id']))


@stock_cli.command("delete")
@click.argument('id')
def delete_stock(id):
    Stock.delete_stock(id)
    print("{} deleted.".format(id))

@stock_cli.command("details")
@click.argument('id')
def stock_details(id):
    stock = Stock(id)
    print(
"""\
id: {}
product_id: {}
site_id: {}
stock_healthy: {} """.format(
        stock.id, stock.product_id, stock.site_id,
        stock.stock_healthy
    ))

#Site commands
@sites_cli.command("create")
@click.argument('id')
def create_site(**values):
    values['name'] = raw_input("Enter the site name: ")
    values['address'] =  raw_input("Enter the site address: ")
    Sites.new_site(**values)
    print("{} created.".format(values['id']))


@sites_cli.command("delete")
@click.argument('id')
def delete_site(id):
    Sites.delete_site(id)
    print("{} deleted.".format(id))

@stock_cli.command("details")
@click.argument('id')
def site_details(id):
    sites = Sites(id)
    print(
"""\
id: {}
name: {}
address: {} """.format(
        sites.id, sites.name, sites.address
    ))