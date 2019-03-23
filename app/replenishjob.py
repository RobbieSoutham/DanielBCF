from app import database
from app.database import Database
import datetime
from configparser import ConfigParser

config = ConfigParser()

def rep():
    #Get delivery time from config
    config.read("app/config.ini")
    del_time = datetime.timedelta(days=int(config.get("Settings", "del_time")))
    today = datetime.datetime.now().date()
    ordered_stock = Database.get("Stock")
    stock_out = []

    for stock in ordered_stock:
        if stock[3] == None and stock[3] is not None:
            #Retrieve stock items that are out of stock
            stock_out.append(stock)

    for stock in stock_out:
        #If the delivery time has passed set the stock level as healthy
        print(stock[4])
        if stock[4] - today >= del_time:
            Database.update("Stock", "stock_healthy", "1", "stock_healthy", "Null")
            Database.update("Stock", "stock_healthy", "1", "order_date", "Null")