'''
Created on 14-Sep-2013

@author: vineet
'''
from app import db


class BaseModel():
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

class Month(BaseModel, db.Model):
    __tablename__ = 'months'
    
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url
        
    name = db.Column(db.String(100))
    url = db.Column(db.String(100))
    themes = db.relationship("Theme")
    
    def data(self):
        return {k:v for k,v in self.__dict__.items() if k in ['id','name','url']}
    
class User(BaseModel, db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(1024), nullable=True)

    def __init__(self, name, email, password=None):
        self.name = name
        self.email = email
        self.password = password
        
    def data(self):
        return {k:v for k,v in self.__dict__.items() if k in ['email','name']}
    
class Theme(BaseModel, db.Model):
    __tablename__ = 'themes'
    
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    month_id = db.Column(db.Integer, db.ForeignKey('months.id'), nullable=False)
    proposer = db.relationship("User")
    talks = db.relationship("Talk")
    votes = db.relationship("ThemeVotes")
    
    def __init__(self, name, description, month_id, proposer):
        self.name = name
        self.description = description
        self.month_id = month_id
        self.proposer = proposer
        
    
    def data(self):
        d = {k:v for k,v in self.__dict__.items() if k in ['id', 'name', 'description']}
        d['proposer'] = self.proposer.name
        d['voteCount'] = len(self.votes)
        return d
    
    
class ThemeVotes(BaseModel, db.Model):
    __tablename__ = 'theme_votes'
    theme_id = db.Column(db.Integer, db.ForeignKey('themes.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    voter = db.relationship("User")
    
    def __init__(self, themeId, userId):
        self.theme_id = themeId
        self.user_id = userId


class Talk(BaseModel, db.Model):
    __tablename__ = 'talks'
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    theme_id = db.Column(db.Integer, db.ForeignKey('themes.id'), nullable=False)
    proposer = db.relationship("User")
    votes = db.relationship("TalkVotes")
    
    def __init__(self, name, description, duration, proposer, theme_id=None):
        self.name = name
        self.description = description
        self.duration = duration
        self.proposer = proposer
        self.theme_id = theme_id
    
    def data(self):
        d = {k:v for k,v in self.__dict__.items() if k in ['id', 'name', 'description', 'duration']}
        d['proposer'] = self.proposer.name
        d['voteCount'] = len(self.votes)
        return d


class TalkVotes(BaseModel, db.Model):
    __tablename__ = 'talk_votes'
    talk_id = db.Column(db.Integer, db.ForeignKey('talks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    voter = db.relationship("User")
    
    def __init__(self, talkId, userId):
        self.talk_id = talkId
        self.user_id = userId
