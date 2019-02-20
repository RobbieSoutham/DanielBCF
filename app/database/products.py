#!/usr/bin/env python
"""
Products module.
"""

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
        kwargs['name'] = kwargs['name'].title()
        print(cls._tablename,
            ["id", "name", "order_qty", "cossh"],
            kwargs)

        Database.insert_into(
            cls._tablename,
            ["id", "name", "order_qty", "cossh"],
            kwargs
        )
    
    
    #Pull sites from DB
        sites = Database.get("Sites")

        for site in sites:
            #Add a new record for each site to the stock table for the site
            kwargs['site_id'] = sites[0][0]
            kwargs['product_id'] = kwargs['id']
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

        for result in results:
                content = {'id': result[0], 'name': result[1], 'order_qty': result[2]}
                data.append(content)
                content = {}
        return jsonify(data)