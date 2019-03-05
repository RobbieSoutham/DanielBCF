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

#Sendgrid setup
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("SENDGRID_API_KEY"))
from_email = Email("no-reply@DanielBCF.tk")
from_email.name = "DanielBCF"

#Setup config parser object
config = ConfigParser()

#Setup Serializer object
s = URLSafeSerializer(app.config["SECRET_KEY"])

@app.route("/login", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def login():
    form = forms.login(request.form)

    if form.validate_on_submit():
        #Check if user exists
        user = User.login(
            form.email.data,
            form.password.encode("utf-8"),
        )
        if user:
            #If user exists log them in
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
    form = forms.registration(request.form)
    
    if request.method == "GET" or not form.validate():
        return render_template("register.html", form=form)
    
    #If the user is not already registered attempt to set up a temp user
    elif not User.registered(form.email.data):
        #Check if they are already a temp user
        try:
            Temp_user.new_user(
                email = form.email.data,
                first_name = form.first_name.data,
                surname = format(form.surname.data),
                #Turn into byte object for use with bcrypt
                password = form.password.data.encode("utf-8"),
            )
        except IntegrityError:
            #If they are a temp user
            flash("Please verify your email address!", "danger")
            return redirect(url_for("login"))
            
        #Generate tokens for verification
        manager_t = s.dumps(form.email.data)
        user_t = s.dumps(form.email.data, salt="confirm_email")
        
        #Form user confirmation email
        mail = Mail(
            from_email,
            "Confirm email",
            Email(form.email.data),
            #Parse the user token, first name and surname into the template
            Content("text/html", render_template("email/user.html", user_t=user_t, first_name=form.first_name.data, surname=form.surname.data)),
        )
        #Send email
        sg.client.mail.send.post(request_body=mail.get())

        #Form manager confirmation email
        mail = Mail(
            from_email,         
            "User confirmation",
            Email("rjsoutham@gmail.com"),
            #Parse the manager token, first name and surname into the template
            Content("text/html", render_template("email/manager.html", manager_t=manager_t, first_name=form.first_name.data, surname=form.surname.data)),
        )
        #Send email
        sg.client.mail.send.post(request_body=mail.get())
        
        flash("Registration complete. Please check your email for verification.", "success")
        return redirect(url_for("login"))
    else:
        flash("User with email already exists.", "danger")
        return redirect(url_for("register"))  

@app.route("/confirm_email/<token>")
def confirm_email(token):
    try:
        #Convert users token into users email
        email = s.loads(token, salt="confirm_email")
    except:
        #If unable to convert, the token does not exist and neither does the user
        flash("Invalid token.", "danger")
        return redirect(url_for("login"))

    #Verify the user on the users side 
    Temp_user.user_verify(email)
    flash("Email verified.", "success")
    return redirect(url_for("login"))

@app.route("/confirm_account/<token>")
def confirm_account(token):
    try:
        #Convert managers token into users email
        email = s.loads(token)
    except:
        flash("Invalid token.", "danger")
        return redirect(url_for("login"))

    #Verify the user on the managers side 
    Temp_user.manager_verify(email)
    flash("Account verified.", "success")
    return redirect(url_for("login"))

@app.route("/stock")
@login_required
def stock():
    return render_template("stock.html")


@app.route("/cossh")
@login_required
def cossh():
    return render_template("cossh.html")

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    if is_manager():
        form = forms.settings(request.form)

        #Open the config
        config.read("app/config.ini")
        #Pull the values needed from the config
        man_email = config.get("Settings", "man_email")
        sup_email = config.get("Settings", "sup_email")
        del_time = config.get("Settings", "del_time")
        
        if request.method == "GET" or not form.validate():         
            return render_template("settings.html", form=form, man_email=man_email, sup_email=sup_email, del_time=del_time)
        else:
            #Update config
            config["Settings"] = {
                'man_email': form.man_email.data,
                'sup_email': form.sup_email.data,
                'del_time': form.del_time.data
            }
            with open('app/config.ini', "w") as f:
                config.write(f)
                flash("Successfully updated.", "success")
                return redirect("settings")
    else:
        flash("Only the manager can use this page.", "danger")
        return redirect(url_for("stock"))
        
@app.route("/products")
@login_required
def products():
    form = forms.products(request.form)
    if is_manager():
        form = forms.products(request.form)
        return render_template("products.html", form=form)
    else:
        flash("Only the manager can use this page.", "danger")
        return redirect(url_for("login"))

@app.route("/sites")
@login_required
def sites():
    if is_manager():
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
            instant_order(request.args.get("id"))
            to_status = "NULL"
        
        try:
            Stock.update_stock(id, to_status)
            return "Ok"
        except:
            flash("An error occurred, the stock was not updated", "danger")
            return redirect(url_for("stock")) 
    else:
        return abort(404)

@app.route("/delete_site")
@login_required
def delete_site():
    if request.is_xhr:
        Site.delete_site(request.args.get("name"))
        return "ok"
    else:
        return abort(404)

@app.route("/delete_product")
@login_required
def delete_product():  
    if request.is_xhr:
        Product.delete_product(request.args.get("id"))
        return "ok"
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
                        try:
                            #Adding site
                            Site.new_site(
                                name = form.name.data,
                                address = form.address.data             
                            )
                            return jsonify(1)
                        except IntegrityError:
                            return jsonify("This site is already in the database.")
                        except:
                            return jsonify("An error occurred, the product was not added.")
                            
                    else:
                        try:
                            #Changing site
                            Site.update_site(
                                previous_name = form.previous_name.data,
                                name = form.name.data,
                                address = form.address.data
                            )
                            return jsonify(1)
                        except:
                            return jsonify("An error occurred, the site was not updated.")
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
                    try:
                        #Changing Product
                        Product.update_product(
                            previous_id = form.previous_id.data,
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


@app.context_processor
def get_man_email():
    #Get managers email for permissions
    config.read("app/config.ini")
    man_email = config.get("Settings", "man_email")

    #Return email for use in templates
    return dict(man_email=man_email)

def is_manager():
    form = forms.settings(request.form)
    config.read("app/config.ini")
    man_email = config.get("Settings", "man_email")
    
    #Check if the current user is the manger
    if current_user.email == man_email:
        return True
    else:
        return False
