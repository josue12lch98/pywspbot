from flask import Flask
from __init__ import db
import json
import http.client
import inspect

app = Flask(__name__)

class UserState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.TEXT, unique=True, nullable=False)
    flow = db.Column(db.Integer, default=0)
    subFlow=db.Column(db.Integer, default=0)
    subFlow2=db.Column(db.Integer, default=0)
    subFlow3=db.Column(db.Integer, default=0)
    subFlow4=db.Column(db.Integer, default=0)
    subFlow5=db.Column(db.Integer, default=0)
    subFlow6=db.Column(db.Integer, default=0)
    dni = db.Column(db.TEXT)
    full_name = db.Column(db.TEXT)
    sucursal = db.Column(db.TEXT)
    json = db.Column(db.TEXT)
    func = db.Column(db.TEXT, default="")
    Flag_b= db.Column(db.TEXT, default="")
    clientAssigned = db.Column(db.TEXT, default="")



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
        "Authorization": "Bearer EAAV8kZCQDeLkBOZCXOZBZAECAfpj82XlNbKcScj0C2xgyaSa4jxWqG3mjY09CafWhMZBgBreiSrOF2xuipmMsXZBW8INRTrum4Cbu1lgocdUaEcWACQdEKQVG8JXHZAZCTKFvweBmkUXh5wmfoNHSGZC7k8JGLODZAuA4Oyu7ioTE8l2luUEeSO1Y2bDZAPsgeyLRLIZAIbGXxeZBNRxzk2SNfEMZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v20.0/357679540758058/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        print(e)
    finally:
        connection.close()






# Commands to push to production
# git add .
# git commit -m "xxx"
#  git push