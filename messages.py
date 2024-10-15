from db import db
import users
import rooms
from sqlalchemy.sql import text
from flask import session


def get_list(room_id):
    sql = text("SELECT DISTINCT M.content, U.username, M.sent_at, M.room_id, M.id, U.id, M.visible, M.user_id FROM messages M, users U, rooms R WHERE M.user_id=U.id AND M.room_id= :room_id AND M.visible = TRUE ORDER BY M.sent_at DESC")
    result = db.session.execute(sql, {"room_id": room_id})
    return result.fetchall()

def send(content, room_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, room_id, sent_at, visible) VALUES (:content, :user_id, :room_id, NOW(), TRUE)")
    db.session.execute(sql, {"content":content, "user_id":user_id, "room_id": room_id})
    db.session.commit()
    return True

def delete_message(id):
    sql = text("UPDATE messages SET visible=FALSE WHERE id = :id")
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def delete_room_messages(room_id):
    sql = text("UPDATE messages SET visible=FALSE WHERE room_id = :room_id")
    db.session.execute(sql, {"room_id":room_id})
    db.session.commit()
    return True





