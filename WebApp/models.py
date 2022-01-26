from WebApp import db
from datetime import datetime

# Struktura bazy danych
"""
Docstringi
"""


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    comment = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return '<User {}>'.format(self.id)

class Dodawanie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    liczba1 = db.Column(db.Text)
    liczba2 = db.Column(db.Text)
    wynik = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return f'{self.liczba1}+{self.liczba2}={self.wynik}, '

