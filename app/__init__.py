from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for

app = Flask(__name__)

app.config.from_object('config')

app.url_map.strict_slashes = False

from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager

db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)

from views import *