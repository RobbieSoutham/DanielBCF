from functools import wraps

from flask import (
    render_template, request, flash,
    redirect, url_for, g
)

from bcrypt import hashpw, gensalt, checkpw
from MySQLdb import IntegrityError
from itsdangerous import URLSafeSerializer
from flask_mail import Mail, Message

from . import forms
from app import app
from . import database


from app.database.user import User
from app.database.sites import Site
from app.database.stock import Stock
from app.database.products import Product

from flask import jsonify, request, abort

from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user, current_user

#Flask login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.user_loader(User)

s = URLSafeSerializer(app.config["SECRET_KEY"])
mail = Mail(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Index at site root. Loads index.html"""
    form = forms.Login(request.form)

    if form.validate_on_submit():
        user = User.login(
            form.email.data,
            form.password.data.encode("utf-8"),
        )
        if user:
            login_user(user, remember=form.remember_me.data)
            flash("Logged in successfully.", "success")
            return redirect(url_for("stock"))
        
        flash("Error! Login details incorrect.", "danger")
    return render_template("index.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register. Loads register.html"""
    form = forms.Registration(request.form)
    
    if request.method == "GET" or not form.validate():
        return render_template("register.html", form=form)
       
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
            return redirect(url_for("register"))

        flash(
            "Registration complete. Please check your email for verification.",
            "success"
        )
        manager_t = s.dumps(form.email.data)
        user_t = s.dumps(form.email.data, salt="email-confirm")
        msg = Message("Confirm Email", sender="", recipients=["rjsoutham@gmail.com"])
        msg.body = render_template("email/manager.txt", manager_t=manager_t, first_name=form.first_name.data, surname=form.surname.data)
        mail.send(msg)
        return redirect(url_for("login"))

@app.route("/confirm_email/<manager_t>")
def confirm_email(manager_t):
    try:
        email = s.loads(manager_t)
    except:
        return "Error"
    print(email)
    User.verify(email)
    return "success"


@app.route("/", methods=["GET", "POST"])
@app.route("/stock")
@login_required
def stock():
    return render_template("stock.html")


@app.route("/", methods=["GET", "POST"])
@app.route("/COSSH")
@login_required
def cossh():
    return render_template("cossh.html")


@app.route("/products")
@login_required
def products():
    if current_user.email == "rob@devthe.com":
        return render_template("products.html")
    else:
        return render_template("denied.html")

@app.route("/sites")
@login_required
def sites():
    return render_template("sites.html")


#AJAX routs
@app.route("/change_stock")
@login_required
def change_stock():
    #Check if the request is xhr (ajax) or from a user
    if request.is_xhr:
        id = request.args.get("id")
        to_status = request.args.get("to_status")
        if to_status == "true":
            to_status = True
        elif to_status == "false":
            to_status = False
        else:
            to_status = "NULL"
    
        Stock.update_stock(id, to_status)
        return "Ok"
    else:
        return abort(404)

@app.route("/stock_list")
@login_required
def stock_list():
    if request.is_xhr:
        return Stock.get_stock()
    else:
        return Stock.get_stock()
    

@app.route("/sites_list")
@login_required
def sites_list():
    if request.is_xhr:
        return Site.getSites()
    else:
        return abort(404)
    
@app.route("/product_list")
@login_required
def product_list():
    if request.is_xhr:
        return Product.get_products()
    else:
        return abort(404)