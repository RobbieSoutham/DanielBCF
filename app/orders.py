from app import database
from app.database import Database
import sendgrid
import os
from sendgrid.helpers.mail import *
from configparser import ConfigParser

config = ConfigParser()


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("no-reply@DanielBCF.tk")

def instant_order(stock_id):
    #Get dat needed for order
    product_id = Database.find("Stock", "id", stock_id)[0][1]
    site_id = Database.find("Stock", "id", stock_id)[0][2]

    order_qty = Database.find("Products", "id", product_id)[0][2]

    address = Database.find("Sites", "name", site_id)[0][1]

    details = product_id, order_qty, address
    order = ""
    
    #Setup email without list formatting
    for detail in details:
        order = order + str(detail) + " "
    make_order(order)


def get_order():
    low_stock =  []

    #Get data needed for order
    results = Database.join("Products.order_qty, Products.id, Stock.stock_healthy, Stock.site_id, Stock.id", "Stock", "Products", "product_id", "id")
    for result in results:
        if result[2] == None:
            
            address = Database.find("Sites", "name", result[3])[0][1]
            low_stock.append([result[0], result[1], address])

            #Set the all the stock that was low to ordered
            Database.update("Stock", "stock_healthy", "Null", "stock_healthy", 0)

    order = ""

    #Setup email without list formatting
    for stock in low_stock:
        line = ""
        for info in stock:
            line = line + " " + str(info)
        order = order + "\n" + line
    
    make_order(order)

def make_order(order):
    config.read("app/config.ini")
    sup_email = config.get("Settings", "sup_email")

    #Send order email
    mail = Mail(
                from_email,
                "DanielBCF Stock order",
                Email(sup_email),
                Content("text/plain", order),
            )
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)