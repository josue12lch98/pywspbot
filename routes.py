from flask import  request, jsonify, render_template


from dbQuery import UserState, get_user_state, update_user_state
from flow1 import handle_flow_0_subflow_0, handle_flow_0_subflow_1, handle_flow_0_subflow_2, handle_flow_0_subflow_3


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
        if challenge and token == 'token':
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
