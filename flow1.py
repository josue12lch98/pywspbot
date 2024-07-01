from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_0(numero, name):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Antes de comenzar, coméntame " + name + "¿Estás teniendo problemas para iniciar tu marcación en Javelin?"
            },
            "footer": {
                "text": "Selecciona solo una de las opciones"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 404 0 0",
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 0 0",
                            "title": "No"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(func = str(inspect.currentframe().f_code.co_name))

def handle_flow_1_subflow_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Perfecto, estamos felices de que seas parte de la correcta gestión en Javelin, juntos estamos logrando la EXCELENCIA OPERACIONAL"
        }
    }
    generic_reply(data)
    
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Para poder registrar tu reclamo o consulta, necesito que me ayudes a escoger un tema."
        }
    }
    generic_reply(data)
    

    btns1 = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Selecciona alguna opción"
            },
            "action":{
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 1 0",
                            "title": "MIS PAGOS"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 2 0",
                            "title": "G4S"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 3 0",
                            "title": "PETICIONES"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(btns1)
    
    btns2 = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Selecciona alguna opción"
            },
            "action":{
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 4 0",
                            "title": "TRÁMITES"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 5 0",
                            "title": "ACCESO A APLICACIONES"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 6 0",
                            "title": "OTROS"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(btns2)
    update_user_state(func = str(inspect.currentframe().f_code.co_name))
    