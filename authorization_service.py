import recognition_service  # recognition_service.classify_face
import base64


def try_signup(name, face):

    try:

        with open(f'./signup-test.jpg', 'wb') as fh:
            fh.write(base64.b64decode(face))

        already_registered_user = check_existing_face("signup-test.jpg")

        response = {"name": f"{str(name).title()}",
                    "status": "", "description": ""}

        if(already_registered_user == "Unknown"):
            with open(f'./faces/{name}.jpg', 'wb') as fh:
                fh.write(base64.b64decode(face))

            response["name"] = f"{str(name).title()}"
            response["status"] = "succesful"
            response["description"] = "Successfully registered user."

            return response

        response["name"] = str(already_registered_user).title()
        response["status"] = "error"
        response["description"] = "already registered user."

        return response

    except:
        return {"status": "error", "description": "invalid image."}


def try_login(face):

    with open(f'./login-test.jpg', 'wb') as fh:

        try:

            fh.write(base64.b64decode(face))

            user = check_existing_face("login-test.jpg")

            response = {"name": "", "status": "", "description": ""}

            if(user != "Unknown"):
                response["name"] = f"{str(user).title()}"
                response["status"] = "succesful"
                response["description"] = "Successfully logged in."

                return response

            response["status"] = "error"
            response["description"] = "User not found."

            return response

        except:
            return {"status": "error", "description": "invalid image."}


def find_face(face):

    with open(f'./find-face-test.jpg', 'wb') as fh:

        try:
            fh.write(base64.b64decode(face))
            result = recognition_service.find_face('find-face-test.jpg')

            # TODO trocar para foundFace
            return {'hasFace': str(result).lower()}

        except:
            return {"status": "error", "description": "invalid image."}


def check_existing_face(face):

    user_name = recognition_service.classify_face(face)

    if(user_name):
        return user_name

    return None
