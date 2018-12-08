#!/usr/bin/env python
"""
User module.
"""

from . import Database
import bcrypt

class User(Database):
    @classmethod
    def new_user(cls, **kwargs):
        kwargs['first_name'] = kwargs['first_name'].title()
        kwargs['surname'] = kwargs['surname'].title()
        kwargs['password'] = bcrypt.hashpw(kwargs['password'], bcrypt.gensalt())
        cls().insert_into(
            "Users",
            ["email", "first_name", "surname", "password"],
            kwargs
        )
    
    @classmethod
    def delete_user(cls, email):
        cls.delete("Users", "email", email)
