from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_2_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Beneficios G4S"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0) # Retirar 0 cuando tengamos la lógica completa de BENEFICIOS

def handle_flow_1_subflow_1_2_2(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "AFP"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 2, subFlow3 = 0) # Retirar 0 cuando tengamos la lógica completa de AFP

def handle_flow_1_subflow_1_2_3(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Capacitaciones"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 2, subFlow3 = 0) # Retirar 0 cuando tengamos la lógica completa de Capa

def handle_flow_1_subflow_1_2_4(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "Abono retención judicial"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow = 2, subFlow3 = 0) # Retirar 0 cuando tengamos la lógica completa de Abono




