from flask import Flask, render_template, request, redirect
from model import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_users.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    user_id=User.save(request.form)
    return redirect('/users/'+str(user_id))

@app.route('/users/<int:id>')
def display_user(id):
    user = User.get_one({'id':id})
    return render_template("readone.html",user=user)

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    user_id=User.save(request.form)
    return redirect('/users/'+str(user_id))

@app.route('/users/<int:id>/edit')
def display_user(id):
    user = User.get_one({'id':id})
    return render_template("edit.html",user=user)



if __name__=="__main__":
    app.run(debug=True)