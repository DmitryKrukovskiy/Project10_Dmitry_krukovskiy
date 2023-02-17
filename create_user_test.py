import sender_stand_request
import data

def get_kit_body(Name):
    current_body = data.kit_body.copy()
    current_body["name"] = Name
    return current_body

def positive_assert(Name):
    kit_body = get_kit_body(Name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 201

    kits_table_response = sender_stand_request.get_kits_table()

    str_kit = kit_body["name"]

    assert kits_table_response.text.count(str_kit)

# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_create_kit_1_letter_in_Name_get_success_response():
    positive_assert("a")
