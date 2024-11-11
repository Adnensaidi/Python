from flask import render_template, redirect, session, flash, request
from flask_app import app 
from flask_app.models.user_model import User
from flask_app.models.party_model import Party

@app.route('/dashboard')
def dashboard():
    parties = Party.get_all()
    return render_template('dashboard.html', parties=parties)