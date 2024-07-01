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
                            "id": "1 1 2 1 1", # Flujo / Sub flow / Sub flow 2 / Sub flow 3
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 2",
                            "title": "No"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 1 3",
                            "title": "Hacer otra pregunta"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(buttton)