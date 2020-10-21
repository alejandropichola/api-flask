from app import db

class User(db.Model):
  __tablename__ = 'user'
  dpi = db.Column(db.Integer, primary_key=True, autoincrement=False)
  fullName = db.Column('full_name',db.String(100))
  phone = db.Column(db.String(20))
  email = db.Column(db.String(100))
  address = db.Column(db.String(300))
  date = db.Column(db.DateTime)
  temperature = db.Column(db.Numeric(10,2))
  heartRate = db.Column('heart_rate', db.Numeric(10,2))
  hasMask = db.Column('has_mask', db.Boolean)
  hasFaceShield = db.Column('has_face_shield', db.Boolean)
  hasRules = db.Column('has_rules', db.Boolean)

  def __init__(self, dpi, fullName):
    self.dpi = dpi
    self.fullName = fullName

class UserSymptoms(db.Model):
  __tablename__='user_symptoms'
  id = db.Column(db.Integer, primary_key=True)
  dpi = db.Column(db.Integer, db.ForeignKey('user.dpi'))
  date = db.Column(db.DateTime)
  symptoms = db.Column(db.Text)
  temperature =db.Column(db.Numeric(10,2))
  heartRate = db.Column('heart_rate', db.Numeric(10,2))