from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")


import routes




