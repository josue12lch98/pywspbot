from flask import  request, jsonify, render_template
import json

from dbQuery import UserState, get_user_state, update_user_state
from flow0 import *
from flow1 import *
from flow1_1_ import *
from flow1_1_1 import *
from flow1_1_2_ import *
from flow1_1_2_1_ import *

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
            entry = req["entry"][0]
            changes = entry["changes"][0]
            value = changes["value"]
            objeto_mensaje = value["messages"]

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
                            subFlow2_ = int(texto.split()[2])
                            subFlow3_ = int(texto.split()[3])
                            subFlow4_ = int(texto.split()[4])
                            update_user_state(number = numero, flow = flow_, subFlow = subflow_, subFlow2 = subFlow2_, subFlow3 = subFlow3_, subFlow4 = subFlow4_)
                            send_txt(texto, numero)

                        elif tipo_interactivo == "list_reply":
                            texto = messages["interactive"]["list_reply"]["id"]
                            numero = messages["from"]
                            flow_ = int(texto.split()[0])
                            subflow_ = int(texto.split()[1])
                            subFlow2_ = int(texto.split()[2])
                            subFlow3_ = int(texto.split()[3])
                            subFlow4_ = int(texto.split()[4])
                            update_user_state(number = numero, flow = flow_, subFlow = subflow_, subFlow2 = subFlow2_, subFlow3 = subFlow3_, subFlow4 = subFlow4_)
                            send_txt(texto, numero)

                    if "text" in messages:
                        texto = messages["text"]["body"]
                        numero = messages["from"]
                        update_user_state(number = numero)
                        send_txt(texto, numero)

            return jsonify({'message': 'EVENT_RECEIVED'})
        except Exception as e:
            return jsonify({'message': 'EVENT_RECEIVED'})

# Ciclo entrada
def send_txt(texto, numero):
    texto = texto.lower()
    user_state = get_user_state(numero)
    if user_state is None:
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
                case 404:
                    handle_flow_0_subflow_404(numero)

        case 1: # Button si de confirmación de datos correctos define el cambio de flujo de 0 a 1
            match user_state.subFlow:
                case 0:
                    name = user_state.full_name
                    name = name.split()[0]
                    handle_flow_1_subflow_0(numero, name.capitalize()) # Consulta si/no problemas javelin
                case 1:
                    if user_state.subFlow2 == 0:
                        handle_flow_1_subflow_1(numero) # Lista reclamo/consulta (5 opciones)
                    else:
                        match user_state.subFlow2:
                            case 1: # 1 1 1 0 0
                                match user_state.subFlow3:
                                    case 0:
                                        handle_flow_1_subflow_1_1(numero,user_state) # Lista botones para mis pagos
                                    case 1:
                                        handle_flow_1_subflow_1_1_1(numero,user_state) # Lista botones para mis pagos
                                    case 1:
                                        handle_flow_1_subflow_1_1_2(numero, user_state)
                                    case 2:
                                        handle_flow_1_subflow_1_1_3(numero, user_state)

                            case 2:
                                if user_state.subFlow3 == 0:
                                    handle_flow_1_subflow_1_2(numero)
                                else:
                                    match user_state.subFlow3:
                                        case 1:
                                            if user_state.subFlow4 == 0:
                                                name = user_state.full_name
                                                name = name.split()[0]
                                                handle_flow_1_subflow_1_2_1(numero, name)
                                                data = {
                                                    "messaging_product": "whatsapp",
                                                    "recipient_type": "individual",
                                                    "to": numero,
                                                    "text": {
                                                        "preview_url": False,
                                                        "body":  "user_state.subFlow4" + str(user_state.subFlow4)
                                                    }
                                                }
                                                generic_reply(data)
                                            else:
                                                match user_state.subFlow4:
                                                    case 1:
                                                        handle_flow_1_subflow_1_2_1_1(numero)
                                                    case _:
                                                        handle_flow_1_subflow_1_2_1_x(numero, user_state.subFlow4)
                                        case 2:
                                            handle_flow_1_subflow_1_2_2(numero)
                                        case 3:
                                            handle_flow_1_subflow_1_2_3(numero)
                                        case 4:
                                            handle_flow_1_subflow_1_2_4(numero)
                                        case _:
                                            handle_flow_1_subflow_1_2_x(numero, user_state.subFlow3)
                            case 3:
                                handle_flow_1_subflow_1_3(numero)## Lista botones para peticiones
                            case 4:
                                handle_flow_1_subflow_1_4(numero) # Lista botones para trámites
                            case 5:
                                handle_flow_1_subflow_1_5(numero) # Lista botones para acceso a aplicaciones
                            case _:
                                print(" ")
                case 404:
                    handle_flow_1_subflow_404(numero)
        case _:
            print("")
