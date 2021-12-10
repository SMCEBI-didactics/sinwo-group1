from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)

from WebApp import views
#from WebApp import models


