#Products module

from . import Database
from flask import jsonify

class ProductNotFound(Exception):
    pass

class Product():
    _tablename = "Products"

    def __init__(self, id):
        try:
            self._tablename = Database.find(self._tablename, "id", id)[0]
        except IndexError:
            raise ProductNotFound(id)
        self.id = id
        self.name = self._tablename[1]
        self.order_qty = self._tablename[2]

    @classmethod
    def new_product(cls, **kwargs):
        kwargs["name"] = kwargs["name"].title()
        Database.insert_into(
            cls._tablename,
            ["id", "name", "order_qty", "cossh"],
            kwargs
        )
    
        #Pull sites from DB
        sites = Database.get("Sites")

        for site in sites:
            #Add a new record for each site to the stock table for the site
            kwargs["site_id"] = site[0]
            kwargs["product_id"] = kwargs["id"]
            Database.insert_into("Stock", ["product_id", "site_id"],
            kwargs
            )

    @classmethod
    def delete_product(cls, id):
        Database.delete(cls._tablename, "id", id)

    @classmethod
    def get_products(cls):
        
        data = []
        content = {}
        results = Database.get("Products")

        #Return products data as JSON
        for result in results:
                content = {"id": result[0], "name": result[1], "order_qty": result[2], "cossh": result[3]}
                data.append(content)
                content = {}
        return jsonify(data)
    
    @classmethod
    def update_product(cls, **kwargs):
        if kwargs["previous_id"] != kwargs["name"]:
            Database.update(cls._tablename, "id", kwargs['id'], "id", kwargs["previous_id"])
            
        Database.update(cls._tablename, "name", kwargs["name"], "id", kwargs["id"])
        Database.update(cls._tablename, "cossh", kwargs['cossh'], "id", kwargs["id"])
        Database.update(cls._tablename, "order_qty", kwargs["order_qty"], "id", kwargs["id"])
