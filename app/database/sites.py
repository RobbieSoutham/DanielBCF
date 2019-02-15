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

    def __init__(self, id):
        try:
            self._tablename = Database.find(self._tablename, "id", id)[0]
        except IndexError:
            raise ProductNotFound(id)
        self.id = id
        self.name = self._tablename[1]
        self.address = self._tablename[2]

    @classmethod
    def new_site(cls, **kwargs):
        kwargs['name'] = kwargs['name'].title()
        kwargs['address'] = kwargs['address'].title()
        Database.insert_into(
            cls._tablename,
            ["name", "address"],
            kwargs
        )

        #Grab newly added site ID
        site_id = Database.find(cls._tablename, "name", kwargs['name'])

        #Pull products from DB
        products = Database.get("Products")

        for product in product:
            #Add a new record for each product to the stock table for the site
                Database.insert_into(product[0], site_id, True)
    
    @classmethod
    def delete_site(cls, id):
        Database.delete(cls._tablename, "id", id)

    @classmethod
    def get_sites(cls):
        data = []
        content = {}
        sites =  Database.get("Sites")
        for site in sites:
            content = {'id': site[0], 'name': site[1], 'address': site[2]}
            data.append(content)
            content = {}
        return jsonify(data)