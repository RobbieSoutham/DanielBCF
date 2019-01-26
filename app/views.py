from functools import wraps

from flask import (
    render_template, request, flash,
    redirect, url_for, g, flask_mail
)

from bcrypt import hashpw, gensalt, checkpw
from MySQLdb import IntegrityError
from itsdangerous import URLSafeSerializer
from flask_mail import Mail, Message

from . import forms
from app import app
from . import database


from app.database.user import User
from app.database.sites import Sites
from app.database.stock import Stock

from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user

#Flask login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.user_loader(User)

s = URLSafeSerializer(app.config["SECRET_KEY"])
app.config.update(
    MAIL_SERVER = '64.233.184.109',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'rjsoutham@gmail.com',
    MAIL_PASSWORD = 'rviiwhwizyddbxbp',
    MAIL_DEFAULT_SENDER = 'noreply@danielbcf.tk'
)
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    """Index at site root. Loads index.html"""
    form = forms.Login(request.form)

    if form.validate_on_submit():
        user = User.login(
            form.email.data,
            form.password.data.encode("utf-8")
        )
        if user:
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('stock'))
        
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
       
    else:
        try:
            User.new_user(
                email=form.email.data,
                first_name=form.first_name.data,
                surname=form.surname.data,
                password=form.password.data.encode("utf-8"),
            )
        except IntegrityError:
            flash("User with email already exists.", "danger")
            return redirect(url_for('register'))

        flash(
            "Registration complete. Please check your email for verification.",
            "success"
        )
        manager_t = s.dumps(form.email.data)
        user_t = s.dumps(form.email.data, salt="email-confirm")
        msg = Message("Confirm Email", sender="", recipients=["rjsoutham@gmail.com"])
        msg.body = render_template("email/manager.txt", manager_t=manager_t, first_name=form.first_name.data, surname=form.surname.data)
        mail.send(msg)
        print(manager_t)
        return redirect(url_for('login'))

@app.route('/confirm_email/<manager_t>')
def confirm_email(manager_t):
    try:
        email = s.loads(manager_t)
    except:
        return "Error"
    print (email)
    User.verify(email)
    return "success"


@app.route('/stock')
@login_required
def stock():
    return render_template('stock.html')

@app.route('/change_stock')
@login_required
def change_stock():
    id = request.args.get('id')
    to_status = request.args.get('to_status')
    print(to_status)
    if to_status == "true":
        to_status = True
    elif to_status == "false":
        to_status = False
    else:
        to_status = "NULL"
    print(to_status)
    Stock.update_stock(id, to_status)
    return "one"

@app.route('/stock_list')
@login_required
def stock_list():
    return Stock.get_stock()

@app.route('/sites_list')
@login_required
def sites_list():
    return Sites.getSites()
