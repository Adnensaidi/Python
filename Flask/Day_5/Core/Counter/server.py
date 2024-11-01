from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "clé_très_secrète_123"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)