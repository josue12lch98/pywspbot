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

with app.app_context():   # Crear la tabla si no existe
    db.create_all()

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
                agregar_mensajes_log(json.dumps(tipo))  #Guardar log en base de datos
                
                if tipo == "interactive":
                    return 0
                
                if "text" in messages:
                    texto = messages["text"]["body"]
                    numero = messages["from"]

                    enviar_mensajes_wsp(texto, numero)
                    #agregar_mensajes_log(json.dumps(texto))
                    #agregar_mensajes_log(json.dumps(numero))
                    agregar_mensajes_log(json.dumps(messages))  #Guardar log en base de datos
        
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
        "Authorization" : "Bearer EAAFtbtx1eJEBO0fAejPfZCmwhT8lWsSsUnM1rqlbb0aoFkJVL6fgYZB4NErXNOc9XyedW8tX9dsxJcVN8FOEWpW0XHNZCMHhG3iZB0rBD888jeZAKMa8GriXZBLEQPSVzZBe0HwvN7Xv9O34e8WUKmhL7FmsThdjGsZCH8vuUP9ej0U8f9dyLug67h5AZCLCMy87x2atYbnlq66sZClk0cNLcD7AuVCCypu3oDIyvh"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST","/v18.0/259957250537628/messages", data, headers)
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