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
    thirdFlow=db.Column(db.Integer, default=0)
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
        "Authorization": "Bearer EAAV8kZCQDeLkBO4bpDntLWRvLuapcPeZBDvSZCPWkQ0xREDZCqr03NX61rZBJKnYh3o2JZAZB3Kqbj9g1yshfZAcwEscI2GpFiZBEFp3pDFMigk84seaKBVFYhzlMVqYWBJOoOlhnSEMwSoQx4Q61pX89B5QIjWLlkR08rzgPoCrQDWCBXivAwM1OVDj2yQqMyTTY46dzmiVb9u07oPmR2CEZD"
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