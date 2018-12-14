#!/usr/bin/env python
"""
Database module.
"""
from MySQLdb import connect

from .. import app
from flask import jsonify


class Database(object):
    """ Base Database Class """
    def __enter__(self):
        self.conn = connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USERNAME'],
            password=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DATABASE']
        )
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

    @classmethod
    def insert_into(cls, table, attributes, values):
        for a in attributes:
            if a not in values:
                raise TypeError("Attribute {} not in values.".format(a))

        with cls() as c: c.execute(
            "INSERT INTO {} ({}) VALUES ({})".format(
                table,
                ', '.join(attributes),
                ', '.join(["'{}'".format(values[a]) for a in attributes])
        ))

    @classmethod
    def delete(cls, table, column, value):
        with cls() as c: c.execute(
            "DELETE FROM {} WHERE {}={}".format(
                table,
                column,
                "'{}'".format(value)
        ))

    @classmethod
    def find(cls, table, column, value):
        with cls() as c:
            c.execute(
                "SELECT * FROM {} WHERE {}={}".format(
                    table,
                    column,
                    "'{}'".format(value)
            ))
            return c.fetchall()

    @classmethod
    def get(cls, table):
        with cls() as c:
            results = []
            query = "SELECT * FROM {}".format(table)
            result = c.execute(query)
            for row in result:
                results.append({'id': row[0], 'product_id': row[1], 'site_id': row[2], 'stock_healthy': row[3]})
            return jsonify(result)
