from dbQuery import update_user_state, generic_reply
import inspect


def handle_flow_1_subflow_1_2_1_1(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Estimado colaborador G4S, para saber a qué AFP estás afiliado ingresa en el siguiente Link y completa la información solicitada: https://servicios.sbs.gob.pe/ReporteSituacionPrevisional/Afili_Consulta.aspx\n\n"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de Capa
def handle_flow_1_subflow_1_2_1_2(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Estimado colaborador G4S, si desea hacer una solicitud de traslado de una AFP a otra, debe realizar los siguientes pasos:\n" +
      "1. Elegir el Tipo de AFP al que desea cambiarse.\n" +
      "2. Dirigirse a Oficinas para realizar la solicitud de cambio.\n" +
      "3. AFP notificará a G4S sobre el cambio.\n\n"
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de Capa

def handle_flow_1_subflow_1_2_1_3(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":"Estimado colaborador G4S, si desea hacer una solicitud de traslado de ONP a AFP, debe realizar la solicitud a la AFP donde quiere migrar para que realice el proceso."
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de Capa

def handle_flow_1_subflow_1_2_4(numero, user_state):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "🔸 **Abono de RETENCIÓN JUDICIAL**\n\n" +
            "🌟 Estimado(a) " + user_state.name + " el abono de Retención Judicial se realiza en el plazo de 5 días hábiles, posteriores al descuento realizado en el pago de fin de mes.\n"

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



