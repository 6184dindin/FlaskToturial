from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta 
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
app.permanent_session_lifetime = timedelta(minutes=1) # session will expire after 1 minute
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' # database name is users.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # stop tracking modifications on the database

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self, name, email):
        self.username = name
        self.email = email

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session.permanent = True
        if user:
            session['username'] = user
            flash('Login Successful!')
            return redirect(url_for('index'))
    elif 'username' in session:
        flash('Already Logged In!')
        return redirect(url_for('index'))
    else:
        return render_template('login.html')
    
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('home.html', name=session['username'])
    else:
        flash('You are not logged in!')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    if not path.exists('users.db'):
        db.create_all(app=app)
    app.run()