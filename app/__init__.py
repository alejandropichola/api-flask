from flask import Flask
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)

from app.user import userController

app.register_blueprint(userController)

CORS(app)
