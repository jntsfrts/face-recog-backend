import requests


def send_message(name, email):

    with open('./templates/index.html') as file:
        content = file.read()
        file.close()

    return requests.post(
        "https://api.mailgun.net/v3/sandboxe25c6c4b0935453b8e70c4eeff027d1b.mailgun.org/messages",
        auth=("api", "0d9f56b23cbb3d8318c8e223bc74370a-30b9cd6d-941c1c4b"),
        data={"from": "FaceRecog <jonatasfreitas20@gmail.com>",
              "to": f"{name} + <{email}>",
              "subject": "Verificação de email",
              "html": content})
