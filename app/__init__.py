from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app.hello.main import hello

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:admin@localhost:3306/redes'
db = SQLAlchemy(app)
db.create_all()
app.register_blueprint(hello)