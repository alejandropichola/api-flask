from flask import Blueprint, request, abort
from app import app, db
import simplejson as json
import urllib3

userController = Blueprint('userController', __name__)


@app.route('/server', methods=["GET"])
def externalService():
  data = {
    'idgrupo': 13001
  }
  http = urllib3.PoolManager()
  r = http.request(
    'POST',
    'http://69.163.46.165:9999/RestSisintERP/casoscovid/findBy',
    body = json.dumps(data).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
  )
  print(r.data)
  return json.dumps(r.data)

@app.route('/server', methods=["POST"])
def externalServiceSaveCases():
  dataRequest = request.get_json()
  response = dataRequest['data']
  http = urllib3.PoolManager()
  r = http.request(
    'POST',
    'http://69.163.46.165:9999/RestSisintERP/casoscovid/saveCases',
    body = json.dumps(response).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
  )
  return json.dumps(r.data)
