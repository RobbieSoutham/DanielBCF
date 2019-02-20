#!/usr/bin/env python
"""
Temp user module.
"""
from bcrypt import hashpw, gensalt, checkpw
from flask_login import UserMixin

from . import Database
from app.database.user import User

class UserNotFound(Exception):
    pass

class Temp_user(UserMixin):
    _tablename = "Temp_users"

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
        kwargs['first_name'] = kwargs['first_name'].title()
        kwargs['surname'] = kwargs['surname'].title()
        
        #Hash the password and convert it back into unicode to be stored in the DB
        kwargs['password'] = hashpw(kwargs['password'], gensalt()).decode('unicode_escape')
        Database.insert_into(
            cls._tablename,
            ["email", "first_name", "surname", "password"],
            kwargs
        )
    
    @classmethod
    def delete_user(cls, email):
        Database.delete(cls._tablename, "email", email)


    @classmethod
    def verify(cls, temp_user):
        User.new_user(
            email = temp_user[0],
            first_name = temp_user[1],
            surname = temp_user[2],
            password = temp_user[3],
        )
        Database.delete(cls._tablename, "email", temp_user[0])


    @classmethod
    def user_verify(cls, email):
        temp_user = Database.find(cls._tablename, "email", email)[0]
        if temp_user[5] == 1:
            cls.verify(temp_user)
        else:
            Database.update(cls._tablename, "user_verified", "1", "email", email)
    
    @classmethod
    def manager_verify(cls, email):
        temp_user = Database.find(cls._tablename, "email", email)[0]
        print(temp_user)
        if temp_user[4] == 1:
            cls.verify(temp_user)
        else:
            Database.update(cls._tablename, "manager_verified", "1", "email", email)
    
