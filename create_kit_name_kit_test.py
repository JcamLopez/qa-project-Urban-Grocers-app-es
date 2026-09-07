import sender_stand_request
import data


def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    response_json = user_response.json()
    assert response_json["authToken"] != ""
    token_guardado = response_json["authToken"]
    return token_guardado


def positive_assert(name=None):
    token = get_new_user_token()
    if name is None:
        kit_response = sender_stand_request.post_new_kit(data.kit_body, token)
    else:
        current_body = data.kit_body.copy()
        current_body["name"] = name
        kit_response = sender_stand_request.post_new_kit(current_body, token)

    assert kit_response.status_code == 201
    return kit_response


def negative_assert(name):
    token = get_new_user_token()
    current_body = data.kit_body.copy()
    current_body["name"] = name
    kit_response = sender_stand_request.post_new_kit(current_body, token)
    assert kit_response.status_code == 400
    return kit_response


def test_create_kit():
    positive_assert()


def test_one_letter_in_name():
    response = positive_assert('a')
    assert response.json()["name"] == "a"


def test_five_hundred_letters_in_name():
    response = positive_assert(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')
    assert response.json()[
               "name"] == "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"


def test_letters_number_minor_zero_in_name():
    negative_assert('')


def test_five_hundred_twelve_letters_in_name():
    negative_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_special_characters_in_name():
    response = positive_assert('"№%@",')
    assert response.json()["name"] == '"№%@",'


def test_space_in_name():
   response = positive_assert(" A Aaa ")
   assert response.json()["name"] == " A Aaa "

def test_number_in_name():
    response = positive_assert("123")
    assert response.json()["name"] == "123"

def test_empy_parameters_in_name():
    negative_assert({})

def  test_type_different_in_name():
    negative_assert(123)