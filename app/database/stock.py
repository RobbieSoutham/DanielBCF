#!/usr/bin/env python
"""
Products module.
"""

from . import Database

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
        kwargs['product_id'] = kwargs['product_id'].title()
        Database.insert_into(
            cls._tablename,
            ["id", "product_id", "site_id", "stock_healthy"],
            kwargs
        )
    
    @classmethod
    def delete_stock(cls, id):
        Database.delete(cls._tablename, "id", id)

    @classmethod
    def getStock(cls):
        return Database.get("Stock")