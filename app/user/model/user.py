from app import db

class User(db.Model):
  __tablename__ = 'user'
  dpi = db.Column(db.Integer, primary_key=True, autoincrement=False)
  fullName = db.Column('full_name',db.String(100))

  def __init__(self, dpi, fullName):
    self.dpi = dpi
    self.fullName = fullName