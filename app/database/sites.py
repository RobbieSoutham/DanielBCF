#!/usr/bin/env python
"""
Products module.
"""

from flask import jsonify
from . import Database

class ProductNotFound(Exception):
    pass

class Site():
    _tablename = "Sites"

    def __init__(self, name):
        try:
            self._tablename = Database.find(self._tablename, "name", name)[0]
        except IndexError:
            raise ProductNotFound(name)
        self.name = name
        self.address = self._tablename[1]

    @classmethod
    def new_site(cls, **kwargs):
        kwargs['name'] = kwargs['name'].title()
        kwargs['address'] = kwargs['address'].title()
        Database.insert_into(
            cls._tablename,
            ["name", "address"],
            kwargs
        )

        #Pull products from DB
        products = Database.get("Products")

        for product in products:
            #Add a new record for each product to the stock table for the site
            kwargs['product_id'] = product[0]
            Database.insert_into("Stock", ["product_id", "name"],
            kwargs
        )
    
    @classmethod
    def delete_site(cls, name):
        Database.delete(cls._tablename, "name", name)

    @classmethod
    def get_sites(cls):
        data = []
        content = {}
        sites =  Database.get("Sites")
        for site in sites:
            content = {'name': site[0], 'address': site[1]}
            data.append(content)
            content = {}
        return jsonify(data)
    
    @classmethod
    def update_site(cls, **kwargs):
        if kwargs['previous_name'] != kwargs['name']:
            Database.update(cls._tablename, "name", kwargs['name'], "name", kwargs['previous_name'])
        
        Database.update(cls._tablename, "address", kwargs['address'], "name", kwargs['name'])
        