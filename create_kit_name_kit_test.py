import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code ==400


#PRUEBAS DE ACUERDO A LA LISTA DE COMPROBACIÓN

#PRUEBA 1: EL NÚMERO PERMITIDO DE CARÁCTERES (1)
def test1_create_kit_1_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)


#PRUEBA 2: EL NÚMERO PERMITIDO DE CARÁCTERES (511)
def test2_create_kit_511_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)


#PRUEBA 3: EL NÚMERO DE CARÁCTERES ES MENOR QUE LA CANTIDAD PERMITIDA (0)
def test3_create_kit_without_name():
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_code_400(current_kit_body)


#PRUEBA 4: EL NÚMERO DE CARÁCTERES ES MAYOR QUE LA CANTIDAD PERMITIDA (512)
def test4_create_kit_512_letter_in_the_name():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_code_400(current_kit_body)


#PRUEBA 5: SE PERMITEN CARÁCTERES ESPECIALES
def test5_create_kit_with_special_characters_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)


#PRUEBA 6: SE PERMITEN ESPACIOS
def test6_create_kit_with_spaces_success_response():
    current_kit_body = get_kit_body(data.test6_kit_name)
    positive_assert(current_kit_body)


#PRUEBA 7: SE PERMITEN NÚMEROS
def test7_create_kit_with_numbers_success_response():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)


#PRUEBA 8: EL PARÁMETRO NO SE PASA EN LA SOLICITUD
def test8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_code_400(current_kit_body)


#PRUEBA 9: SE HA PASADO UN TIPO DE PARÁMETRO DIFERENTE (NÚMERO)
def test9_create_kit_with_different_parameters():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_code_400(current_kit_body)


