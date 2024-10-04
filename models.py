from flask_sqlalchemy import SQLAlchemy
from db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)