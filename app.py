from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

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
    #prueba1 = Log(texto = 'Mensaje de Prueba 1')
    #prueba2 = Log(texto = 'Mensaje de Prueba 2')
    #db.session.add(prueba1)
    #db.session.add(prueba2)
    #db.session.commit()

# Función para ordenar los registros por fecha y hora
def ordenar_por_fecha_y_hora(registros):
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
TOKEN_SS = "SOFTWARESOLUTIONS"

@app.route('/webhook', methods = ['GET', 'POST'])
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
    if challenge and token == TOKEN_SS:
        return jsonify({'message':'Token Correcto'}),401 #challenge
    else:
        return jsonify({'error':'Token Invalido'}),401

def recibir_mensajes(req):
    req = request.get_json()
    agregar_mensajes_log(req)
    return jsonify({'message':'EVENT_RECEIVED'})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(debug=True)
    # git add .
    # git commit -m "xxx"
    # git push