'''
Created on 14-Sep-2013

@author: vineet
'''

from flask import send_file, json, jsonify

from app.models import Month

from . import app


@app.route("/")
def index():
    return send_file("static/templates/index.html")

@app.route("/months.json")
def months_json():
    months = Month.query.all()
    return jsonify(months=[month.data() for month in months])

@app.route("/themes/<month>")
def themes_json(month):
    return "{}"