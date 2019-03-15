from wtforms import (
    BooleanField, StringField,
    PasswordField, IntegerField
)
from wtforms.validators import *
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm

from . import app

csrf = CSRFProtect(app)

#Setting up forms
class registration(FlaskForm):
    email = StringField(
        'Email Address:', [
            InputRequired("Please enter your email address:"),
            Email("Please enter a valid email address."),
            length(max=32)
            
        ]
    )
    first_name = StringField('First Name:', [
        DataRequired("Please enter your first name."),
        length(max=32)
        ]
    )
    surname = StringField('Surname:', [
        DataRequired("Please enter your surname."),
        length(max=32)
        ]
    )
    password = PasswordField('Password:', [
        DataRequired("Please enter a password.")
        ]
    )
    confirm = PasswordField('Repeat Password:', [
        EqualTo('password', message='Passwords must match.')
        ]
    )

class login(FlaskForm):
    email = StringField(
        'Email Address:', [
            InputRequired("Please enter your email address."),
            Email("Please enter a valid email address."),
            length(max=32)
        ]
    )
    password = PasswordField('New Password:', [
        DataRequired("Please enter a password."),
        ]
    )
    remember_me = BooleanField(
        'Remember me:',
        false_values=(False, 'false', 0, '0'))
    )

class sites(FlaskForm):
    name = StringField(
        'Site Name:', [
            DataRequired("Please enter a site name."),
            length(max=32)
        ]
    )
    address = StringField(
        'Site Address:', [
            DataRequired("Please enter a site address."),
            length(max=256)
        ]
    )

    #Not for user
    #Allow us to determine if the form returned is editing a site or adding a new one
    edit = BooleanField(
        ''
    )
    #Allows us to identify the name of the product being edited
    previous_name = StringField(
        ''
    )

    
class products(FlaskForm):
    product_id = StringField(
        'Product ID:', [
            DataRequired("Please enter a product ID."),
            length(max=256)
        ]
    )
    name = StringField(
        'Product Name:', [
            length(max=256),
            DataRequired("Please enter a product name.")
        ]
    )
    cossh = StringField(
        'COSSH:'
    )
    order_qty = IntegerField(
        'Order Quantity:', [
            DataRequired("Please enter an order quantity."),
            NumberRange(min=1, max=None)
        ])
    

    #Not for user
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
            Email("This field requires a valid email address."),
            length(max=256)
        ]
    )
    sup_email = StringField(
        'Supplier email:', [
            DataRequired("Please enter the suppliers email."),
            length(max=32)
        ]
    )
    del_time = IntegerField(
        'Average supplier delivery time:', [
        DataRequired("Please enter a delivery time."),
        NumberRange(min=1, max=None)
        ]
    )
