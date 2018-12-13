#!/usr/bin/env python
"""
Products module.
"""
from bcrypt import hashpw, gensalt, checkpw
from flask_login import UserMixin

from . import Database

class ProductNotFound(Exception):
    pass

class Product(UserMixin):
    _tablename = "Product"

    def __init__(self, id):
        try:
            self.__product = Database.find(self._tablename, "id", id)[0]
        except IndexError:
            raise ProductNotFound(id)
        self.id = id
        self.name = self._product[1]
        self.order_qty = self._product[2]

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
    
