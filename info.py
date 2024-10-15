from db import db
import users
import rooms
from sqlalchemy.sql import text
from flask import session

def get_info():
    sql = text("SELECT I.content, U.username, I.sent_at, I.visible FROM info I, users U WHERE visible = TRUE AND I.user_id = U.id ORDER BY I.id DESC LIMIT 1")
    result = db.session.execute(sql)
    return result.fetchall()

def send_info(content):
    user_id = users.user_id()
    sql = text("INSERT INTO info (content, user_id, sent_at, visible) VALUES (:content, :user_id, NOW(), TRUE)")
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return True

def delete_info(id):
    sql = text("UPDATE info SET visible=FALSE WHERE id = :id")
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True