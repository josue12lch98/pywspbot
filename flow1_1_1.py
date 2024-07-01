from dbQuery import update_user_state, generic_reply
import inspect

def handle_flow_1_subflow_1_1_1(numero, user_state):
    list = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {
                "text":  "1️⃣Quiero saber la fecha de pago de gratificación \n\n " +
                "2️⃣Quiero saber la fecha de pago de vacaciones\n\n"

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
                                "id": "1 1 1 1 1",
                                "title": "Opción 1",
                                "description": "Quiero saber la fecha de pago de gratificación"
                            },
                            {
                                "id": "1 1 1 1 2",
                                "title": "Opción 2",
                                "description": "Quiero saber la fecha de pago de vacaciones"
                            }, {
                                "id": "1 1 1 1 0",
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
    update_user_state(numero, subFlow = 1, subFlow2 = 0, func = str(inspect.currentframe().f_code.co_name)) # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros


def handle_flow_1_subflow_1_1_2(numero, user_state):
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

def handle_flow_1_subflow_1_1_2(numero, user_state):
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


def handle_flow_1_subflow_1_1_2(numero, user_state):
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


def handle_flow_1_subflow_1_1_2(numero, user_state):
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
def handle_flow_1_subflow_1_1_2(numero, user_state):
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


