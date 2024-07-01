from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Ingresar lista/botones para MIS PAGOS"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 1, subFlow2 = 0) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
    
def handle_flow_1_subflow_1_2(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Ingresar lista/botones para INFORMACIÓN G4S"
        }
    }
    generic_reply(data)
    
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "Información sobre beneficios, G4S y otros"
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
                                "id": "1 1 2 1",
                                "title": "Beneficios G4S"
                            },
                            {
                                "id": "1 1 2 2",
                                "title": "AFP"
                            }
                        ]
                    },
                    {
                        "title": "Section 2",
                        "rows": [
                            {
                                "id": "1 1 2 3",
                                "title": "Capacitaciones"
                            },
                            {
                                "id": "1 1 2 4",
                                "title": "Abono Retención Judicial"
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(number=numero)
    
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
    update_user_state(numero, subFlow = 1, subFlow2 = 0) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
    
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
    update_user_state(numero, subFlow = 1, subFlow2 = 0) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros

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
    update_user_state(numero, subFlow = 1, subFlow2 = 0) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros

def handle_flow_1_subflow_1_6(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Este era extra"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 1, subFlow2 = 0) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
