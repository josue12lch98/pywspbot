from dbQuery import update_user_state, generic_reply

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
                            "id": "1 404 0",
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1 0",
                            "title": "No"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(data)


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
    """
    """
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "Selecciona alguna opción"
            },
            "footer": {
                "text": "Selecciona alguna de las opciones para poder ayudarte"
            },
            "action":{
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "========================================================",
                        "rows": [
                            {
                                "id": "1 1 1", # FLOW / SUBFLOW / SUBFLOW2
                                "title": "MIS PAGOS"
                            }
                        ]
                    },
                    {
                        "title": "========================================================",
                        "rows": [
                            {
                                "id": "1 1 2",
                                "title": "INFORMACIÓN SOBRE BENEFICIOS G4S Y OTROS"
                            }
                        ]
                    },
                    {
                        "title": "========================================================",
                        "rows": [
                            {
                                "id": "1 1 3",
                                "title": "PETICIONES"
                            }
                        ]
                    },
                    {
                        "title": "========================================================",
                        "rows": [
                            {
                                "id": "1 1 4",
                                "title": "TRÁMITES"
                            }
                        ]
                    },
                    {
                        "title": "========================================================",
                        "rows": [
                            {
                                "id": "1 1 5",
                                "title": "ACCESO A APLICACIONES"
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(numero)