from recognition_service import classify_face, has_face
import base64



def try_signup(name, face):
    
    with open(f'./test.jpg', 'wb') as fh:
        fh.write(base64.b64decode(face))
    
    already_registered_user = check_existing_face("test.jpg")
    
    response = {"name": f"{str(name).title()}", "status": "", "description": ""}


    if(not already_registered_user):
        with open(f'./faces/{name}.jpg', 'wb') as fh:
            fh.write(base64.b64decode(face))

        
        response["status"] = "succesful"
        response["description"] = "Successfully registered user."

        return response
        
    response["status"] = "error"
    response["descrption"] = "already registered user."

    return response


def check_existing_face(face):
    user_name = classify_face(face)

    if(user_name):
        return False

    return True


    
