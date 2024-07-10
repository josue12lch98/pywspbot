from dbQuery import update_user_state, generic_reply
import inspect


def handle_flow_1_subflow_1_4_1(numero, name):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Estimado(a) " + name + ", para tramitar tu *Inconveniente con respecto a operaciones* por favor detállanos tu caso al correo de Atención al Colaborador: atencion.colaborador@pe.g4s.com con la siguiente información 📝:\n\n" +
                    "1. Nombre y Apellidos\n" +
                    "2. Número de DNI\n" +
                    "3. Unidad\n" +
                    "4. Nombre y Apellido de la persona con la que se tiene el inconveniente.\n" +
                    "5. Detalle del Caso\n" +
                    "6. Número de Contacto\n\n" +
                    "Posteriormente, se elevará el reclamo y en base a las verificaciones sobre el caso, se realizarán las medidas correctivas. ✅"
        }
    }

    generic_reply(data)
    update_user_state(numero, subFlow=1, subFlow2=0, func=str(
        inspect.currentframe().f_code.co_name))  # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros


def handle_flow_1_subflow_1_4_2(numero, name):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": numero,
        "text": {
            "preview_url": False,
            "body": "Estimado(a)" + name + ", para tramitar tu Cambio de Unidad por favor detállanos tu caso al "
                                           "correo de Atención al Colaborador: atencion.colaborador@pe.g4s.com con la"
                                           " siguiente información 📝:\n\n" +
                    "1. Nombre y Apellidos\n" +
                    "2. Número de DNI\n" +
                    "3. Unidad\n" +
                    "4. Motivo\n" +
                    "5. Localidad a la que desea migrar\n" +
                    "6. Número de Contacto\n\n" +
                    "Antes de generar su solicitud, consulte a su supervisor si hay puestos disponibles en la unidad "
                    "a la que desea trasladarse y si corresponde su cambio. Así mismo, le informamos que su "
                    "supervisor ya tendrá conocimiento de su caso."

        }
    }

    generic_reply(data)
    update_user_state(numero, subFlow=1, subFlow2=0, func=str(
        inspect.currentframe().f_code.co_name))  # Retirar 0 cuando tengamos la lógica completa de 2. Imfo G4S y otros
