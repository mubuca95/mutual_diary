import mysql.connector
from mysql.connector import errorcode
from db import db


class mutual_diary(db.Model):
    __tablename__ = 'mutual_diary'
    id = db.Column(db.Integer, PRIMARY_KEY = True,autoincrement=True)
    diaryname = db.Column(db.VARCHAR(50))
    shortdescription = db.Column(db.VARCHAR(240))
    datecreated = db.Column(db.TIMESTAMP)
    isactive = db.Column(db.BOOLEAN)


    def __init__(self, id, diaryname, shortdescription, datecreated, isactive):
        self.id = id
        self.diaryname = diaryname
        self.shortdescription = shortdescription
        self.datecreated = datecreated
        self.isactive = isactive
