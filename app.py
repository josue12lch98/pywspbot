from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import http.client

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Modelo de la tabla log
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.TEXT, unique=True, nullable=False)
    flow = db.Column(db.Integer, default=0)
    subFlow=db.Column(db.Integer, default=0)
    dni = db.Column(db.TEXT)
    full_name = db.Column(db.TEXT)
    client = db.Column(db.TEXT)
    sucursal = db.Column(db.TEXT)
def get_user_state(number):
    return Log.query.filter_by(number=number).first()
def update_user_state(number, **kwargs):
    user_state = get_user_state(number)
    if not user_state:
        user_state = Log(number=number)
        db.session.add(user_state)
    for key, value in kwargs.items():
        setattr(user_state, key, value)
    db.session.commit()


with app.app_context():  # Crear la tabla si no existe
    db.create_all()
    # t1= Log(texto = "Test1")
    # t2= Log(texto = "Test2", number = "XXXXXXXXX")
    # db.session.add(t1)
    # db.session.add(t2)
    # db.session.commit()

def get_last_flow(number):
    try:
        # Filtra los registros por el número dado y ordena por fecha y hora en orden descendente
        last_log = Log.query.filter_by(number=number).order_by(Log.fecha_y_hora.desc()).first()
        if last_log:
            # Si encuentra un registro, devuelve el valor de flow en formato JSON
            return jsonify({"flow": last_log.flow}), 200
        else:
            # Si no encuentra registros para ese número, devuelve un mensaje adecuado
            return jsonify({"message": "No logs found for the specified number"}), 404
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la consulta
        return jsonify({"error": str(e)}), 500
def ordenar_por_fecha_y_hora(registros):  # Función para ordenar los registros por fecha y hora
    # return sorted(registros, key = lambda x: x.id, reverse = False) # Para invertir orden de id
    return sorted(registros, key=lambda x: x.fecha_y_hora, reverse=True)


@app.route('/')
def index():
    # Obtener todos los registros de la base de datos
    registros = Log.query.all()
    registros_ordenados = ordenar_por_fecha_y_hora(registros)
    return render_template('index.html', registros=registros_ordenados);


mensajes_log = []


# Función para agregar mensajes y guardar en la base de datos
def agregar_mensajes_log(texto):
    mensajes_log.append(texto)
    nuevo_registro = Log(texto=texto)  # Guardar el mensaje en la base de datos
    db.session.add(nuevo_registro)
    db.session.commit()


mensajes_log2 = []
number_log2 = []


# Función para agregar mensajes y guardar en la base de datos
def agregar_txt_num_log(texto, number, flow):
    mensajes_log2.append(texto)
    number_log2.append(number)
    nuevo_registro = Log(texto=texto, number=number, flow=flow)  # Guardar el mensaje en la base de datos
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


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        challenge = verificar_token(request)
        return challenge
    elif request.method == 'POST':
        response = recibir_mensaje(request)
        return response


def verificar_token(req):
    token = req.args.get('hub.verify_token')
    challenge = req.args.get('hub.challenge')
    if challenge and token == TOKEN:
        return challenge
    else:
        return jsonify({'error': 'Token Invalido'}), 401


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

def find_last_flow_by_number(number):
    try:
        last_log = Log.query.filter_by(number=number).order_by(Log.fecha_y_hora.desc()).first()
        if last_log:
            return last_log.flow
        else:
            return None
    except Exception as e:
        print("Error retrieving last flow: ", str(e))
        return None
# Ciclo entrada
def send_txt(texto, numero, flow):
    texto = texto.lower()
    user_state = get_user_state(numero)
    if user_state is None:
        user_state = update_user_state(numero, flow=0,subFlow=0)

    match user_state.flow:
        case 0:
            match user_state.subFlow:
                case 0:
                    data = {
                        "messaging_product": "whatsapp",
                        "recipient_type": "individual",
                        "to": numero,
                        "text": {
                            "preview_url": False,
                            "body": "Hola! 😃 Te saluda Robotín, asistente virtual G4S que ha sido creado para absolver las dudas generales de todos los colaboradores G4S Perú \n Para ayudarte de la mejor manera, por favor detállame tu número de DNI (Ejemplo: 758152334)"
                        }
                    }
                    subFlow = 1
                    update_user_state( number=numero, subFlow=subFlow)


                case 1:
                    try:
                        int(texto)
                        data = {
                            "messaging_product": "whatsapp",
                            "recipient_type": "individual",
                            "to": numero,
                            "text": {
                                "preview_url": False,
                                "body": "Así mismo, bríndame tu nombre completo (Ejemplo: Juan Luis Perez Gonzales)"
                            }
                        }
                        dni = texto
                        subFlow = 1
                        update_user_state( number=numero, subFlow=subFlow, dni=dni)
                    except Exception as e:
                        msgerror = "Disculpa tú numero de dni no parece válido. Ingresaste: " + texto + " Ingresa sólo el número de tu DNI"
                        data = {
                            "messaging_product": "whatsapp",
                            "recipient_type": "individual",
                            "to": numero,
                            "text": {
                                "preview_url": False,
                                "body": msgerror
                            }
                        }
                case 2:  # Consultar si se puede hacer lista
                    full_name = texto
                    name = texto.split()[0]
                    msg = name + " Un gusto de conocerte por este medio (...), ¿Puedes comentarme, a qué cliente estás asignado? (Ejemplo: BCP)"
                    data = {
                        "messaging_product": "whatsapp",
                        "recipient_type": "individual",
                        "to": numero,
                        "text": {
                            "preview_url": False,
                            "body": msg
                        }
                    }
                    client = name
                    flow = 3
                    update_user_state( number=numero, flow=flow)

                case 3:
                    msg = "Finalmente, detállame a qué sucursal perteneces " + name + " (Ejemplos: Lima Sur, Arequipa, Chiclayo)"
                    # Colocar excepcion para cuando está asignado a clientes que no maneja G4S pending
                    data = {
                        "messaging_product": "whatsapp",
                        "recipient_type": "individual",
                        "to": numero,
                        "text": {
                            "preview_url": False,
                            "body": msg
                        }
                    }
                    flow = 4

                    update_user_state( number=numero, flow=flow)
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    # app.run(debug=True)

# Commands to push to production
# git add .
# git commit -m "xxx"
#  git push