'''
Created on 14-Sep-2013

@author: vineet
'''

from datetime import datetime

from flask import send_file, jsonify, request, json
from werkzeug.exceptions import abort

from app.models import *

from . import app


@app.route("/")
def index():
    return send_file("static/templates/index.html")

@app.route("/months.json")
def months_json():
    months = Month.query.all()
    current_month = filter(lambda m: m.id == datetime.now().month, months)[0]
    return jsonify(months=[month.data() for month in months], 
                   themes=[theme.data() for theme in current_month.themes])

@app.route("/months/<monthId>/themes.json")
def themes_json(monthId):
    month = db.session.query(Month).filter(Month.id==monthId).first()
    if month:
        return jsonify(themes=[theme.data() for theme in month.themes])
    else:
        abort(404)
        
@app.route("/months/<monthId>/themes", methods=['POST'])
def save_theme(monthId):
    data, _ = request.form.items()[0]
    data = json.loads(data)
    name, desc = tuple([data.get(n, None) for n in ('name', 'description')])
    proposer = db.session.query(User).filter(User.name=='Admin').first()
    theme = Theme(name, desc, monthId, proposer)
    db.session.add(theme)
    db.session.commit()
    return themes_json(monthId)

@app.route("/themes/<themeId>/voteUp", methods=['GET', 'POST'])
def vote_up_theme(themeId):
    theme = db.session.query(Theme).filter(Theme.id==themeId).first()
    user = db.session.query(User).filter(User.name=='Admin').first()
    vt = ThemeVotes(themeId, user.id)
    db.session.add(vt)
    db.session.commit()
    return themes_json(theme.month_id)
    
@app.route("/themes/<themeId>/talks.json")
def talks_json(themeId):
    theme = db.session.query(Theme).filter(Theme.id==themeId).first()
    if theme:
        return jsonify(theme={'name':theme.name,'id':theme.id}, talks=[talk.data() for talk in theme.talks])
    else:
        abort(404)

@app.route("/themes/<themeId>/talks", methods=['POST'])
def save_talk(themeId):
    data, _ = request.form.items()[0]
    data = json.loads(data)
    name, desc, duration = tuple([data.get(n, None) for n in ('name', 'description', 'duration')])
    proposer = db.session.query(User).filter(User.name=='Admin').first()
    talk = Talk(name, desc, duration, proposer, themeId)
    db.session.add(talk)
    db.session.commit()
    return talks_json(themeId)

@app.route("/talks/<talkId>/voteUp", methods=['GET', 'POST'])
def vote_up_talkId(talkId):
    talk = db.session.query(Talk).filter(Talk.id==talkId).first()
    user = db.session.query(User).filter(User.name=='Admin').first()
    vt = TalkVotes(talkId, user.id)
    db.session.add(vt)
    db.session.commit()
    return talks_json(talk.theme_id)

@app.errorhandler(404)
def page_not_found(e):
    return send_file('static/templates/404.html'), 404

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_file('static/img/favicon.ico')