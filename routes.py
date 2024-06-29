from flask import  request, jsonify, render_template
import json

from dbQuery import UserState, get_user_state, update_user_state
from flow0 import handle_flow_0_subflow_0, handle_flow_0_subflow_1, handle_flow_0_subflow_2, handle_flow_0_subflow_3
from flow1 import *

def init_app(app):
    @app.route('/')
    def index():
        # Obtener todos los registros de la base de datos
        registros = UserState.query.all()
        return render_template('index.html', registros=registros);

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
        if challenge and token == 'token': #Reemplazar con variable de entorno
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
                    
                    if tipo == "interactive":
                        tipo_interactivo = messages["interactive"]["type"]

                        if tipo_interactivo == "button_reply":
                            texto = messages["interactive"]["button_reply"]["id"]
                            numero = messages["from"]
                            flow_ = int(texto.split()[0])
                            subflow_ = int(texto.split()[1])
                            update_user_state(number = numero, flow = flow_, subFlow = subflow_, json = json.dumps(req))
                            send_txt(texto, numero)
                            
                        elif tipo_interactivo == "list_reply":
                            texto = messages["interactive"]["list_reply"]["id"]
                            numero = messages["from"]
                            update_user_state(number = numero, json = json.dumps(req))
                            send_txt(texto, numero)
                            
                    if "text" in messages:
                        texto = messages["text"]["body"]
                        numero = messages["from"]
                        update_user_state(number = numero, json = json.dumps(req))
                        send_txt(texto, numero)
                        
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
                case 2:  
                    handle_flow_0_subflow_2(numero, texto)
                case 3:
                    name = user_state.full_name
                    dni = user_state.dni
                    handle_flow_0_subflow_3(numero, texto, name, dni)  
                case _:
                    print("")
                    
        case 1:
            match user_state.subFlow:
                case 0:
                    name = user_state.full_name
                    name = name.split()[0]
                    handle_flow_1_subflow_0(numero, name.capitalize())
                case 1:
                    handle_flow_1_subflow_1(numero)
                case _:
                    print("")
        case _:
            print("")
