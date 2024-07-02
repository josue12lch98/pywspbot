from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_2_1_1(numero):
    buttton = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "¿Estás satisfecho con la respuesta? 👍"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 1 1 0", # Flujo / Sub flow / Sub flow 2 / Sub flow 3
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 1 2 0",
                            "title": "No"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 1 3 0",
                            "title": "Hacer otra pregunta"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(buttton)
    update_user_state(numero, func = str(inspect.currentframe().f_code.co_name))
    
    
def handle_flow_1_subflow_1_2_1_x(numero, x):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": ":" + str(x)
        }
    }
    generic_reply(data)




def handle_flow_1_subflow_1_2_1_1_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "A partir de la experiencia que acabas de tener ¿En qué medida te encuentras satisfecho(a) con la *atención* brindada?"
            },
            "action":{
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Section 1",
                        "rows": [
                            {
                                "id": "1 1 2 1 1 1 1",
                                "title": "Malo"
                            },
                            {
                                "id": "1 1 2 1 1 1 2",
                                "title": "Regular"
                            },
                            {
                                "id": "1 1 2 1 1 1 3",
                                "title": "Bueno"
                            },
                            {
                                "id": "1 1 2 1 1 1 4",
                                "title": "Muy bueno"
                            },
                            {
                                "id": "1 1 2 1 1 1 5",
                                "title": "Excelente"
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    

def handle_flow_1_subflow_1_2_1_1_1_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Gracias por tu calificación 🙂, no dudes en escribirnos si tienes otra consulta. 👋 \n\n📍Recuerda que nuestro canal de atención está habilitado de Lunea a Viernes de 8:00 am a 5:00 pm"
        }
    }
    generic_reply(data)

def handle_flow_1_subflow_1_2_1_1_1_2(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Para que uno de nuestros asesores pueda atenderte, por favor, indícame el detalle de tu consulta 🔎"
        }
    }
    generic_reply(data)

def handle_flow_1_subflow_1_2_1_1_1_3(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Salida a Flujo A"
        }
    }
    generic_reply(data)