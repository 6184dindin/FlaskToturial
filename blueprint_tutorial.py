from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta 
from blueprint_tutorial_user import user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
app.permanent_session_lifetime = timedelta(minutes=1)
app.register_blueprint(user, url_prefix='/user')

@app.route('/')
def index():
    return redirect(url_for('user.home'))

if __name__ == '__main__':
    app.run()