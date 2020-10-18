from flask import Blueprint, request, abort, jsonify
from app import app
from app.user.model.user import User

userController = Blueprint('userController', __name__)

@app.route('/user', methods=['GET'])
def getAllUser():
  data='users'
  return jsonify(data)