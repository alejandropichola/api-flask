from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

uri = 'mysql+pymysql://{}:{}@{}:3306/{}'.format(
  os.environ.get('DATABASE_USER'),
  os.environ.get('DATABSE_PASSWORD'),
  os.environ.get('DATABASE_SERVER'),
  os.environ.get('DATABASE_NAME')
)

app.config['SQLALCHEMY_DATABASE_URI']=uri
db = SQLAlchemy(app)

from app.hello.main import hello
from app.user import userController

app.register_blueprint(hello)
app.register_blueprint(userController)

CORS(app)

migrate = Migrate(app, db)
