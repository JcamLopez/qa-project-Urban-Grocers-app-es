import sender_stand_request
import data

def get_new_user_token ():
    user_response= sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201
    response_json = user_response.json()
    assert response_json["authToken"] != ""
    token_guardado = response_json["authToken"]
    return token_guardado

def test_positive_create_kit():
    token = get_new_user_token()
    kit_response= sender_stand_request.post_new_kit(data.kit_body,token)
    assert kit_response.status_code == 201
    response = kit_response.json()
    print(response)

