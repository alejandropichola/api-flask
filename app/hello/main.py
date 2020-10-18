from flask import Blueprint, request,render_template, abort, jsonify
from app import app

hello = Blueprint('hello', __name__)

@app.route('/hello', methods=['GET'])
def helloWorld():
  data='hola'
  return jsonify(data)