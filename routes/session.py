from flask import Blueprint, jsonify, request
from service import authorization_service


session = Blueprint('session', __name__)


@session.route("/session/new", methods=['POST'])
def login():

    face = request.json['face']

    response = authorization_service.try_login(face)
    print(response)
    return response
