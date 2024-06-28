from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import http.client

from dbQuery import UserState, get_user_state, update_user_state
from flow1 import handle_flow_0_subflow_0, handle_flow_0_subflow_1, handle_flow_0_subflow_2, handle_flow_0_subflow_3
from flask import Flask, request, jsonify

from Config import DevelopmentConfig  # Importa la configuración que necesitas

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Utiliza la configuración del objeto

# Ahora inicializa SQLAlchemy con la app configurada
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Modelo de la tabla y otras partes de tu aplicación aquí...

# Resto del código de Flask...

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Modelo de la tabla log

def ordenar_por_fecha_y_hora(registros):
    registros_ordenados = sorted(registros, key=lambda x: x.fecha, reverse=True)
    return registros_ordenados
with app.app_context():  # Crear la tabla si no existe
    db.create_all()
    # t1= Log(texto = "Test1")
    # t2= Log(texto = "Test2", number = "XXXXXXXXX")
    # db.session.add(t1)
    # db.session.add(t2)
    # db.session.commit()





mensajes_log = []


# Función para agregar mensajes y guardar en la base de datos
def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
    nuevo_registro = UserState(texto=texto)  # Guardar el mensaje en la base de datos
    db.session.add(nuevo_registro)
    db.session.commit()


mensajes_log2 = []
number_log2 = []


# Función para agregar mensajes y guardar en la base de datos
def agregar_txt_num_log(texto, number, flow):
    mensajes_log2.append(texto)
    number_log2.append(number)
    nuevo_registro = UserState(texto=texto, number=number, flow=flow)  # Guardar el mensaje en la base de datos
    db.session.add(nuevo_registro)
    db.session.commit()


# variables globales
flow = 0
dni = ""
full_name = ""
name = ""
client = ""
sucursal = ""

# Token de verificación para la configuración
TOKEN = "TOKENX"





def recibir_mensaje(req):
    try:
        req = request.get_json()
        entry = req['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        objeto_mensaje = value['messages']


        if objeto_mensaje:
            messages = objeto_mensaje[0]

            if "type" in messages:
                tipo = messages["type"]
                # agregar_mensajes_log(json.dumps(messages))  #Guardar log en base de datos

                if tipo == "interactive":
                    tipo_interactivo = messages["interactive"]["type"]

                    if tipo_interactivo == "button_reply":
                        texto = messages["interactive"]["button_reply"]["id"]
                        numero = messages["from"]
                        send_txt(texto, numero)
                        # return 0

                    elif tipo_interactivo == "list_reply":
                        texto = messages["interactive"]["list_reply"]["id"]
                        numero = messages["from"]
                        send_txt(texto, numero)


                if "text" in messages:
                    texto = messages["text"]["body"]
                    numero = messages["from"]
                    send_txt(texto, numero)
                    # agregar_mensajes_log(json.dumps(texto))
                    # agregar_mensajes_log(json.dumps(numero))


        # agregar_mensajes_log(json.dumps(objeto_mensaje))
        return jsonify({'message': 'EVENT_RECEIVED'})
    except Exception as e:
        return jsonify({'message': 'EVENT_RECEIVED'})


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





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    # app.run(debug=True)

# Commands to push to production
# git add .
# git commit -m "xxx"
#  git push