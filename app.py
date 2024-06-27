from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import http.client

app = Flask(__name__)

#Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metapython.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de la tabla log
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_y_hora = db.Column(db.DateTime, default = datetime.utcnow)
    texto = db.Column(db.TEXT)
    number = db.Column(db.TEXT)

with app.app_context():   # Crear la tabla si no existe
    db.create_all()
    #t1= Log(texto = "Test1")
    #t2= Log(texto = "Test2", number = "XXXXXXXXX")
    #db.session.add(t1)
    #db.session.add(t2)
    #db.session.commit()

def ordenar_por_fecha_y_hora(registros): # Función para ordenar los registros por fecha y hora
    #return sorted(registros, key = lambda x: x.id, reverse = False) # Para invertir orden de id
    return sorted(registros, key = lambda x: x.fecha_y_hora, reverse = True)

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
    nuevo_registro = Log(texto=texto) # Guardar el mensaje en la base de datos
    db.session.add(nuevo_registro)
    db.session.commit()
    
mensajes_log2 = []
number_log2 = []
# Función para agregar mensajes y guardar en la base de datos
def agregar_txt_num_log(texto, number):
    mensajes_log2.append(texto)
    number_log2.append(number)
    nuevo_registro = Log(texto = texto, number = number) # Guardar el mensaje en la base de datos
    db.session.add(nuevo_registro)
    db.session.commit()



# Token de verificación para la configuración
TOKEN = "TOKENX"

@app.route('/webhook', methods=['GET','POST'])

def webhook():
    if request.method == 'GET':
        challenge = verificar_token(request)
        return challenge
    elif request.method == 'POST':
        response = recibir_mensajes(request)
        return response

def verificar_token(req):
    token = req.args.get('hub.verify_token')
    challenge = req.args.get('hub.challenge')
    if challenge and token == TOKEN:
        return challenge
    else:
        return jsonify({'error':'Token Invalido'}),401

