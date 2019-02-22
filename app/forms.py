from wtforms import (
    BooleanField, StringField,
    PasswordField
)
from wtforms.validators import *
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm

from . import app

csrf = CSRFProtect(app)
csrf.exempt("/sites")

class registration(FlaskForm):
    email = StringField(
        'Email Address', [
            InputRequired("Please enter your email address:"),
            Email("This field requires a valid email address:")
    ])
    first_name = StringField('First Name:', [
        DataRequired("Please enter your first name:"),
        length(max=32)
    ])
    surname = StringField('Surname:', [
        DataRequired("Please enter your surname."),
        length(max=32)
    ])
    password = PasswordField('Password:', [
        DataRequired("Please enter a password.")
    ])
    confirm = PasswordField('Repeat Password:', [
        EqualTo('password', message='Passwords must match.')
    ])

class login(FlaskForm):
    email = StringField(
        'Email Address:', [
            InputRequired("Please enter your email address"),
            Email("This field requires a valid email address")
    ])
    password = PasswordField('New Password:', [
        DataRequired("Please enter a password.")
    ])
    remember_me = BooleanField(
        'Remember me:'
    )

class sites(FlaskForm):
    name = StringField(
        'Site Name:', [
            DataRequired("Please enter a site name.")
    ])
    address = StringField(
        'Site Address:', [
            DataRequired("Please enter a site address.")
    ])

    previous_name = StringField(
        ''
    )
    edit = BooleanField(
        ''
    )
    
class products(FlaskForm):
    product_id = StringField(
        'Product ID:', [
            DataRequired("Please enter a product ID.")
    ])
    name = StringField(
        'Product Name:', [
            DataRequired("Please enter a product name.")
    ])
    cossh = StringField(
        'COSSH:'
    )
    order_qty = StringField(
        'Order Quantity:', [
            DataRequired("Please enter an order quantity.")
    ])

    previous_id = StringField(
        ''
    )
    edit = BooleanField(
        ''
    )

class settings(FlaskForm):
    man_email = StringField(
        'Manager email:', [
            InputRequired("Please enter an email address."),
            Email("This field requires a valid email address.")
    ])
    sup_email = StringField(
        'Supplier email:', [
            DataRequired("Please enter the suppliers email.")
    ])
    del_time = StringField(
        'Average supplier delivery time:', [
        DataRequired("Please enter a delivery time.")
    ])