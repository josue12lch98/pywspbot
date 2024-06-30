from dbQuery import update_user_state, generic_reply

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
    update_user_state(numero, subFlow = 1, subFlow2 = 0) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
      
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
