from models.event import *
import datetime

event_1 = Event(datetime.date(2020, 5, 17), "wedding", 2, "tesco", "meet me at the yellow stickers", False)
event_2 = Event(datetime.date(2023, 6, 1), "funeral", 13, "mcdonalds", "its what he would have wanted", True)

events = [event_1, event_2]

def add_new_event(event):
    events.append(event)

def delete_event(event):
    events.remove(event)



