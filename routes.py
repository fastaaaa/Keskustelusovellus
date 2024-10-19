from app import app
from flask import render_template, request, redirect
import messages
import users
import rooms
import admins
import info
from flask import Flask, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy.sql import text
from models import User, Admin

@app.route("/")
def index():
    list = rooms.room_list()
    hox = info.get_info()
    count = len(list)
    username = session.get("username")
    admin_user = False
    if username:
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            admin_user = True
    user_id = session.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    if not user:
         return render_template("login.html")
    else:  
        return render_template("index.html", count=count, rooms=list, info=hox, admin_user=admin_user)

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    room_id = request.form["room_id"]
    if messages.send(content, room_id):
        return redirect(f"/room/{room_id}/messages")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")
            
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        other_user = User.query.filter_by(username=username).first()
        if other_user:
            return render_template("error.html", message="Valitsemasi käyttäjätunnus on jo käytössä")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/new/<int:room_id>")
def new(room_id):
    return render_template("new.html", room_id=room_id)

@app.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    room_id = rooms.send_room(name)
    if room_id:
        return redirect(f"/new/{room_id}")
    else:
        return render_template("error.html", message="Alueen luominen ei onnistunut")
    
@app.route("/room/<int:room_id>/messages")
def room_messages(room_id):
    messages_list = messages.get_list(room_id)
    room_name = rooms.get_room_name(room_id)
    username = session.get("username")
    count = len(messages_list)
    admin_user = False
    if username:
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            admin_user = True
            print(f"{username} is an admin")
        else:
            print(f"{username} is not an admin")
    return render_template("messages.html", messages=messages_list, room_name=room_name, count=count, room_id=room_id, admin_user=admin_user)

@app.route("/search")
def search():
    query = request.args["query"]
    sql = text("SELECT M.id, M.content, M.room_id, M.visible, R.visible, R.name AS room_name FROM messages M, rooms R WHERE M.content LIKE :query AND M.room_id = R.id AND M.visible = TRUE AND R.visible = TRUE")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    count = len(messages)
    return render_template("search.html", messages=messages, count=count)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    user_id = session.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return render_template("error.html", message="Kirjaudu sisään nähdäksesi tämän sivun")
    if request.method == "GET":
        admin_user = Admin.query.filter_by(username=user.username).first()
        if admin_user:
            return render_template("admin.html", user_id=user_id, admin_user=admin_user, username=user.username)
        else:
            return render_template("error.html", message="Sinulla ei ole tarvittavia käyttöoikeuksia tälle sivulle")
    if request.method == "POST":
        username = request.form["username"]
        user = User.query.filter_by(username=username).first()
        if user:
            admin = Admin.query.filter_by(username=username).first()
            if not admin:
                new = Admin(username=username)
                db.session.add(new)
                db.session.commit()
                flash(f"Käyttäjä {username} lisätty ylläpitäjäksi")
            else: 
                flash(f"Käyttäjän {username} lisäys ylläpitäjäksi epäonnistui")
        else:
            flash(f"Käyttäjän {username} lisäys ylläpitäjäksi epäonnistui")
        return redirect("/admin")
    
@app.route("/delete", methods=["POST"])
def delete_message():
    id = request.form["id"]
    room_id = request.form["room_id"]
    messages.delete_message(id)
    return redirect(f"/room/{room_id}/messages")

@app.route("/delete_room", methods=["POST"])
def delete_room():
    room_id = request.form["room_id"]
    print(f"Deleting room with ID: {room_id}") 
    messages.delete_room_messages(room_id)
    rooms.delete_room(room_id)
    print(f"Room {room_id} deleted.")
    return redirect("/")

@app.route("/send_info", methods=["POST"])
def send_info():
    content = request.form["content"]
    if info.send_info(content):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")
   






