import requests
import configuration
import data


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)


#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.text)
#print(response.json()['authToken'])

def get_new_user_token():
    response = post_new_user(data.user_body)
    auth_token = response.json()['authToken']
    return auth_token

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": "Bearer " + auth_token,
        "Content-Type": "application/json",
    }
    url = configuration.URL_SERVICE + configuration.CREATE_KITS_PATH
    response = requests.post(url, json=kit_body, headers=headers)
    return response


auth_token = get_new_user_token()


kit_response = post_new_client_kit(data.kit_body, auth_token)
print(kit_response.status_code)
print(kit_response.text)
