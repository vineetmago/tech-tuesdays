'''
Created on 14-Sep-2013

@author: vineet
'''

from flask import send_file, jsonify, request
from werkzeug.exceptions import abort

from app.models import *

from . import app


@app.route("/")
def index():
    return send_file("static/templates/index.html")

@app.route("/months.json")
def months_json():
    months = Month.query.all()
    return jsonify(months=[month.data() for month in months])

@app.route("/themes/<month>.json")
def themes_json(month):
    month = db.session.query(Month).filter(Month.id==month).first()
    if month:
        return jsonify(themes=[theme.data() for theme in month.themes])
    else:
        abort(404)
    
@app.route("/theme/<themeId>/talks.json")
def talks_json(themeId):
    theme = db.session.query(Theme).filter(Theme.id==themeId).first()
    if theme:
        return jsonify(theme={'name':theme.name,'id':theme.id}, talks=[talk.data() for talk in theme.talks])
    else:
        abort(404)

@app.route("/theme/<themeId>/talks", methods=['POST'])
def save_talk(themeId):
    name, desc, duration = tuple([request.form[n] for n in 
                                  ['name', 'description', 'duration']])
    proposer = db.session.query(User).filter(User.name=='Admin').first()
    talk = Talk(name, desc, duration, proposer, themeId)
    db.session.add(talk)
    db.session.commit()
    return jsonify(talk=talk)

@app.errorhandler(404)
def page_not_found(e):
    return send_file('static/templates/404.html'), 404

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_file('static/img/favicon.ico')