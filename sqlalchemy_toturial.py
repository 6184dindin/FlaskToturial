from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta 
from flask_sqlalchemy import SQLAlchemy
from os import path
import sys

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
def index():
    return redirect(url_for('home'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session.permanent = True
        if user:
            session['username'] = user
            found_user = Users.query.filter_by(username=user).first()
            if found_user:
                flash('User already exists!')
                session["email"] = found_user.email
            else:
                usr = Users(username=user, email='temple@gmail.com')
                db.session.add(usr)
                db.session.commit()
            return redirect(url_for('home'))
    elif 'username' in session:
        flash('Already Logged In!')
        return redirect(url_for('home'))
    else:
        return render_template('login.html')
    
@app.route('/home', methods=['POST', 'GET'])
def home():
    if 'username' in session:
        username_in_session = session['username']
        if request.method == "POST":
            action = request.form['action']
            if action == 'Save Email':
                email = request.form['email']
                session['email'] = email
                found_user = Users.query.filter_by(username=username_in_session).first()
                found_user.email = email
                db.session.commit()
                flash('Email was saved!')
                return render_template('home.html', name=username_in_session, email=email)
            elif action == 'Delete User':
                Users.query.filter_by(username=username_in_session).delete()
                db.session.commit()
                session.pop('email', None)
                flash(f'User {username_in_session} was deleted!')
                return redirect(url_for('logout'))
        elif 'email' in session:
            email = session['email']
            flash('You are logged in as ' + username_in_session + ' and your email is ' + email)
            return render_template('home.html', name=username_in_session, email=email)
        return render_template('home.html', name=username_in_session)
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
        with app.app_context():
            db.create_all()
            print('Database Created!')
    print(sys.prefix)
    app.run()