from flask import Blueprint, jsonify, request
from service import authorization_service


user = Blueprint('user', __name__)


@user.route("/user/new", methods=['POST'])
def signup():

    #name = request.json['name']
    email = request.json['email']
    token = request.json['token']
    face = request.json['face']

    response = authorization_service.try_signup(email, token, face)

    return response


@user.route("/user/face", methods=['POST'])
def find_face():
    face = request.json['face']

    return authorization_service.find_face(face)
