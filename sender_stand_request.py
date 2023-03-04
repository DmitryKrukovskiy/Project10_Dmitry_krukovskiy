import requests
import configuration
import data


#  Функция отправляет POST-запрос на создание нового пользователя.
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)


#  Функция возвращает токен авторизации из POST-запроса на создание нового пользователя.
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json()['authToken']


#   Функция отправляет POST-запрос на создание нового набора и использует словарь с данными набора (kit_body)
#   и токен авторизации (auth_token).
def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = "Bearer " + auth_token
    url = configuration.URL_SERVICE + configuration.CREATE_KITS_PATH
    response = requests.post(url, json=kit_body, headers=headers_dict)
    return response
