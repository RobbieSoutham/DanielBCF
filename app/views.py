from functools import wraps

from flask import (
    render_template, request, flash,
    redirect, url_for, g
)

from bcrypt import hashpw, gensalt, checkpw
from MySQLdb import IntegrityError
from itsdangerous import URLSafeSerializer
import sendgrid
import os
from sendgrid.helpers.mail import *

from . import forms
from app import app
from . import database

from app.database.user import User
from app.database.sites import Site
from app.database.stock import Stock
from app.database.products import Product

from flask import jsonify, request, abort
from flask_mail import Mail, Message

from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user, current_user

#Flask login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.user_loader(User)

mail = Mail(app)
sg = sendgrid.SendGridAPIClient(apikey="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")
from_email = Email("no-reply@DanielBCF.tk")

s = URLSafeSerializer(app.config["SECRET_KEY"])

@app.route("/login", methods=["GET", "POST"])
def login():
    """Index at site root. Loads index.html"""
    form = forms.login(request.form)

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
    form = forms.registration(request.form)
    
    if request.method == "GET" or not form.validate():
        return render_template("register.html", form=form)
       
    else:
        try:
            User.new_user(
                email = form.email.data,
                first_name = form.first_name.data,
                surname = form.surname.data,
                password = form.password.data.encode("utf-8"),
            )
        except IntegrityError:
            flash("User with email already exists.", "danger")
            return redirect(url_for("register"))

        flash(
            "Registration complete. Please check your email for verification.",
            "success"
        )
        manager_t = s.dumps(form.email.data)


        msg = Message("sf", sender="no-reply@danielbcf.tk", recipients="rjsoutham@gmail.com".split())
        msg.body = "sdf"
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
    form = forms.products(request.form)
    if current_user.email == "rob@devthe.com":
        form = forms.products(request.form)
        return render_template("products.html", form=form)
    else:
        return render_template("denied.html")




@app.route("/sites", methods=["GET", "POST"])
@app.route("/sites")
@login_required
def sites():
    form = forms.sites(request.form)
    return render_template("sites.html", form=form)
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

@app.route("/delete_site")
@login_required
def delete_site():
    Site.delete_site(request.args.get("id"))
    return ""

@app.route("/delete_product")
@login_required
def delete_product():
    Product.delete_product(request.args.get("id"))
    return ""

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
    return Site.get_sites()

@app.route("/product_list")
@login_required
def product_list():
    #if request.is_xhr:
    return Product.get_products()
    #else:
       # return abort(404)


@app.route("/modal_forms", methods=["GET", "POST"])
@login_required
def modal_forms():
    if request.method == "GET":
        return abort(404)
    else:
        #Load the form depending on the page theyre on
        print(request.form.get('page'))
        if request.form.get('page') == "sites":
            form = forms.sites(request.form)
        else:
            form = forms.products(request.form)
        if form.validate():
            if request.form.get('page') == "sites":
                #User on sites page
                if form.site_id.data == "":
                        #Adding site
                        try:
                            Site.new_site(
                                name = form.name.data,
                                address = form.address.data
                                
                            )
                            return jsonify(1)
                        except:
                            return jsonify("An error occurred, the site was not added.")
                            
                else:
                    try:
                        #Changing site
                        Site.update_site(
                            site_id = form.site_id.data,
                            name = form.name.data,
                            address = form.address.data
                        )
                        return jsonify(true)
                    except:
                        return jsonify("An error occurred, the site was not updated.")
            else:
                #User on products page
                if form.edit.data == 0:
                        #Adding Product
                        print("sdf")
                        Product.new_product(
                            id = form.product_id.data,
                            name = form.name.data,
                            order_qty = form.order_qty.data,
                            cossh = form.cossh.data
                                
                        )
                        return jsonify(1)
                else:
                    try:
                        #Changing Product
                        Product.update_product(
                            id = form.product_id.data,
                            name = form.name.data,
                            order_qty = form.order_qty.data,
                            cossh = form.cossh.data
                        )
                        return jsonify(1)
                    except:
                        return jsonify("An error occurred, the product was not updated.")
        else:
            for fieldName, errorMessages in form.errors.items():
                for error in errorMessages:
                    return jsonify(error)
