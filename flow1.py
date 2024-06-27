# flow_handlers.py
from app import update_user_state, send_txt  # Importa las funciones necesarias

def handle_flow_0_subflow_0(numero):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Hola! 😃 Te saluda Robotín, asistente virtual G4S que ha sido creado para absolver las dudas generales de todos los colaboradores G4S Perú \n Para ayudarte de la mejor manera, por favor detállame tu número de DNI (Ejemplo: 758152334)"
        }
    }
    send_txt(data)  # Asume que existe una función para enviar mensajes
    update_user_state(numero, subFlow=1)

def handle_flow_0_subflow_1(numero, texto):
    try:
        int(texto)  # Intenta convertir el texto a int, suponiendo que es el DNI
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": "Así mismo, bríndame tu nombre completo (Ejemplo: Juan Luis Perez Gonzales)"
            }
        }
        send_txt(data)
        update_user_state(numero, subFlow=2, dni=texto)
    except ValueError:  # Captura una excepción más específica
        msgerror = "Disculpa tú número de dni no parece válido. Ingresaste: " + texto + " Ingresa sólo el número de tu DNI"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "text": {
                "preview_url": False,
                "body": msgerror
            }
        }
        send_txt(data)
