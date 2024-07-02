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
                "body":  "Estimado " + name.capitalize() + ", te informamos que tenemos beneficios actualizados en la página de Bienestar Social G4S:  https://sites.google.com/view/g4s-peru-bienestar-social/inicio, en donde encontrarás información detallada sobre: \n* Convenios Corporativos \n* Seguros Corporativos \n       - ESSALUD \n       - SCTR \n       - Vida Ley \n* Beneficios Corporativos \n      - Préstamos \n      - Licencias \n* Programas Corporativos"
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
    lista = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "🔧 TP Services " + "\n Por favor, selecciona el trámite relacionado con AFP que deseas realizar:\n" +
    "1️⃣ Tipo de AFP\n" +
    "2️⃣ Solicitud de traslado AFP-AFP\n" +
    "3️⃣ Afiliación de ONP a AFP\n"
    },
    "footer": {
        "text": "Selecciona alguna de las opciones para poder ayudarte"
    },
    "action": {
        "button": "Ver Opciones",
        "sections": [
            {
                "title": "Section 1",
                "rows": [
                    {
                        "id": "1 1 2 2 1 1 0",
                        "title": "Opción 1",
                        "description": "Tipo de AFP"
                    },
                    {
                        "id": "1 1 2 2 2 2 0",
                        "title": "Opción 2",
                        "description": "Solicitud de traslado AFP-AFP"
                    },
                    {
                        "id": "1 1 2 2 3 3 0",
                        "title": "Opción 3",
                        "description": "Afiliación de ONP a AFP"
                    }, {
                        "id": "1 1 2 2 0 0 0",
                        "title": "Menú principal",
                        "description": ""
                    }
                ]
            }
        ]
    }
    }
    }
    generic_reply(lista)
    update_user_state(numero, subFlow=1, subFlow2=2, func=str(inspect.currentframe().f_code.co_name))
    update_user_state(numero, subFlow2 = 2, subFlow3 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de AFP

def handle_flow_1_subflow_1_2_3(numero, user_state):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body":  "🌟 Estimado(a) "+user_state.name + " si desea obtener información sobre sus capacitaciones, le brindamos el siguiente link al instructivo en donde podrá conocer:\n" +
"📚 ¿Cuáles son las Capacitaciones a tomar por Política de la empresa?\n" +
"📋 ¿Cuáles son las Capacitaciones Opcionales?\n" +
"🔍 ¿Cómo accedo a mis Capacitaciones?\n\n" +
"A continuación se le brinda el link al instructivo en donde podrá conocer el paso a paso de cómo visualizar la información de sus capacitaciones mediante INTRANET.\n\n" +
"🔗 Link al Instructivo:\n\n"
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



