from app import database
from app.database import Database
import sendgrid
import os
from sendgrid.helpers.mail import *

#sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#from_email = Email("no-reply@DanielBCF.tk")

def get_order():
    low_stock =  []
    results = Database.join("Products.order_qty, Products.id, Stock.stock_healthy, site_id", "Stock", "Products", "product_id", "id")
    for result in results:
        if result[2] == None:
            address = Database.find("Sites", "name", result[3])[0][1]
            low_stock.append([result[0], result[1], address])

    order = ""

    for stock in low_stock:
        line = ""
        for info in stock:
            line = line + " " + str(info)
        order = order + "\n" + line
    
    make_order(order)

def make_order(order):
    mail = Mail(
                from_email,
                "DanielBCF Stock order",
                Email("rjsoutham@gmail.com"),
                Content("text/plain", order),
            )
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
    