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

class Registration(FlaskForm):
    email = StringField(
        'Email Address', [
            InputRequired("Please enter your email address."),
            Email("This field requires a valid email address")
    ])
    first_name = StringField('First Name', [
        DataRequired("Please enter your first name."),
        length(max=32)
    ])
    surname = StringField('Surname', [
        DataRequired("Please enter your surname."),
        length(max=32)
    ])
    password = PasswordField('New Password', [
        DataRequired("Please enter a password.")
    ])
    confirm = PasswordField('Repeat Password', [
        EqualTo('password', message='Passwords must match.')
    ])

class Login(FlaskForm):
    email = StringField(
        'Email Address', [
            InputRequired("Please enter your email address."),
            Email("This field requires a valid email address")
    ])
    password = PasswordField('New Password', [
        DataRequired("Please enter a password.")
    ])
    remember_me = BooleanField(
        'Remember me'
    )

class site(FlaskForm):
    name = StringField(
        'Site Name', [
            DataRequired("Please enter a site name.")
    ])
    address = StringField(
        'Site Address', [
            DataRequired("Please enter a site address")
    ])
    site_id = StringField(
        ''
    )