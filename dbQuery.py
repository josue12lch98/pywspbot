from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import http.client

from app import db
from flow1 import handle_flow_0_subflow_0, handle_flow_0_subflow_1, handle_flow_0_subflow_2, handle_flow_0_subflow_3

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




# Ciclo entrada
def send_txt(texto, numero):
    texto = texto.lower()
    user_state = get_user_state(numero)
    if user_state is None:
        update_user_state(numero, flow=0,subFlow=0)
        user_state = get_user_state(numero)

    match user_state.flow:
        case 0:
            match user_state.subFlow:
                case 0:
                    handle_flow_0_subflow_0(numero)


                case 1:
                    handle_flow_0_subflow_1(numero, texto)
                case 2:  # Consultar si se puede hacer lista
                    handle_flow_0_subflow_2(numero, texto)

                case 3:
                    handle_flow_0_subflow_3(numero, texto)
        case 4:
            """                
            if texto != "": 
                msg = "¡Listo " + name + " Gracias por confirmar tu DNI: " + dni + ", sucursal a la que perteneces: " + sucursal + " y al cliente: " + client + ", al que estás asignado. \n Para continuar, necesito que me confirmes que tus datos son los correctos."
                data = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": numero,
                    "text": {
                        "preview_url": False,
                        "body": msg
                    }
                }
                flow = 5    
            """
            msg = "¡Listo " + name + " Gracias por confirmar tu DNI: " + dni + ", sucursal a la que perteneces: " + sucursal + " y al cliente: " + client + ", al que estás asignado. \n Para continuar, necesito que me confirmes que tus datos son los correctos."
            data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": numero,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": msg
                    },
                    "footer": {
                        "text": "Selecciona una de las opciones"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "btnsi",
                                    "title": "Si"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "btnno",
                                    "title": "No"
                                }
                            }
                        ]
                    }
                }
            }
            flow = 5
        case 5:
            if "btnsi" in texto:
                data = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": numero,
                    "text": {
                        "preview_url": False,
                        "body": "Nice"
                    }
                }
            else:
                data = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": numero,
                    "text": {
                        "preview_url": False,
                        "body": "Indicame tus datos nuevamente"
                    }
                }
                flow = 0


def ordenar_por_fecha_y_hora(registros):
    registros_ordenados = sorted(registros, key=lambda x: x.fecha, reverse=True)
    return registros_ordenados
def generic_reply(data):
    data = json.dumps(data)  # Convertir el diccionario en formato JSON

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EAAV8kZCQDeLkBOwQu1NSf9nGRs5AxW1ZBT9NyjzA1aHTC0ZAZColXU5Resu79lwawwLHn0VlHT7BkIIIEz2USl4pHLjOATxu803wFWPpKs6kyoaDEzZCYBwJjkuXjw2V0o5XZCVbirxI3xcKXcCaQZBi92aQpkafFFGI3oTGuHXwugmf44ZAUXMS1aoezS9i9Lg3LxW1OA72uZACxUZCFzdaoZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v20.0/357679540758058/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(json.dumps(e))
    finally:
        connection.close()

def generic_reply(data):
    data = json.dumps(data)  # Convertir el diccionario en formato JSON

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EAAV8kZCQDeLkBO7zt2MHThLR9X9V7OK75TnsYprLwLos8sbv1sreKraudfBRwVHZBZBpt9PESJ4m974NH6fZBew8p0RAZBNxEBjSEONYjjWZBmNIQIms38XHIFlK4r7ChWOasPq4W0uZCJEXJ4X0CajyGbzC08z8kz2UZAZApdHIcNpiiEGwZCHZBUBVt3F9qaWHhXhEK3gPduiudoWDmYKAYgZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v20.0/357679540758058/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(json.dumps(e))
    finally:
        connection.close()

mensajes_log = []


def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
    nuevo_registro = UserState(texto=texto)  # Guardar el mensaje en la base de datos
    db.session.add(nuevo_registro)
    db.session.commit()




# Commands to push to production
# git add .
# git commit -m "xxx"
#  git push