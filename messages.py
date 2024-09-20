from db import db
import users
import rooms
from sqlalchemy.sql import text


def get_list(room_id):
    sql = text("SELECT DISTINCT M.content, U.username, M.sent_at, M.room_id FROM messages M, users U, rooms R WHERE M.user_id=U.id AND M.room_id= :room_id ORDER BY M.sent_at DESC")
    result = db.session.execute(sql, {"room_id": room_id})
    return result.fetchall()

def send(content, room_id):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, room_id, sent_at) VALUES (:content, :user_id, :room_id, NOW())")
    db.session.execute(sql, {"content":content, "user_id":user_id, "room_id": room_id})
    db.session.commit()
    return True





