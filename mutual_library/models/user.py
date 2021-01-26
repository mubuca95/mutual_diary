#import mysql.connector
from mysql.connector import errorcode
from db import db



class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.VARCHAR(50))
    password = db.Column(db.VARCHAR(32))
    firstname = db.Column(db.VARCHAR(25))
    lastname = db.Column(db.VARCHAR(25))
    datecreated = db.Column(db.TIMESTAMP)
    isactive = db.Column(db.BOOLEAN)


    def __init__(self, email, password, firstname, lastname, isactive):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname      
        self.isactive = isactive
   

    @classmethod
    def find_by_email(cls, email):
        return UserModel.query.filter_by(email = email).first() # .filter_by can go on.  select * from user where email = 'email'

    @classmethod
    def find_by_id(cls, _id):
        return UserModel.quer.filter_by(id = _id).first()


    @classmethod
    def save_to_db(self):
        print(self.email)
        print(self.password)
        print(self.firstname)
        print(self.lastname)
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()