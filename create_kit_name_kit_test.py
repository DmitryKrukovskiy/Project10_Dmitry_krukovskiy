import sender_stand_request
import data


def get_kit_body(nname):
    current_body = data.kit_body.copy()
    current_body["name"] = nname
    return current_body


def positive_assert(nname):
    kit_body = get_kit_body(nname)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201
    kits_table_response = sender_stand_request.get_new_client_kit(kit_body)
    str_user = data.kit_body["name"]


# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")
