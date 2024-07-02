from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_1_5(numero):
    list = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text":  "👇 Selecciona una opción para más detalles:"

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
                                "id": "1 1 5 1 1 1",
                                "title": "Opción 1",
                                "description": "¿Cómo registro asistencia?"
                            },
                            {
                                "id": "1 1 5 1 1 2",
                                "title": "Opción 2",
                                "description": "¿Cómo accedo/marco?"
                            },  {
                                "id": "1 1 5 1 1 3",
                                "title": "Opción 3",
                                "description": "Actualización de datos"
                            }, {
                                "id": "1 1 5 1 1 4",
                                "title": "Opción 4",
                                "description": "Cambio de contraseña"
                            },{
                                "id": "1 1 5 0 0 0",
                                "title": "Menú Aplicaciones",
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


def handle_flow_1_subflow_1_1_2(numero, ):
    list = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": " 1️⃣ Cálculo de CTS \n\n " +
                "2️⃣ Cálculo de GRATIFICACIÓN\n\n" +
                "3️⃣ Cálculo de LIQUIDACIÓN\n\n" +
                "4️⃣ Cálculo de VACACIONES\n\n" +
                "5️⃣ Cálculo de HORAS EXTRAS\n\n" +
                "6️⃣ NO ME PAGARON\n\n"

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
                                "id": "1 1 1 2 1",
                                "title": "Cálculo de CTS",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 2",
                                "title": "Cálculo de GRATIFICACIÓN",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 3",
                                "title": "Cálculo de LIQUIDACIÓN",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 4",
                                "title": "Cálculo de VACACIONES",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 5",
                                "title": "Cálculo de HORAS EXTRAS",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 2 6",
                                "title": "NO ME PAGARON",
                                "description": ""
                            }, {
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
    update_user_state(numero, subFlow=1, subFlow2=0, func=str(
        inspect.currentframe().f_code.co_name))  # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros

def handle_flow_1_subflow_1_1_3(numero, ):
    list = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text":  "🔧 TP Services" + "\nPor favor, selecciona la opción de tu interés:\n" +
    "1️⃣ ¿Cuánto es el porcentaje de descuento AFP?\n" +
    "2️⃣ Retención Judicial\n" +
    "3️⃣ Descuento por Devolución de Horas Acumuladas en Pandemia\n"


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
                                "id": "1 1 1 3 1",
                                "title": "Opción 1",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 3 2",
                                "title": "Opción 2",
                                "description": ""
                            },
                            {
                                "id": "1 1 1 3 3",
                                "title": "Opción 3",
                                "description": ""
                            }, {
                                "id": "1 1 1 0 0",
                                "title": "Menú Pagos",
                                "description": ""
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(list)
    update_user_state(numero, subFlow=1, subFlow2=0, func=str(
        inspect.currentframe().f_code.co_name))  # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros


def handle_flow_1_subflow_1_1_4(numero, ):
    list = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text": "🔧 TP Services" + "\n Por favor, selecciona la opción de tu interés:\n" +
    "1️⃣ Quiero ver mi BOLETA (Cesada o Activa)\n" +
    "2️⃣ Quiero saber el concepto de mis BOLETAS\n" +
    "3️⃣ Consulta de TAREAJE del mes\n"

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
                                "id": "1 1 1 4 1",
                                "title": "Opción 1",
                                "description": "Quiero ver mi BOLETA (Cesada o Activa)"
                            },
                            {
                                "id": "1 1 1 4 2",
                                "title": "Opción 2",
                                "description": "Quiero saber el concepto de mis BOLETAS"
                            },
                            {
                                "id": "1 1 1 4 3",
                                "title": "Opción 3",
                                "description": "Consulta de TAREAJE del mes"
                            }, {
                                "id":"1 1 1 0 0",
                                "title": "Menú Pagos",
                                "description": ""
                            }
                        ]
                    }
                ]
            }
        }
    }
    generic_reply(list)
    update_user_state(numero, subFlow=1, subFlow2=0, func=str(
        inspect.currentframe().f_code.co_name))  # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
