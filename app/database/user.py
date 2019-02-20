#!/usr/bin/env python
"""
User module.
"""
from bcrypt import hashpw, gensalt, checkpw
from flask_login import UserMixin

from . import Database

class UserNotFound(Exception):
    pass

class User(UserMixin):
    _tablename = "Users"

    def get_id(self):
        return(self.email)
        
    def __init__(self, email):
        try:
            self._user = Database.find(self._tablename, "email", email)[0]
        except IndexError:
            raise UserNotFound(email)
        self.email = email
        self.first_name = self._user[1]
        self.surname = self._user[2]
        self.password = self._user[3]

    @classmethod
    def new_user(cls, **kwargs):
        
        Database.insert_into(
            cls._tablename,
            ["email", "first_name", "surname", "password"],
            kwargs
        )
    
    @classmethod
    def delete_user(cls, email):
        Database.delete(cls._tablename, "email", email)
    
    @classmethod
    def login(cls, email, password):
        try:
            user = cls(email)
            if checkpw(password, user.password.encode("utf-8")):
                return user
        except UserNotFound:
            pass
            
    @classmethod
    def registered(cls, email):
        if not Database.find(cls._tablename, "email", email):
            return False
        else:
            return True