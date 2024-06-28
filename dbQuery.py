from flask import Flask

import json
import http.client

from app import db
from flow1 import handle_flow_0_subflow_0, handle_flow_0_subflow_1, handle_flow_0_subflow_2, handle_flow_0_subflow_3

app = Flask(__name__)

class UserState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.TEXT, unique=True, nullable=False)
    flow = db.Column(db.Integer, default=0)
    subFlow=db.Column(db.Integer, default=0)
    dni = db.Column(db.TEXT)
    full_name = db.Column(db.TEXT)
    client = db.Column(db.TEXT)
    sucursal = db.Column(db.TEXT)
def get_user_state(number):
    return UserState.query.filter_by(number=number).first()
def update_user_state( number , **kwargs):
    user_state = get_user_state(number)
    if not user_state:
        user_state = UserState(number=number)
        db.session.add(user_state)
    for key, value in kwargs.items():
        setattr(user_state, key, value)
        db.session.commit()







# Commands to push to production
# git add .
# git commit -m "xxx"
#  git push