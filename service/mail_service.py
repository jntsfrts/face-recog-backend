import requests
import configparser

config = configparser.RawConfigParser()
config.read('Config.properties')

MAILGUN_URL = config.get('MailGunSection', 'mail.endpoint')
MAIL_API_KEY = config.get('MailGunSection', 'mail.apikey')
MAIL_SENDER = config.get('MailGunSection', 'mail.sender')


def send_message(name, email):

    with open('./templates/index.html') as file:
        content = file.read()
        file.close()

    with open('./templates/foto_cadastrada.jpg', 'rb') as file:
        foto_cadastrada = file.read()
        file.close()

    return requests.post(
        MAILGUN_URL,
        auth=("api", MAIL_API_KEY),
        files=[("attachment", foto_cadastrada)],
        data={"from": MAIL_SENDER,
              "to": f"{name} + <{email}>",
              "subject": "Verificação de email",
              "html": content})
