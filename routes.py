from time import sleep

from flask import  request, jsonify, render_template
import json

from dbQuery import UserState, get_user_state, update_user_state
from flow0 import *
from flow1 import *
from flow1_1_ import *
from flow1_1_1 import *
from flow1_1_1_1 import *
from flow1_1_2_ import *
from flow1_1_2_1_ import *
from flow1_1_2_2 import *
from flow1_1_4_1 import *
from flow1_1_5 import handle_flow_1_subflow_1_1_5


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
                            try:
                                subFlow5_ = int(texto.split()[5])
                            except Exception as e:
                                subFlow5_=0

                            update_user_state(number = numero, flow = flow_, subFlow = subflow_, subFlow2 = subFlow2_, subFlow3 = subFlow3_, subFlow4 = subFlow4_)
                            try:
                                subFlow6_ = int(texto.split()[6])
                            except Exception as e:
                                subFlow6_ = 0
                            update_user_state(number = numero, flow = flow_, subFlow = subflow_, subFlow2 = subFlow2_, subFlow3 = subFlow3_, subFlow4 = subFlow4_, subFlow5 = subFlow5_, subFlow6 = subFlow6_)
                            send_txt(texto, numero)
                            
                        elif tipo_interactivo == "list_reply":
                            texto = messages["interactive"]["list_reply"]["id"]
                            numero = messages["from"]
                            flow_ = int(texto.split()[0])
                            subflow_ = int(texto.split()[1])
                            subFlow2_ = int(texto.split()[2])
                            subFlow3_ = int(texto.split()[3])
                            subFlow4_ = int(texto.split()[4])
                            try:
                                subFlow5_ = int(texto.split()[5])
                            except Exception as e:
                                subFlow5_ = 0

                            try:
                                subFlow6_ = int(texto.split()[6])
                            except Exception as e:
                                subFlow6_ = 0
                            update_user_state(number=numero, flow=flow_, subFlow=subflow_, subFlow2=subFlow2_,
                                              subFlow3=subFlow3_, subFlow4=subFlow4_, subFlow5=subFlow5_,
                                              subFlow6=subFlow6_)
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
        update_user_state(numero, flow=0,subFlow=0,subFlow2=0,subFlow3=0,subFlow4=0,subFlow5=0, subFlow6=0)
        user_state = get_user_state(numero)

    b = user_state.Flag_b
    name=user_state.full_name.split()[0]

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
                    if user_state.subFlow2 == 0: # 1 1 0 0 0 Menú principal
                        handle_flow_1_subflow_1(numero) # Lista reclamo/consulta (5 opciones)
                    else:
                        match user_state.subFlow2:
                            case 1: # 1 1 1 0 0
                                match user_state.subFlow3:
                                    case 0:
                                        handle_flow_1_subflow_1_1(numero) # 1 1 1 0 0 -  Menú Gastos
                                    case 1:
                                        match user_state.subFlow4:
                                            case 0 :
                                                handle_flow_1_subflow_1_1_1(numero)

                                            case _:
                                                handle_database_manteniment(numero)
                                    case 2:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_2(numero)
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 3:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_3(numero)
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 4:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_4(numero, )
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 5:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_contact_asesor(numero)
                                            case _:
                                                handle_database_manteniment(numero)

                            case 2:
                                if user_state.subFlow3 == 0:
                                    handle_flow_1_subflow_1_2(numero)
                                else:
                                    match user_state.subFlow3:
                                        case 1:
                                            name = user_state.full_name
                                            name = name.split()[0]
                                            if user_state.subFlow4 == 0:
                                                handle_flow_1_subflow_1_2_1(numero, name, b) ## Encuesta  1 1 2 1 0
                                                handle_flow_1_subflow_1_2_1_1(numero)
                                            else:
                                                match user_state.subFlow4:
                                                    case 1:
                                                        match user_state.subFlow5:
                                                            case 1:
                                                                if user_state.subFlow6 == 0:
                                                                    handle_flow_1_subflow_1_2_1_1_1(numero)
                                                                else:
                                                                    match user_state.subFlow6:
                                                                        case _:
                                                                            handle_flow_1_subflow_1_2_1_1_1_1(numero)
                                                                        
                                                            case 2:
                                                                handle_flow_1_subflow_1_2_1_1_2_2(numero)
                                                            case 3:
                                                                handle_flow_1_subflow_1_2_1_1_2_3(numero)
                                                            case _:
                                                                print("")
                                                    case _:
                                                        handle_flow_1_subflow_1_2_1_x(numero, user_state.subFlow4)
                                        case 2: ## 1 1 2 2 0
                                            match user_state.subFlow4:
                                                case 0:
                                                    handle_flow_1_subflow_1_2_2(numero)
                                                case 1:
                                                    handle_flow_1_subflow_1_2_1_1_1_1_1(numero)
                                                    handle_flow_1_subflow_1_2_1_1(numero)
                                                case 2:
                                                    handle_flow_1_subflow_1_2_1_1_2(numero)
                                                    handle_flow_1_subflow_1_2_1_1(numero)
                                                case 3:
                                                    handle_flow_1_subflow_1_2_1_1_1_3(numero)
                                                    handle_flow_1_subflow_1_2_1_1(numero)

                                        case 3:
                                            handle_flow_1_subflow_1_2_3(numero, user_state)
                                            handle_flow_1_subflow_1_2_1_1(numero)
                                        case 4:
                                            handle_flow_1_subflow_1_2_4(numero, user_state)
                                            handle_flow_1_subflow_1_2_1_1(numero)
                                        case 5:
                                            handle_flow_1_subflow_1_2_1_1_2_2(numero)

                            # case 3:
                            #
                            #     match user_state.subFlow3:
                            #         case 0:
                            #             handle_flow_1_subflow_1_3(numero)  # 1 1 3 0 0 -  Menú Peticiones
                            #         case 1:
                            #             match user_state.subFlow4:
                            #                 case 0:
                            #                     handle_database_manteniment(numero)
                            #
                            #                 case _:
                            #                     handle_database_manteniment(numero)
                            #         case 2:
                            #             match user_state.subFlow4:
                            #                 case 0:
                            #                     handle_database_manteniment(numero)
                            #                 case _:
                            #                     handle_database_manteniment(numero)
                            #         case 3:
                            #             match user_state.subFlow4:
                            #                 case 0:
                            #                     handle_database_manteniment(numero)
                            #                 case _:
                            #                     handle_database_manteniment(numero)
                            #         case 4:
                            #             match user_state.subFlow4:
                            #                 case 0:
                            #                     handle_database_manteniment(numero, )
                            #                 case _:
                            #                     handle_database_manteniment(numero)
                            #         case 5:
                            #             match user_state.subFlow4:
                            #                 case 0:
                            #                     handle_database_manteniment(numero)
                            #                 case _:
                            #                     handle_database_manteniment(numero)
                            case 4:

                                match user_state.subFlow3:
                                    case 0:
                                        handle_flow_1_subflow_1_4(numero)  # 1 1 4 0 0 -  Menú Trámites
                                    case 1:
                                        match user_state.subFlow4: # 1 1 4 1 0
                                            case 0:

                                                handle_flow_1_subflow_1_4_1(numero, name)
                                                sleep(1)
                                                handle_flow_1_subflow_1_2_1_1(numero)

                                            case _:
                                                handle_database_manteniment(numero)
                                    case 2:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_4_2(numero, name)
                                                sleep(1)
                                                handle_flow_1_subflow_1_2_1_1(numero) ## Hasta aquì me quedé, falta agregar para enviar correo y demás.
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 3:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_contact_asesor(numero)
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 4:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_contact_asesor(numero )
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 5:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_contact_asesor(numero)
                                            case _:
                                                handle_database_manteniment(numero) # Lista botones para trámites
                            case 5:

                                match user_state.subFlow3:
                                    case 0:
                                        handle_flow_1_subflow_1_5(numero)  # 1 1 5 0 0 -  Menú Aplicaciones
                                    case 1:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_5(numero)

                                            case _:
                                                handle_database_manteniment(numero)
                                    case 2:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_5(numero)
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 3:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_5(numero)
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 4:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_5(numero, )
                                            case _:
                                                handle_database_manteniment(numero)
                                    case 5:
                                        match user_state.subFlow4:
                                            case 0:
                                                handle_flow_1_subflow_1_1_5(numero)
                                            case _:
                                                handle_database_manteniment(numero)  # Lista botones para trámites
                            case 6:
                                handle_contact_asesor(numero)

                case 404:
                    handle_flow_1_subflow_404(numero)
        case _:
            print("")
