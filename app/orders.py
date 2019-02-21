from app import database
from app.database import Database
#import sendgrid
import os
#from sendgrid.helpers.mail import *

#sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
#from_email = Email("no-reply@DanielBCF.tk")

def instant_order(stock_id):
    product_id = Database.find("Stock", "id", stock_id)[0][1]
    stock_id = Database.find("Stock", "id", stock_id)[0][2]

    order_qty = Database.find("Products", "id", product_id)[0][2]

    address = Database.find("Sites", "name", stock_id)[0][1]

    print(product_id, order_qty, address)


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
'''
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
    '''