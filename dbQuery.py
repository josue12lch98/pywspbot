from flask import Flask
from __init__ import db
import json
import http.client


app = Flask(__name__)

class UserState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.TEXT, unique=True, nullable=False)
    flow = db.Column(db.Integer, default=0)
    subFlow=db.Column(db.Integer, default=0)
    dni = db.Column(db.TEXT)
    full_name = db.Column(db.TEXT)
    client = db.Column(db.TEXT)
    sucursal = db.Column(db.TEXT)
    
def get_user_state(number):
    return UserState.query.filter_by(number=number).first()

def update_user_state( number , **kwargs):
    user_state = get_user_state(number)
    if not user_state:
        user_state = UserState(number=number)
        db.session.add(user_state)
    for key, value in kwargs.items():
        setattr(user_state, key, value)
        db.session.commit()

def generic_reply(data):
    data = json.dumps(data)  # Convertir el diccionario en formato JSON

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EAAOdZCMIRR5IBO8y5ddn9PgPRdTMmlk5yA0vZC0jofUDAH2VqiCGFI5T74snjDJJOsX5iRm5tf0kMA5EityYN7ivWpNLyfreRL0ib7DU2rc1eZAZB92XZCZAaL2ZA79ZCkBb8ZAXbkOnPbbZBUaEULC50fnHodQr8TXVRJwhJfohZAqAIDevg4QksuDt15cVMD9Rx0yz2rUZBDf9zVnZBzHlMiIJP"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v19.0/378273298696469/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        print(e)
    finally:
        connection.close()
