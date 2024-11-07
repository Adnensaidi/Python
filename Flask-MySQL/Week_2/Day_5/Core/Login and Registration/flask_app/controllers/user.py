from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/registration',methods=['POST'])
def register():
    if User.validate_user(request.form):
        pw_hash=bcrypt.generate_password_hash(request.form['password'])
        data={**request.form,'password':pw_hash}
        user_id=User.save(data) #we save the users id in the variable user_id 
        session['user_id']=user_id # the session is used to keep the user logged in after a successful registration
        return redirect('/dashboard')
    return redirect('/')


@app.route('/login',methods=['POST'])
def login():
    # see if the email provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("User not found",'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("User not found",'login')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect('/dashboard')


@app.route('/dashboard')
def display_user():
    if 'user_id' not in session :
        return redirect('/')
    user=User.get_one({'id':session['user_id']})
    return render_template("dashboard.html",user=user)



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




