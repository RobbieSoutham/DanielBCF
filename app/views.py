from functools import wraps

from flask import (
    render_template, request, flash,
    redirect, url_for, g
)
from MySQLdb import IntegrityError
from . import forms
from app import app

from database.user import User

from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user 

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.user_loader(User)

@app.route('/', methods=['GET', 'POST'])
def login():
    """Index at site root. Loads index.html"""
    form = forms.Login(request.form)

    if form.validate_on_submit():
        user = User.login(
            form.email.data,
            form.password.data.encode('utf-8')
        )
        if user:
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('stocks'))
        
        flash('Error! Login details incorrect.', 'danger')

    return render_template('index.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

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

@app.route('/stocks')
@login_required
def stocks():
    return render_template('stocks.html')
