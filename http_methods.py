from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
app.permanent_session_lifetime = timedelta(minutes=1)

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
    app.run()