from flask import Flask
from flask import Flask, jsonify, request
import base64
import authorization_service


app = Flask("app")


@app.route("/signup", methods=['POST'])  # TODO mudar para /user/new
def signup():

    name = request.json['name']
    face = request.json['face']

    response = authorization_service.try_signup(name, face)

    return response


@app.route("/login", methods=['POST'])  # TODO mudar para /session/new
def login():

    face = request.json['face']

    response = authorization_service.try_login(face)
    print(response)
    return response


# TODO mudar para /user/new


@app.route("/login/face", methods=['POST'])
def find_face():
    face = request.json['face']

    return authorization_service.find_face(face)


if __name__ == '__main__':
    app.run()
