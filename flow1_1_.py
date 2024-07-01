from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_1(numero, user_state):
    list = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "1️⃣Cronograma de pagos \n\n " +
                "2️⃣¿Cuánto me van a pagar?\n\n" +
                "3️⃣Consulta sobre los descuentos de mi pago\n\n" +
                "4️⃣Detalles de mi pago\n\n" +" Otras consultas\n\n"
            },
            "footer": {
                "text": "Elige un tema para tu reclamo o consulta."
            },
            "action": {
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Section 1",
                        "rows": [
                            {
                                "id": "1 1 1 0 0",
                                "title": "Cronograma de Pagos",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 1 0",
                                "title": "¿Cuanto me van Pagar?",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 1 0",
                                "title": "Consulta descuentos",

                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 0",
                                "title": "Detalles de pago",
                                "description": ""
                            },

                            {
                                "id": "1 1 1 3 0",
                                "title": "Otras consulta",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 0 0",
                                "title": "Menú principal",
                                "description": " "
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(list)
    update_user_state(numero, subFlow = 1, subFlow2 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
    
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
