from flask import Blueprint, request, abort
from app import app, db
from app.user.model.user import User, UserSymptoms
import simplejson as json

userController = Blueprint('userController', __name__)

@app.route('/user', methods=['POST'])
def transactionUsers():
  dataRequest = request.get_json()
  response = dataRequest['data']
  users = []
  for item in response:
    users.append(User(
      dpi = item['dpi'],
      name = item['name'],
      phone = item['phone'],
      email = item['email'],
      address = item['address'],
      date = item['date'],
      temperature = item['temperature'],
      heartRate = item['heartRate'],
      hasMask = item['hasMask'],
      hasFaceShield = item['hasFaceShield'],
      hasRules = item['hasRules'],
    ))
  db.session.bulk_save_objects(users)
  db.session.commit()
  return json.dumps(response)


@app.route('/user', methods=['GET'])
def getAllUser():
  data = User.query.all()
  response = []
  for item in data:
    response.append({
      'dpi': item.dpi,
      'name': item.name,
      'phone': item.phone,
      'email': item.email,
      'address': item.address,
      'date': str(item.date),
      'temperature': item.temperature,
      'heartRate': item.heartRate,
      'hasMask': item.hasMask,
      'hasFaceShield': item.hasFaceShield,
      'hasRules': item.hasRules
    })
  return json.dumps(response, use_decimal=True)

@app.route('/user/<dpi>')
def getUser(dpi):
  data = User.query.filter_by(dpi=dpi).first()
  response = {
    'dpi': data.dpi,
    'name': data.name,
    'phone': data.phone,
    'email': data.email,
    'address': data.address,
    'date': str(data.date),
    'temperature': data.temperature,
    'heartRate': data.heartRate,
    'hasMask': data.hasMask,
    'hasFaceShield': data.hasFaceShield,
    'hasRules': data.hasRules,
  }
  return json.dumps(response, use_decimal=True)

@app.route('/user/<dpi>/symptoms')
def getUserSymptoms(dpi):
  data = UserSymptoms.query.filter_by(dpi=dpi).first()
  response = []
  if data==None:
    return json.dumps(response, use_decimal=True)
  for item in data:
    response.append({
      'id': item.id,
      'dpi': item.dpi,
      'date': str(item.date),
      'symptoms': item.symptoms,
      'temperature': item.temperature,
      'heartRate': item.heartRate
    })
  return json.dumps(response, use_decimal=True)

@app.route('/user/<dpi>/symptoms')
def addUserSymptoms(dpi):
  return 'test'
