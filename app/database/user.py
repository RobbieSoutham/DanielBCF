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
        self.verified = self._user[3]
        self.password = self._user[4]
        self.creation_time = self._user[5]

    @classmethod
    def new_user(cls, **kwargs):
        kwargs['first_name'] = kwargs['first_name'].title()
        kwargs['surname'] = kwargs['surname'].title()
        kwargs['password'] = hashpw(kwargs['password'], gensalt())
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
            if checkpw(password, user.password):
                return user
        except UserNotFound:
            pass
    @classmethod
    def verify(email):
        Database.update("Users", "verified", "IFNULL(verified, 0) + 1", "email", email)