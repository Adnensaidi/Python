from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
from datetime import datetime


class Party :
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.location=data['location']
        self.date=data['date']
        self.all_ages=data['all_ages']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.poster =""
        self.fav = Party.get_fav_users({'party_id': self.id})


    @classmethod
    def save(cls,data):
        query="INSERT INTO parties (title,location,date,all_ages,description) VALUES (%(title)s,%(location)s,%(date)s,%(all_ages)s,%(description)s) ;"
        results= connectToMySQL(DB).query_db(query,data)
        return results 


    @classmethod
    def get_all(cls):
        query="SELECT * FROM parties JOIN users on parties.user_id = users.id;"
        results= connectToMySQL(DB).query_db(query,data)
        all_parties=[]
        for row in results :
            party = cls(row)
            party.poster=f"{row['first_name']} {row['last_name=']}"
            all_parties.append(party)
        return all_parties


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM parties JOIN users on parties.user_id=users.id WHERE parties.id = %(id)s ;"
        results=connectToMySQL(DB).query_db(query,data)
        party=cls(results[0])
        party.poster=results[0]['first_name']+" "+results[0]['last_name']
        return party 


    @classmethod
    def update(clas,data) :
        query="UPDATE parties SET title=%(title)s,location=%(location)s=%(date)s,all_ages=%(all_ages)s,description=%(description)s WHERE  users.id=%(id)s ; "
        return connectToMySQL(DB).query_db(query,data)


    @staticmethod
    def validate_party( data ):
        is_valid = True
        if len(data['title'])< 3 :
            is_valid=False
        flash("title must contain at least 3 chracaters","title_validation")
        if len(data['location'])<3:
            is_valid=False
        flash("location must contain at least 3 chracaters","location_validation")
        if data['data']== "":
            flash("Date is required ","date-validation")
        elif data['data'] < datetime.now():
            is_valid=False
            flash("Date must bein the future","date_validation")
        return is_valid


        @classmethod
        def add_fav(cls,data):
            query ="INSERT INTO favorites (user_id,party_id) VALUES %(user_id)s,%(party_id)s"
            return  connectToMySQL(DB).query_db(query,data)


        @classmethod
        def remove_fav(cls,data):
            query="DELETE FROM favorites WHERE user_id=%(user_id)s AND party_id=%(party_id)s"
            return connectToMySQL(DB).query_db(query,data)


        @classmethod
        def get_fav(cls,data):
            query="SELECT FROM parties JOIN favorites ON favorites.party_id=parties.id) JOIN users ON users.id=favorites.user_id WHERE favorites.user_id=%(user_id)s"
            results=connectToMySQL(DB).query_db(query,data)
            all_parties=[]
            for row in results :
                party= cls(row)
                    

