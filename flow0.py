import re

from dbQuery import update_user_state, generic_reply
import inspect #inspect.currentframe().f_code.co_name

def handle_flow_0_subflow_0(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Hola! 😃 Te saluda *Robotín*, asistente virtual G4S que ha sido creado para absolver las dudas generales de todos los colaboradores G4S Perú."
        }
    }
      # Asume que existe una función para enviar mensajes
    generic_reply(data)
    add = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Para ayudarte de la mejor manera, por favor detállame tu número de DNI (Ejemplo: 758152334)"
        }
    }
    generic_reply(add)
    
    update_user_state(numero, subFlow=1, func = str(inspect.currentframe().f_code.co_name))

def handle_flow_0_subflow_1(numero, texto):
    patron = r'^\d{8}$'  # Expresión regular para validar un DNI
    if re.fullmatch(patron, texto):
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "Así mismo, bríndame tu nombre completo (Ejemplo: Juan Luis Perez Gonzales)"
            }
        }
        generic_reply(data)
        update_user_state(numero, subFlow=2, dni=texto)
    else:
        msgerror = "Disculpa tú número de dni no parece válido. \nIngresaste: " + texto + "\nIngresa sólo el número de tu DNI sin letras o espacios."
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": msgerror
            }
        }
        generic_reply(data)
        update_user_state(numero, subFlow=1, func = str(inspect.currentframe().f_code.co_name)) # considerar retirar el subflow 1 puesto que igual va a regresar a 1
                

def handle_flow_0_subflow_2(numero, texto):
    full_name = texto
    name = texto.split()[0]
    msg = name.capitalize() + ", un gusto de conocerte por este medio (...). \nFinalmente, detállame a qué sucursal perteneces (Ejemplos: Lima Sur, Arequipa, Chiclayo)"
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": msg
        }
    }

    generic_reply(data)
    subFlow = 3
    update_user_state(number=numero, subFlow=subFlow, name=name, full_name=full_name, func = str(inspect.currentframe().f_code.co_name))
        
## poner este mensaje Listo, ${myState.nombre}.\n Gracias por confirmar tu DNI: ${myState.dni}, sucursal a la que perteneces: ${myState.sucursal}. `+ `Para continuar, necesito que me confirmes que tus datos son los correctos.`) cargando todos los datos ingresados
def handle_flow_0_subflow_3(numero, texto, name, dni):
    sucursal = texto
    name = name.split()[0]
    
    msg = "¡Listo " + name.capitalize() + " Gracias por confirmar tu DNI: " + dni + ", sucursal a la que perteneces: " + sucursal + " \nPara continuar, necesito que me confirmes que tus datos son los correctos."
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": msg
        }
    }
    generic_reply(data)

    buttton = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Para continuar, necesito que me confirmes que tus datos son los correctos."
                },
                "footer": {
                    "text": "Selecciona una de las opciones"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "1 0 0 0 0",
                                "title": "Si"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "0 2 0 0",
                                "title": "No"
                            }
                        }
                    ]
                }
            }
        }
    generic_reply(buttton)
    
    subFlow = 4
    update_user_state(number=numero, subFlow=subFlow, sucursal=texto, func = str(inspect.currentframe().f_code.co_name))

