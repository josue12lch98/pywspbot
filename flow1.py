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
                            "id": "1 404 0 0 0",
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 0 0 0",
                            "title": "No"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(number=numero, func = str(inspect.currentframe().f_code.co_name))

def handle_flow_1_subflow_1(numero):
    list = {
        "messaging_product" : "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "Perfecto, estamos felices de que seas parte de la correcta gestión en Javelin, juntos estamos logrando la EXCELENCIA OPERACIONAL"
            },
            "footer": {
                "text": "Elige un tema para tu reclamo o consulta."
            },
            "action":{
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Section 1",
                        "rows": [
                            {
                                "id": "1 1 1 0 0",
                                "title": "Mis pagos"
                            },
                            {
                                "id": "1 1 2 0 0",
                                "title": "Información G4S y otros"
                            },
                            {
                                "id": "1 1 3 0 0",
                                "title": "Peticiones"
                            },
                            {
                                "id": "1 1 4 0 0",
                                "title": "Trámites"
                            },
                            {
                                "id": "1 1 5 0 0",
                                "title": "Acceso a aplicaciones"
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(list)
    
    update_user_state(number=numero, func = str(inspect.currentframe().f_code.co_name))

def handle_flow_1_subflow_404(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Saliendo del consulta Marcación Javelin \nExit"
        }
    }
    generic_reply(data)
