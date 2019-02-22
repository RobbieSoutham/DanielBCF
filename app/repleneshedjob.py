from app import database
from app.database import Database
import datetime

def rep():
    print("*********")
    delivery_days = datetime.timedelta(7)
    today = datetime.date.today()
    ordered_stock = Database.get("Stock")
    stock_out = []

    for stock in ordered_stock:
        if stock[3] == None:
            stock_out.append(stock)

    for stock in stock_out:
        if stock[4] - today >= delivery_days:
            Database.update("Stock", "stock_healthy", "1", "stock_healthy", "Null")
            Database.update("Stock", "stock_healthy", "1", "order_date", "Null")