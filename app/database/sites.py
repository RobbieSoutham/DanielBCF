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
            ["id", "name", "address"],
            kwargs
        )
    
    @classmethod
    def delete_site(cls, id):
        Database.delete(cls._tablename, "id", id)

    @classmethod
    def getSites(cls):
        data = []
        content = {}
        results =  Database.get("Sites")
        for result in results:
            content = {'id': result[0], 'name': result[1], 'address': result[2]}
            data.append(content)
            content = {}
        return jsonify(data)