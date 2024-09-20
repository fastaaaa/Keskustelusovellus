from db import db
import messages
from sqlalchemy.sql import text


def room_list():
    sql = text("SELECT id, name FROM rooms ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def send_room(name):
    sql = text("INSERT INTO rooms (name) VALUES (:name) RETURNING id")
    x = db.session.execute(sql, {"name":name})
    room_id = x.fetchone()[0]
    db.session.commit()
    return room_id

def get_room_name(room_id):
    sql = text("SELECT name FROM rooms WHERE id = :id")
    result = db.session.execute(sql, {"id": room_id})
    return result.scalar()