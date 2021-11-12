from flask import Flask
from flask import Flask, jsonify, request
from service import authorization_service


app = Flask("app")


@app.route("/user/new", methods=['POST'])
def signup():

    name = request.json['name']
    email = request.json['email']
    face = request.json['face']

    response = authorization_service.try_signup(name, email, face)

    return response


@app.route("/session/new", methods=['POST'])
def login():

    face = request.json['face']

    response = authorization_service.try_login(face)
    print(response)
    return response


@app.route("/user/face", methods=['POST'])
def find_face():
    face = request.json['face']

    return authorization_service.find_face(face)


if __name__ == '__main__':
    app.run()
