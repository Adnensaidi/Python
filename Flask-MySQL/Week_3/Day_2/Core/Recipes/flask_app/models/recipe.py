from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class Recipe: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_min=data["under_30_min"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]  
        self.user_id = data['user_id']
        self.posted_by=""
    

    @staticmethod
    def validate(data):
        is_valid=True
        if(len(data['name'])<2):
            is_valid=False
            flash('name too short',"name")
        if (len(data["instructions"])<2):
            is_valid=False
            flash("instructions too short","instructions")
        if (len(data["instructions"])<1):

            is_valid=False
            flash("description too short","description")
        if (data["date_made"]==""):
            is_valid=False
            flash("data is required","date_made")
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def create(cls,data): 
        query="insert into recipes (name, description, instructions, date_made, under_30_min, user_id)values(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30_min)s, %(user_id)s)"
        return connectToMySQL(DB).query_db(query,data) 
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query,data)
        return cls(result[0])
    
    @classmethod 
    def get_by_id(cls,data):
        query="select *from recipes join users on recipes.user_id=users.id where recipes.id=%(id)s;" 
        result=connectToMySQL(DB).query_db(query,data)
        recipe=cls(result[0])
        recipe.posted_by=f'{result[0]["first_name"]}{result[0]["last_name"]}'
        return recipe
    
    @classmethod 
    def update(cls,data): 
        query="update recipe set name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under_30_minutes=%(under_30_minutes)s where id=%(id)s;"
        result=connectToMySQL(DB).query_db(query,data) 
        return result
    
    @classmethod 
    def delete(cls,data): 
        qurey="delete form recipes where id =%(id)s;" 
        result=connectToMySQL(DB).query_db(qurey,data) 
        return result
    
    @classmethod
    def get_recipes( cls , data ):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL('users').query_db( query , data )
        recipes = cls( results[0] )
        for row_from_db in results:
            users_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : row_from_db["password"],
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
                }
            recipes.users.append( users_data.user( users_data ) )
        return recipes
