import platform
import datetime
import socket
import requests

def send_to_telegram(message):

    apiToken = ''
    chatID = ''
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    now = datetime.datetime.now().strftime("%H:%M:%S")
    time = datetime.datetime.now().strftime("%d/%m/%Y")
    ip_equipo = socket.gethostbyname(socket.gethostname())
    ip_privada = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_privada = s.getsockname()[0]
    s.close()
    info_equipo = 'MI PC \n - Equipo: '+ platform.node() + '\n - IP: ' + ip_privada + '\n - Hora: ' + str(now) + '\n - Fecha: ' + str(time)  + '\n'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': info_equipo + message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram(" - ¡¡Localizador activado!!")