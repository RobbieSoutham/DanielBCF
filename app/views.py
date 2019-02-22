from functools import wraps

from flask import (
    render_template, request, flash,
    redirect, url_for, g
)

from bcrypt import hashpw, gensalt, checkpw
from MySQLdb import IntegrityError
from itsdangerous import URLSafeSerializer
#import sendgrid
import os
#from sendgrid.helpers.mail import *
from configparser import ConfigParser


from . import forms
from app import app
from . import database
from app import orders
from app import repleneshedjob

from app.orders import instant_order
from app.orders import get_order
from app.repleneshedjob import rep
from app.database.user import User
from app.database.temp_user import Temp_user
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

#sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#from_email = Email("no-reply@DanielBCF.tk")

config = ConfigParser()

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
       
    elif not User.registered(form.email.data):
            try:
                Temp_user.new_user(
                    email = form.email.data,
                    first_name = form.first_name.data,
                    surname = form.surname.data,
                    password = form.password.data.encode("utf-8"),
                )
            except IntegrityError:
                flash("User with email already exists.", "danger")
                return redirect(url_for("register"))
            
            #Generate tokens for verification
            manager_t = s.dumps(form.email.data)
            user_t = s.dumps(form.email.data, salt="confirm_email")

            print(manager_t)
            print(user_t)

            #Send user confirmation email
            '''
            mail = Mail(
                from_email,
                "User Confirmation",
                Email(form.email.data),
                Content("text/html", render_template("email/user.html", user_t=user_t, first_name=form.first_name.data, surname=form.surname.data)),
            )
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)

            #Send manager confirmation email
            mail = Mail(
                from_email,         
                "Confirm Email",
                Email("rjsoutham@gmail.com"),
                Content("text/html", render_template("email/manager.html", manager_t=manager_t, first_name=form.first_name.data, surname=form.surname.data)),
            )
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            '''
            flash("Registration complete. Please check your email for verification.", "success")
            return redirect(url_for("login"))
    else:
        flash("User with email already exists.", "danger")
        return redirect(url_for("register"))  

@app.route("/confirm_email/<token>")
def confirm_email(token):
    try:
        email = s.loads(token, salt="confirm_email")
    except:
        return "Error"
    print(email)
    Temp_user.user_verify(email)
    flash("Email verified.", "success")
    return redirect(url_for("login"))

@app.route("/confirm_account/<token>")
def confirm_account(token):
    try:
        email = s.loads(token)
    except:
        return "Error"
    print(email)
    Temp_user.manager_verify(email)
    flash("Account verified.", "success")
    return redirect(url_for("login"))

@app.route("/stock")
@login_required
def stock():
    return render_template("stock.html")


@app.route("/COSSH")
@login_required
def cossh():
    return render_template("cossh.html")

@app.route("/sites", methods=["GET", "POST"])
@app.route("/settings")
@login_required
def settings():
    config.read("app/config.ini")
    man_email = config.get("Settings", "man_email")
    sup_email = config.get("Settings", "sup_email")
    del_time = config.get("Settings", "del_time")
    file = open("config.ini", "w")
    if request.method == "GET" or not form.validate():
        form = forms.settings(request.form)
        return render_template("settings.html", form=form, man_email=man_email, sup_email=sup_email, del_time=del_time)


@app.route("/products")
@login_required
def products():
    form = forms.products(request.form)
    if current_user.email == "rob@devthe.com":
        form = forms.products(request.form)
        return render_template("products.html", form=form)
    else:
        flash("Only the manager can use this page.", "danger")
    return redirect(url_for("login"))
    con

@app.route("/sites")
@login_required
def sites():
    if current_user.email == "rob@devthe.com":
        form = forms.sites(request.form)
        return render_template("sites.html", form=form)
    else:
        flash("Only the manager can use this page.", "danger")
        return redirect(url_for("login"))

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
            #get_order()
            rep()
            #instant_order(request.args.get("id"))
            to_status = "NULL"
    
        #Stock.update_stock(id, to_status)
        return "Ok"
    else:
        return abort(404)

@app.route("/delete_site")
@login_required
def delete_site():
    Site.delete_site(request.args.get("name"))
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
    if request.is_xhr:
        return Site.get_sites()
    else:
        return abort(404)

@app.route("/product_list")
@login_required
def product_list():
    if request.is_xhr:
        return Product.get_products()
    else:
        return abort(404)


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
                    if form.edit.data == 0:
                        #try:
                            #Adding site
                            Site.new_site(
                                name = form.name.data,
                                address = form.address.data             
                            )
                            return jsonify(1)
                        #except IntegrityError:
                            #return jsonify("This site is already in the database.")
                        #except:
                            #return jsonify("An error occurred, the product was not added.")
                            
                    else:
                        #try:
                            #Changing site
                            Site.update_site(
                                previous_name = form.previous_name.data,
                                name = form.name.data,
                                address = form.address.data
                            )
                            return jsonify(1)
                        #except:
                            #return jsonify("An error occurred, the site was not updated.")
            else:
                #User on products page
                if form.edit.data == False:
                    try:
                        #Adding Product
                        Product.new_product(
                            id = form.product_id.data,
                            name = form.name.data,
                            order_qty = form.order_qty.data,
                            cossh = form.cossh.data
                                
                        )
                        return jsonify(1)  
                    except:
                        return jsonify("An error occurred, the product was not added.")
                else:
                    #try:
                        #Changing Product
                        Product.update_product(
                            previous_id = form.previous_id.data,
                            id = form.product_id.data,
                            name = form.name.data,
                            order_qty = form.order_qty.data,
                            cossh = form.cossh.data
                        )
                        return jsonify(1)
                    #except:
                       # return jsonify("An error occurred, the product was not updated.")
        else:
            for fieldName, errorMessages in form.errors.items():
                for error in errorMessages:
                    return jsonify(error)
