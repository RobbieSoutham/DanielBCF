#!/usr/bin/env python
"""
Products module.
"""

from . import Database
from flask import jsonify

class ProductNotFound(Exception):
    pass

class Stock():
    _tablename = "Stock"

    def __init__(self, id):
        try:
            self._tablename = Database.find(self._tablename, "id", id)[0]
        except IndexError:
            raise ProductNotFound(id)
        self.id = id
        self.product_id = self._tablename[1]
        self.site_id = self._tablename[2]
        self.stock_healthy = self._tablename[2]

    @classmethod
    def new_stock(cls, **kwargs):
        Database.insert_into(
            cls._tablename,
            ["id", "product_id", "site_id"],
            kwargs
        )
    
    @classmethod
    def delete_stock(cls, id):
        Database.delete(cls._tablename, "id", id)

    @classmethod
    def getStock(cls):
        data = []
        content = {}
        results = Database.join("Stock.id, Products.name, Stock.stock_healthy, Stock.site_id", "Stock", "Products", "product_id", "id")
        for result in results:
                content = {'id': result[0], 'name': result[1], 'site_id': result[2], 'stock_healthy': result[3]}
                data.append(content)
                content = {}

        return jsonify(data)