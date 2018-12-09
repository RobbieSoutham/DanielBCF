#!/usr/bin/env python
"""
User module.
"""
from bcrypt import hashpw, gensalt

from . import Database

class User():
    @classmethod
    def new_user(cls, **kwargs):
        kwargs['first_name'] = kwargs['first_name'].title()
        kwargs['surname'] = kwargs['surname'].title()
        kwargs['password'] = hashpw(kwargs['password'], gensalt())
        Database.insert_into(
            "Users",
            ["email", "first_name", "surname", "password"],
            kwargs
        )
    
    @classmethod
    def delete_user(cls, email):
        Database.delete("Users", "email", email)
