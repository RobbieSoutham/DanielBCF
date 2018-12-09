from functools import wraps

from flask import (
    render_template, request, flash,
    redirect, url_for, g
)
from MySQLdb import IntegrityError
from . import forms
from app import app

from database.user import User

# TODO: Incorporate flask-login here
# https://flask-login.readthedocs.io

@app.route('/', methods=['GET', 'POST'])
def index():
    """Index at site root. Loads index.html"""
    form = forms.Login(request.form)
    return render_template('index.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register. Loads register.html"""
    form = forms.Registration(request.form)
    if request.method == 'GET' or not form.validate():
        return render_template('register.html', form=form)

    try:
        User.new_user(
            email=form.email.data,
            first_name=form.first_name.data,
            surname=form.surname.data,
            password=form.password.data.encode('utf-8'),
        )
    except IntegrityError:
        flash("User with email already exists.", "danger")
        return redirect(url_for('register'))

    flash(
        "Registration complete. Please check your email for verification.",
        "success"
    )
    return redirect(url_for('index'))
