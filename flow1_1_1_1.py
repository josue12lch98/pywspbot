from dbQuery import update_user_state, generic_reply
import inspect

def handle_database_manteniment(numero):
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
                            "id": "1 1 0 0 0",
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
