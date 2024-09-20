from app import app
from flask import render_template, request, redirect
import messages
import users
import rooms
from flask import Flask, redirect, session


@app.route("/")
def index():
    list = rooms.room_list()
    count = len(list)
    return render_template("index.html", count=count, rooms=list)

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
    count = len(messages_list)
    return render_template("messages.html", messages=messages_list, room_name=room_name, count=count, room_id=room_id)








