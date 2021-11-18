from flask import Flask
from flask import Flask, jsonify, request
from service import authorization_service
from routes import user
from routes import session


app = Flask(__name__)

app.register_blueprint(user.user)
app.register_blueprint(session.session)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
