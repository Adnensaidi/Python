from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re   

classlogin:def__init__(self,data):
self.id=data['id']
self.first_name=data['first_name']
self.last_name=data['last_name']
self.email=data["email"]
self.created_at=data["created_at"]
self.updated_at=data["updated_at"]
