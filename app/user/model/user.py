from app import db

class User(db.Model):
  __tablename__ = 'user'
  dpi = db.Column(db.String(100), primary_key=True)
  name = db.Column('full_name',db.String(100))
  phone = db.Column(db.String(20))
  email = db.Column(db.String(100))
  address = db.Column(db.String(300))
  date = db.Column(db.DateTime)
  temperature = db.Column(db.Numeric(10,2))
  heartRate = db.Column('heart_rate', db.Numeric(10,2))
  hasMask = db.Column('has_mask', db.Boolean)
  hasFaceShield = db.Column('has_face_shield', db.Boolean)
  hasRules = db.Column('has_rules', db.Boolean)

  def __init__(self, dpi, fullName, phone, email, address, date, temperature, heartRate, hasMask, hasFaceShield, hasRules):
    self.dpi = dpi
    self.fullName = fullName
    self.phone = phone
    self.email = email
    self.address = address
    self.date = date
    self.temperature = temperature
    self.heartRate = heartRate
    self.hasMask = hasMask
    self.hasFaceShield = hasFaceShield
    self.hasRules = hasRules

class UserSymptoms(db.Model):
  __tablename__='user_symptoms'
  id = db.Column(db.Integer, primary_key=True)
  dpi = db.Column(db.String(100), db.ForeignKey('user.dpi'))
  date = db.Column(db.DateTime)
  symptoms = db.Column(db.Text)
  temperature =db.Column(db.Numeric(10,2))
  heartRate = db.Column('heart_rate', db.Numeric(10,2))

  def __init__(self, dpi, date, symptoms, temperature, heartRate):
    self.dpi = dpi
    self.date = date
    self.symptoms = symptoms
    self.temperature = temperature
    self.heartRate = heartRate
