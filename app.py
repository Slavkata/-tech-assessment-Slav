from flask import Flask
from flask_restful import Api
from models.db_init import db

from resources.dummy import DummiesResource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:slavkata@localhost/tech_assignment'

api.add_resource(DummiesResource, '/dummy/')

db.init_app(app)
