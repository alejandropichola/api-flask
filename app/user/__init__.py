from flask import Blueprint, request, abort
from app import app, db
from app.user.model.user import User
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
