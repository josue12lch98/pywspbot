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
                            "id": "1 1 2 1 1 1", # Flujo / Sub flow / Sub flow 2 / Sub flow 3
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 1 2",
                            "title": "No"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 1 3",
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
            "body": "Excepción no match para _handle_flow_1_subflow_1_2_1_x_ en subFlow4:" + str(x)
        }
    }
    generic_reply(data)




def handle_flow_1_subflow_1_2_1_1_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "A partir de la experiencia que acabas de tener ¿En qué medida te encuentras satisfecho(a) con la *atención* brindada? \n1) Malo \n2) Regular\n3) Bueno \n4) Muy bueno \n5) Excelente "
        }
    }
    generic_reply(data)