def recibir_mensajes(req):
    try:
        req = request.get_json()
        entry = req['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        objeto_mensaje = value['messages']

        if objeto_mensaje:
            messages = objeto_mensaje[0]
            
            if  "type" in messages:
                tipo = messages["type"]
                #agregar_mensajes_log(json.dumps(messages))  #Guardar log en base de datos
                
                if tipo == "interactive":
                    tipo_interactivo  = messages["interactive"]["type"]
                    
                    if tipo_interactivo == "button_reply":
                        texto = messages["interactive"]["button_reply"]["id"]
                        numero = messages["from"]
                        enviar_mensajes_wsp(texto, numero)
                        #return 0
                    
                    elif tipo_interactivo == "list_reply":
                        texto = messages["interactive"]["list_reply"]["id"]
                        numero = messages["from"]
                        enviar_mensajes_wsp(texto, numero)
                    agregar_mensajes_log(json.dumps(messages))  #Guardar log en base de datos

                if "text" in messages:
                    texto = messages["text"]["body"]
                    numero = messages["from"]

                    enviar_mensajes_wsp(texto, numero)
                    #agregar_mensajes_log(json.dumps(texto))
                    #agregar_mensajes_log(json.dumps(numero))
                    agregar_txt_num_log(json.dumps(messages), numero)  #Guardar log en base de datos
        
        #agregar_mensajes_log(json.dumps(objeto_mensaje))
        return jsonify({'message':'EVENT_RECEIVED'})
    except Exception as e:
        return jsonify({'message':'EVENT_RECEIVED'})

def enviar_mensajes_wsp(texto, numero):
    texto = texto.lower()

    if "hola" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "🤖 Hola, ¿Cómo estas? Bienvenido."
            }
        }
    elif "1" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "Lore Ipsum"
            }
        }
    elif "2" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "location",
            "location": {
                "latitude": "-12.054347540574366", 
                "longitude": "-77.03943293543378",
                "name": "KDN4 Software Solutions",
                "address": "Jr. Washington 1206"
            }
        }
    elif "3" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "document",
            "document": {
                "link": "https://www.renfe.com/content/dam/renfe/es/General/PDF-y-otros/Ejemplo-de-descarga-pdf.pdf",
                "caption": "Ejemplo de PDF"
            }
        }
    elif "4" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "audio",
            "audio": {
                "link": "https://filesamples.com/samples/audio/mp3/sample1.mp3",
            }
        }
    elif "5" in texto:
        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "text": {
                "preview_url" : True,
                "body" : "Introducción al curso! XXXXXXXXX"
            }
        }
    elif "6" in texto:
        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "text": {
                "preview_url" : False,
                "body" : "🤝 En breve me pondré en contacto contigo."
            }
        }
    elif "7" in texto:
        data = {
            "messaging_product": "whatsapp",
            "to": numero,
            "text": {
                "preview_url" : False,
                "body" : "El horario de atención: Lunes a Viernes (9:00 AM - 17:00 PM)"
            }
        }
    elif "0" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, visita mi Github https://github.com/m1guel17 para más información.\n \n📌Por favor, ingresa un número #️⃣ para recibir información.\n \n1️⃣. Información del Curso. ❔\n2️⃣. Ubicación del local. 📍\n3️⃣. Enviar temario en PDF. 📄\n4️⃣. Audio explicando curso. 🎧\n5️⃣. Video de Introducción. ⏯️\n6️⃣. Hablar con Miguel. 🙋‍♂️\n7️⃣. Horario de Atención. 🕜 \n0️⃣. Regresar al Menú. 🔄"
            }
        }
    elif "button" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "¿Confirmas tu registro?"
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
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "btntalvez",
                                "title": "Tal vez"
                            }
                        }
                    ]
                }
            }
        }
    elif "btnsi" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Muchas Gracias por aceptar"
            }
        }
    elif "btnno" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Es una lástima"
            }
        }
    elif "btntalvez" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Estaré a la espera"
            }
        }
    elif "lista" in texto:
        data = {
            "messaging_product": "whatsapp",
            #"recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Selecciona alguna opción"
                },
                "footer": {
                    "text": "Selecciona alguna de las opciones para poder ayudarte"
                },
                "action":{
                    "button": "Ver Opciones",
                    "sections": [
                        {
                            "title": "Compra y Venta",
                            "rows": [
                                {
                                    "id": "btncompra",
                                    "title": "Comprar",
                                    "description": "Compra los mejores artículos de tecnología"
                                },
                                {
                                    "id": "btnvender",
                                    "title": "Vender",
                                    "description": "Vende lo que ya no estés usando"
                                }
                            ]
                        },
                        {
                            "title": "Distribución y Entrega",
                            "rows": [
                                {
                                    "id": "btndireccion",
                                    "title": "Local",
                                    "description": "Puedes visistar nuestro local."
                                },
                                {
                                    "id": "btnentrega",
                                    "title": "Entrega",
                                    "description": "La entrega se realiza todo los dias."
                                }
                            ]
                        }
                    ]
                }
            }
        }
    elif "btncompra" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Los mejores artículos top en ofertas."
            }
        }
    elif "btnvender" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Excelente elección."
            }
        }
    elif "btndireccion" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "La dirección es la siguiente."
            }
        }
    elif "btnentrega" in texto:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "La entrega son los días miercoles en oficina."
            }
        }
    else:
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "🚀 Hola, visita mi Github https://github.com/m1guel17 para más información.\n \n📌Por favor, ingresa un número #️⃣ para recibir información.\n \n1️⃣. Información del Curso. ❔\n2️⃣. Ubicación del local. 📍\n3️⃣. Enviar temario en PDF. 📄\n4️⃣. Audio explicando curso. 🎧\n5️⃣. Video de Introducción. ⏯️\n6️⃣. Hablar con Miguel. 🙋‍♂️\n7️⃣. Horario de Atención. 🕜 \n0️⃣. Regresar al Menú. 🔄"
            }
        }
    data = json.dumps(data) # Convertir el diccionario en formato JSON

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer EAAV8kZCQDeLkBO7zt2MHThLR9X9V7OK75TnsYprLwLos8sbv1sreKraudfBRwVHZBZBpt9PESJ4m974NH6fZBew8p0RAZBNxEBjSEONYjjWZBmNIQIms38XHIFlK4r7ChWOasPq4W0uZCJEXJ4X0CajyGbzC08z8kz2UZAZApdHIcNpiiEGwZCHZBUBVt3F9qaWHhXhEK3gPduiudoWDmYKAYgZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST","/v20.0/357679540758058/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(json.dumps(e))
    finally:
        connection.close()


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(debug=True)

# Commands to push to production
# git add .
# git commit -m "xxx"
# git push