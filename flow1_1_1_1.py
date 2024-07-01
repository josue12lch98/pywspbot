from dbQuery import update_user_state, generic_reply
import inspect

def handle_database_manteniment(numero, user_state):
    buttton = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "Estamos actualizando la base de datos, por favor, intenta más tarde. \n Selecciona asesor si quieres que te pongamos en contacto con uno"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "6 1 2 1 1",  # Flujo / Sub flow / Sub flow 2 / Sub flow 3
                            "title": "Asesor"
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
                            "title": "Menú Principal"
                        }
                    }
                ]
            }
        }
    }
    generic_reply(buttton)
def handle_contact_asesor (numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "En breve te pondremos en contacto con un asesor."
        }
    }
    generic_reply(data)

def handle_flow_1_subflow_1_2(numero):
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "Información sobre beneficios G4S y otros"
            },
            "footer": {
                "text": "Selecciona alguna de las opciones para poder ayudarte"
            },
            "action":{
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Section 1",
                        "rows": [
                            {
                                "id": "1 1 2 1 0",
                                "title": "Beneficios G4S"
                            },
                            {
                                "id": "1 1 2 2 0",
                                "title": "AFP"
                            },
                            {
                                "id": "1 1 2 3 0",
                                "title": "Capacitaciones"
                            },
                            {
                                "id": "1 1 2 4 0",
                                "title": "Abono retención judicial"
                            },
                            {
                                "id": "1 1 2 5 0",
                                "title": "Otras consultas"
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 1, subFlow2 = 2, func = str(inspect.currentframe().f_code.co_name))
    
def handle_flow_1_subflow_1_3(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Ingresar lista/botones para PETICIONES"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 1, subFlow2 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
    
def handle_flow_1_subflow_1_4(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Ingresar lista/botones para TRÁMITES"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 1, subFlow2 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros

def handle_flow_1_subflow_1_5(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Ingresar lista/botones para ACCESOS A APLICACIONES"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 1, subFlow2 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
