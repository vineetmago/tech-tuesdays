'''
Created on 14-Sep-2013

@author: vineet
'''
import calendar
from datetime import datetime

from app import db
from app.models import Month, Theme, User


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    current = datetime.now().month
    months = [Month(id=i, name=calendar.month_name[i], url="/months/{0}/themes".format(i))
              for i in range(current,current+3)]
    db.session.add_all(months)
    db.session.commit()
    
    user = User('Admin', 'admin@email.com', 'password')
    db.session.add(user)
    
    current_month = db.session.query(Month).filter(Month.id==current).first()
    current_month.themes = [Theme('Javascript', 'Javascript lanugage / frameworks', 9, user)]
    
    db.session.add(current_month)
    db.session.commit()
    
        