from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import events, add_new_event, delete_event

@app.route('/')
def index():
    return render_template("index.html", title="Randolph")

@app.route("/events")
def show_tasks():
    return render_template("index.html", event_list = events)

@app.route("/events", methods=["POST"])
def add_event():
    name = request.form["name"]
    description = request.form["description"]
    room_location = request.form["room_location"]
    num_guests = request.form["num_guests"]
    date = request.form["date"]
    if "recurring" in request.form:
        recurring = request.form["recurring"]
    new_event = Event(name, description, room_location, num_guests, date, recurring)
    add_new_event(new_event)
    return render_template("index.html", event_list=events)

@app.route("/events/delete/<index>", methods=["POST"])
def remove_event(index):
    delete_event(index)
    return render_template("index.html")

# , item = events(index)
