from flask import Flask
from face_rec import classify_face, has_face
from flask import Flask, jsonify, request
import base64


app = Flask("app")


@app.route("/signup", methods=['POST'])
def signup():
    name = request.json['name']
    face = request.json['face']

    with open(f'./faces/{name}.jpg', 'wb') as fh:
        fh.write(base64.b64decode(face))

    return {"name":f"{str(name).title()}"}



@app.route("/login", methods=['POST'])
def login():

    photo = request.json['photo']

    with open(f'./test.jpg', 'wb') as fh:
        fh.write(base64.b64decode(photo))

    name = classify_face('test.jpg')

    return {"name":f"{str(name).title()}"}



@app.route("/login/face", methods=['POST'])
def find_face():
    face = request.json['face']

    with open(f'./face.jpg', 'wb') as fh:
        fh.write(base64.b64decode(face))

    result = has_face('face.jpg')
    

    data = {'hasFace': str(result).lower()}

    return jsonify(data)




if __name__ == '__main__':
    app.run()