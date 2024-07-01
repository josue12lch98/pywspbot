from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_1(numero):
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
                                "id": "1 1 1 1 0",
                                "title": "Cronograma de Pagos",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 0",
                                "title": "¿Cuanto me van Pagar?",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 3 0",
                                "title": "Consulta descuentos",

                                "description": ""
                            },
                            {
                                "id": "1 1 1 4 0",
                                "title": "Detalles de pago",
                                "description": ""
                            },

                            {
                                "id": "1 1 1 5 0",
                                "title": "Otras consulta",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 0 0",
                                "title": "Menú principal",
                                "description": ""
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
                                "id": "1 1 2 1 0 0",
                                "title": "Beneficios G4S"
                            },
                            {
                                "id": "1 1 2 2 0 0",
                                "title": "AFP"
                            },
                            {
                                "id": "1 1 2 3 0 0",
                                "title": "Capacitaciones"
                            },
                            {
                                "id": "1 1 2 4 0 0",
                                "title": "Abono retención judicial"
                            },
                            {
                                "id": "1 1 2 5 0 0",
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
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "🔧 TP Services" + "\n Por favor, selecciona la opción de tu interés:\n" +
    "1️⃣ Vacaciones: Realiza tu solicitud de vacaciones, conoce cuántos días de vacaciones te quedan disponibles y el estado de tu papeleta.\n" +
    "2️⃣ Descanso Médico: Conoce el paso a paso de cómo registrar tu Descanso Médico.\n" +
    "3️⃣ Asignación Familiar: Realiza tu solicitud de Asignación Familiar.\n" +
    "4️⃣ Certificado o Constancia de Trabajo: Solicita tu Certificado o Constancia de Trabajo.\n" +
    "5️⃣ Status de Baja de Carnet Sucamec: Conoce el status de baja de tu Carnet Sucamec.\n"

            },
            "footer": {
                "text": "👇 Selecciona una opción para más detalles:"
            },
            "action": {
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Section 1",
                        "rows": [
                            {
                                "id": "1 1 3 1 0 0",
                                "title": "Opción 1",
                                "description": "Solicitud de vacaciones"
                            },
                            {
                                "id": "1 1 3 2 0 0",
                                "title": "Opción 2",
                                "description": "Solicitud de Registro de DESCANSO MÉDICO"
                            },
                            {
                                "id": "1 1 3 3 0 0",
                                "title": "Opción 3",
                                "description": "Solicitud de ASIGNACIÓN FAMILIAR"
                            },
                            {
                                "id": "1 1 3 4 0 0",
                                "title": "Opción 4",
                                "description": "Cambio de CUENTAS BANCARIAS"
                            },
                            {
                                "id": "1 1 3 5 0 0",
                                "title": "Opción 5",
                                "description": "Certificado o Constancia de Trabajo"
                            },
                            {
                                "id": "1 1 3 6 0 0",
                                "title": "Opción 6",
                                "description": "Status de Baja de Carnet Sucamec"
                            }, {
                                "id": "1 1 0 0 0 0",
                                "title": "Menú principal",
                                "description": ""
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow=1, subFlow2=2, func=str(inspect.currentframe().f_code.co_name))
def handle_flow_1_subflow_1_4(numero):
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text":  "🔧 TP Services" + "\n En esta sección, conoce los diversos trámites que puedes realizar:\n" +
    "1️⃣ Queja con Respeto a Operaciones\n" +
    "2️⃣ Trámite de Cambio de Unidad\n" +
    "3️⃣ Trámite de Cambio de Uniforme\n" +
    "4️⃣ Renuncia\n" +
    "5️⃣ Denuncias\n"

            },
            "footer": {
                "text": "👇 Selecciona una opción para más detalles:"
            },
            "action": {
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Opciones de Trámites",
                        "rows": [
                            {
                                "id": "1 1 4 1 0 0",
                                "title": "Opción 1",
                                "description": "Queja con respecto a Operaciones."
                            },
                            {
                                "id": "1 1 4 2 0 0",
                                "title": "Opción 2",
                                "description": "Cambio de Unidad"
                            },
                            {
                                "id": "1 1 4 3 0 0",
                                "title": "Opción 3",
                                "description": "Cambio de Uniforme"
                            },
                            {
                                "id": "1 1 4 4 0 0",
                                "title": "Opción 4",
                                "description": "Renuncia"
                            },
                            {
                                "id": "1 1 4 5 0 0",
                                "title": "Opción 5",
                                "description": "Denuncias"
                            }, {
                                "id": "1 1 1 0 0 0",
                                "title": "Menú principal",
                                "description": ""
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow=1, subFlow2=2, func=str(inspect.currentframe().f_code.co_name))
def handle_flow_1_subflow_1_5(numero):
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "👇 Selecciona una opción para más detalles:"

            },
            "footer": {
                "text": ""
            },
            "action": {
                "button": "Ver Opciones",
                "sections": [
                    {
                        "title": "Opciones de Trámites",
                        "rows": [
                            {
                                "id": "1 1 5 1 0 0",
                                "title": "Opción 1",
                                "description": "JAVELIN"
                            },
                            {
                                "id": "1 1 5 2 0 0",
                                "title": "Opción 2",
                                "description": "INTRANET"
                            },
                            {
                                "id": "1 1 5 3 0 0",
                                "title": "Opción 3",
                                "description": "MyLearning (Cursos Virtuales)"
                            },
                            {
                                "id": "1 1 1 0 0 0",
                                "title": "Opción 4",
                                "description": "Menú principal"
                            },

                        ]
                    }
                ]
            }
        }
    }
    generic_reply(data)
    update_user_state(numero, subFlow=1, subFlow2=2, func=str(inspect.currentframe().f_code.co_name))