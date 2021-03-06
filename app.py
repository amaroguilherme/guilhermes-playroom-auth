from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from flask_cors import CORS

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.secret_key = 'gui'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')

app.run()