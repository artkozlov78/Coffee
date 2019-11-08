
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import xmltodict


access_data = {
    "ip_address": "10.10.143.100",
    "login": "admin",
    "password": ""
}

get_value(access_data)

def get_value(access_data):

    # URL
    http_url = "http://" + access_data["ip_address"] + "/putxml"

    # HTTP Headers
    http_headers = {'Content-Type': 'text/xml'}

    http_params = {"location": "/Status/UserInterface/Extensions"}

    # disable warning about untrusted certs
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Create the Requests Connection
    try:
        get = requests.get(http_url, params=http_params, headers=http_headers, verify=False, auth=(access_data["login"], access_data["password"]))
    except requests.exceptions.ConnectionError:
        console_output = "Ошибка соединения с сервером " + access_data["ip_address"]
        print(console_output)
    except:
        console_output = "Что-то пошло не так при подключении пользователя " + access_data["login"] + " к серверу " + access_data["ip_address"]
        print(console_output)

    # Check is answer is successful
    if get.status_code == 401:
        console_output = "Пользователь " + access_data["login"] + " не авторизован для подключения к серверу " + access_data["ip_address"]
        print(console_output)

    if get.status_code != 200:
        console_output = "Ошибка при подключении к серверу: " + str(get.status_code) + ": " + get.reason
        print(console_output)

    # Convert output to Dict
    console_output = "Данные получены от " + access_data["ip_address"]
    print(console_output)

    xml_dict = xmltodict.parse(get.text)
    print(xml_dict)

