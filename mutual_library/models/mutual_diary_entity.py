import mysql.connector
from mysql.connector import errorcode
from db import db

class mutual_diary_entity(db.Model):
    __tablename__ = 'mutual_diary_entity'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    idmutualdiary = db.Column(db.Integer, db.ForeignKey('mutal_diary.id'))
    memoryname = db.Column(db.VARCHAR(50))
    memory_note = db.Column(db.VARCHAR(750))
    photoaddress = db.Column(db.VARCHAR(300))
    maplocation = db.Column(db.VARCHAR(300))
    date = db.Column(db.Date)


    def __init__(self, _id, idmutualdiary, memoryname, memorynote, photoaddress, maplocation, date):
        self.id = _id
        self.idmutualdiary = idmutualdiary
        self.memorname = memoryname
        self.memorynote = memorynote
        self.photoaddress = photoaddress
        self.maplocation = maplocation
        self.date = date