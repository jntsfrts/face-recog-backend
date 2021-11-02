from flask import Flask
from recognition_service import classify_face, has_face
from flask import Flask, jsonify, request
import base64
import signup_service


app = Flask("app")


@app.route("/signup", methods=['POST'])
def signup():

    name = request.json['name']
    face = request.json['face']

    response = signup_service.try_signup(name, face)

    return response


@app.route("/login", methods=['POST'])
def login():

    photo = request.json['photo']

    with open(f'./faces/current-face-test/test.jpg', 'wb') as fh:
        fh.write(base64.b64decode(photo))

    name = classify_face('test.jpg')

    return {"name": f"{str(name).title()}"}


@app.route("/login/face", methods=['POST'])
def find_face():
    face = request.json['face']

    with open(f'./faces/current-face-test/test.jpg', 'wb') as fh:
        fh.write(base64.b64decode(face))

    result = has_face('test.jpg')

    data = {'hasFace': str(result).lower()}

    return jsonify(data)


if __name__ == '__main__':
    app.run()
