from app import database
from app.database import Database

def order(stock_id):
    product_id = Database.find("Stock", "id", stock_id)[0][1]
    stock_id = Database.find("Stock", "id", stock_id)[0][2]

    order_qty = Database.find("Products", "id", product_id)[0][2]

    address = Database.find("Sites", "name", stock_id)[0][1]

    print(product_id, order_qty, address)
