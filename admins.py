from db import db
import users
import rooms
from sqlalchemy.sql import text

def add_admin(username):
    sql = text("INSERT INTO admins (username) VALUES (:username)")
    db.session.execute(sql, {"username":username})
    db.session.commit()
    return True