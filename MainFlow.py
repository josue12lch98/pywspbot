from dbQuery import get_user_state, update_user_state
from flow1 import handle_flow_0_subflow_0, handle_flow_0_subflow_1, handle_flow_0_subflow_2, handle_flow_0_subflow_3


# Ciclo entrada
def send_txt(texto, numero):
    texto = texto.lower()
    user_state = get_user_state(numero)
    if user_state is None:
        update_user_state(numero, flow=0,subFlow=0)
        user_state = get_user_state(numero)

    match user_state.flow:
        case 0:
            match user_state.subFlow:
                case 0:
                    handle_flow_0_subflow_0(numero)


                case 1:
                    handle_flow_0_subflow_1(numero, texto)
                case 2:  # Consultar si se puede hacer lista
                    handle_flow_0_subflow_2(numero, texto)

                case 3:
                    handle_flow_0_subflow_3(numero, texto)
        case 4:

        case 5:
            if "btnsi" in texto:
                data = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": numero,
                    "text": {
                        "preview_url": False,
                        "body": "Nice"
                    }
                }
            else:
                data = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": numero,
                    "text": {
                        "preview_url": False,
                        "body": "Indicame tus datos nuevamente"
                    }
                }
                flow = 0


def ordenar_por_fecha_y_hora(registros):
    registros_ordenados = sorted(registros, key=lambda x: x.fecha, reverse=True)
    return registros_ordenados
def generic_reply(data):
    data = json.dumps(data)  # Convertir el diccionario en formato JSON

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EAAV8kZCQDeLkBOwQu1NSf9nGRs5AxW1ZBT9NyjzA1aHTC0ZAZColXU5Resu79lwawwLHn0VlHT7BkIIIEz2USl4pHLjOATxu803wFWPpKs6kyoaDEzZCYBwJjkuXjw2V0o5XZCVbirxI3xcKXcCaQZBi92aQpkafFFGI3oTGuHXwugmf44ZAUXMS1aoezS9i9Lg3LxW1OA72uZACxUZCFzdaoZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v20.0/357679540758058/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(json.dumps(e))
    finally:
        connection.close()

def generic_reply(data):
    data = json.dumps(data)  # Convertir el diccionario en formato JSON

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EAAV8kZCQDeLkBO7zt2MHThLR9X9V7OK75TnsYprLwLos8sbv1sreKraudfBRwVHZBZBpt9PESJ4m974NH6fZBew8p0RAZBNxEBjSEONYjjWZBmNIQIms38XHIFlK4r7ChWOasPq4W0uZCJEXJ4X0CajyGbzC08z8kz2UZAZApdHIcNpiiEGwZCHZBUBVt3F9qaWHhXhEK3gPduiudoWDmYKAYgZD"
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")

    try:
        connection.request("POST", "/v20.0/357679540758058/messages", data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        agregar_mensajes_log(json.dumps(e))
    finally:
        connection.close()

mensajes_log = []
