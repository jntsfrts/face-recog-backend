from service import recognition_service
from service import mail_service
import base64
import json


def try_signup(email, token, face):

    try:

        with open(f'./signup-test.jpg', 'wb') as fh:
            fh.write(base64.b64decode(face))

        already_registered_user = check_existing_face("signup-test.jpg")

        response = {"name": "",
                    "status": "", "description": ""}

        user = get_user_by(token)

        if(already_registered_user == "Unknown" and user != None):

            with open(f"./faces/{user['name']}.jpg", 'wb') as fh:
                fh.write(base64.b64decode(face))

            response["name"] = f"{str(user['name']).title()}"
            response["status"] = "succesful"
            response["description"] = "Successfully registered user."

            mail_service.send_message(user['name'], email)

            return response

        response["name"] = str(already_registered_user).title()
        response["status"] = "error"
        response["description"] = "already registered user."

        return response

    except Exception as e:
        print(e)
        return {"status": "error", "description": "invalid image."}


def try_login(face):

    with open(f'./login-test.jpg', 'wb') as fh:

        try:

            fh.write(base64.b64decode(face))

            user_name = check_existing_face("login-test.jpg")


            response = {"name": "", "status": "", "accessLevel": "", "description": ""}

            if(user_name != "Unknown"):
                
                access_level = get_access_level_by(user_name)
                
                response["name"] = f"{str(user_name).title()}"
                response["status"] = "succesful"
                response["accessLevel"] = access_level
                response["description"] = "Successfully logged in."

                return response

            response["status"] = "error"
            response["description"] = "User not found."

            return response

        except Exception as e:
            print(e)
            return {"status": "error", "description": "invalid image."}

# procurando por uma face válida


def find_face(face):

    with open(f'./find-face-test.jpg', 'wb') as fh:

        try:
            # decodificando o texto em base 64 e salvando a imagem.
            fh.write(base64.b64decode(face))
            # enviando a imagem para o serviço de detecção.
            result = recognition_service.find_face('find-face-test.jpg')

            # retornando o resultado vindo do serviço de detecção.
            return {'hasFace': str(result).lower()}

        except Exception as e:
            print(e)
            # retornando erro no caso da imagem ser inválida.
            return {"status": "error", "description": "invalid image."}


def check_existing_face(face):

    user_name = recognition_service.classify_face(face)

    if(user_name):
        return user_name

    return None


def get_user_by(token):

    users = open('credentials.txt', 'rt')
    lines = users.read().split('\n')
    user = None

    for line in lines:
        if line != '':
            user = json.loads(line)

            if (user['token'] == token):
                print(f'TOKEN [{token}] válido')
                return user
    
    print(f'TOKEN [{token}] inválido')
    return None



def get_access_level_by(name):

    users = open('credentials.txt', 'rt')
    lines = users.read().split('\n')
    user = None

    for line in lines:
        if line != '':
            user = json.loads(line)

            if (user['name'] == name):
                print(f'TOKEN [{name}] válido')
                return user['accessLevel']
    
    print(f'TOKEN [{name}] inválido')
    return None