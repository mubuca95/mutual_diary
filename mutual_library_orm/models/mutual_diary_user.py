import mysql.connector
from mysql.connector import errorcode
from sqlalchemy.sql.schema import ForeignKey
from db import db

class mutual_diary_user(db.Model):
    __tablename__ = 'mutual_diary_user'
    iduser = db.Column(db.Integer, foreign_key = True)
    iddiary = db.Column(db.Integer, foreign_key = True)

    def __init__(self, iduser, iddiary):
        self.iduser = iddiary
        self.iddiary = iddiary