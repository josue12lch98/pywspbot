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
                            "id": "1 404",
                            "title": "Si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1 1",
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
def handle_flow_1_subflow_11(numero): # Lista en flow 1 - 1 para ingresar A
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
                        "title": "1. MIS PAGOS",
                        "rows": [
                            {
                                "id": "idcron",
                                "title": "Cronograma de Pagos",
                                "description": "Compra los mejores artículos de tecnología"
                            },
                            {
                                "id": "idpag",
                                "title": "¿Cuánto me van a pagar?",
                                "description": "Vende lo que ya no estés usando"
                            },
                            {
                                "id": "idcon",
                                "title": "Consulta sobre los descuentos de mi pago",
                                "description": "Vende lo que ya no estés usando"
                            },
                            {
                                "id": "idpago",
                                "title": "Detalles de pago",
                                "description": "Vende lo que ya no estés usando"
                            },
                            {
                                "id": "idothers",
                                "title": "Otras consultas",
                                "description": "Vende lo que ya no estés usando"
                            }
                        ]
                    },
                    {
                        "title": "Distribución y Entrega",
                        "rows": [
                            {
                                "id": "btndireccion",
                                "title": "Local",
                                "description": "Puedes visistar nuestro local."
                            },
                            {
                                "id": "btnentrega",
                                "title": "Entrega",
                                "description": "La entrega se realiza todo los dias."
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow=2) # considerar retirar el subflow 1 puesto que igual va a regresar a 1