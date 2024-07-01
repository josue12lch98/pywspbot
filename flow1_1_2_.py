from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_2_1(numero, name, b):
    if b == "":
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body":  "Estimado " + name.capitalize() + ", te informamos que tenemos beneficios actualizados en la página de Bienestar Social G4S: #Link, en donde encontrarás información detallada sobre: \n* Convenios Corporativos \n* Seguros Corporativos \n       - ESSALUD \n       - SCTR \n       - Vida Ley \n* Beneficios Corporativos \n      - Préstamos \n      - Licencias \n* Programas Corporativos"
            }
        }
        generic_reply(data)
        
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "Asímismo, se detalla el paso a paso para la gestión de cada uno. \nRecuerda comunicarnos sobre tus gestiones personales para saber cómo ayudarte. ¡Estamos para ti!"
            }
        }
        generic_reply(data)
    else:
        print("")
    update_user_state(numero, subFlow2 = 2, subFlow3 = 1, subFlow4 = 1, subFlow5 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de BENEFICIOS

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
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de AFP

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
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de Capa

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
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de Abono

def handle_flow_1_subflow_1_2_x(numero, x):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Excepción no match para handle_flow_1_subflow_1_2_x en subFlow3:" + str(x)
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de Abono



