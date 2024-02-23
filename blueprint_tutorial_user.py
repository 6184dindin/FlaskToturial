from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        session.permanent = True
        if user:
            session['username'] = user
            flash('Login Successful!')
            return redirect(url_for('user.home'))
    elif 'username' in session:
        flash('Already Logged In!')
        return redirect(url_for('user.home'))
    else:
        return render_template('login.html')
    
@user.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('user.login'))
    
@user.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', name=session['username'])
    else:
        flash('You are not logged in!')
        return redirect(url_for('user.login'))