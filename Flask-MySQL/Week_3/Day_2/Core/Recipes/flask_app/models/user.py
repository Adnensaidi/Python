from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class User:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod 
    def register(cls,data):
        query="insert into users(first_name,last_name,email,password)values(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DB).query_db(query,data)
    @classmethod
    def get_by_email(cls,data):
        query="SELECT * FROM users where email =%(email)s;"
        result=connectToMySQL(DB).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM users where id =%(id)s;"
        result=connectToMySQL(DB).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    @staticmethod
    def validate(data):
        is_valide = True
        if len(data.get("first_name", "")) < 2:
            flash("First name must be at least 2 characters", "first_name")
            is_valide = False
        if len(data["last_name"])<2:
            flash("Last name must be at least 2 characters", "last_name")
            is_valide=False
        if not(EMAIL_REGEX.match(data["email"])):
            flash("email not valide","email")
            is_valide=False
        elif User.get_by_email({"email":data['email']}):
            flash("email alread taken","email")
            is_valide=False
        if len(data["password"])<7:
            flash("password must contain at least 7 characters","password")
        elif(data["password"]!=data["confirm_password"]):
            flash("password don't match","confirm_password")
            is_valide=False
        return is_valide

