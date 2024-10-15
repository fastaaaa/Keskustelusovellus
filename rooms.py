from db import db
import messages
from sqlalchemy.sql import text
from flask import session


def room_list():
    sql = text("SELECT id, name, visible FROM rooms WHERE visible = TRUE ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def send_room(name):
    sql = text("INSERT INTO rooms (name, visible) VALUES (:name, TRUE) RETURNING id")
    result = db.session.execute(sql, {"name":name})
    room_id = result.fetchone()[0]
    db.session.commit()
    return room_id

def get_room_name(room_id):
    sql = text("SELECT name FROM rooms WHERE id = :id")
    result = db.session.execute(sql, {"id": room_id})
    return result.scalar()

def delete_room(room_id):
    sql = text("UPDATE rooms SET visible=FALSE WHERE id = :room_id")
    db.session.execute(sql, {"room_id":room_id})
    db.session.commit()
    return True
