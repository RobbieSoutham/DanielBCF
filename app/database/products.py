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
        kwargs['order_qty'] = kwargs['order_qty'].title()
        Database.insert_into(
            cls._tablename,
            ["id", "name", "order_qty"],
            kwargs
        )
    
    @classmethod
    def delete_product(cls, id):
        Database.delete(cls._tablename, "id", id)

    @classmethod
    def get_products(cls):
        
        data = []
        content = {}
        results = Database.find("Products", "id", "*")
        print("dv")
        for result in results:
                print(result[3])
                content = {'id': result[0], 'name': result[1], 'site_id': result[2], 'stock_healthy': result[3]}
                data.append(content)
                content = {}

        return jsonify(data)