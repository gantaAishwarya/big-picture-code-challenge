#Importing the required libraries
from flask import Flask
from flask_restful import Api
from .config import DB_config
from .extensions import db
from .fetchBook import FetchBook
from .getBooks import GetBooks
from .saveBook import SaveBooks

#Function to register required extensions
def register_extensions(app):
    #initialising db
    db.init_app(app=app)
    with app.app_context():
        db.create_all()


#Function to create application
def create_app(config):
    app = Flask(__name__)
    app.config |= config
    register_extensions(app=app)
    
    return app

#Initialising the flask application
app = create_app(DB_config)

#Adding the required resources
api = Api(app)
api.add_resource(FetchBook,'/isbn/<isbn>')
api.add_resource(GetBooks,'/books')
api.add_resource(SaveBooks,'/books')












