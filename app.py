from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World! </h1>'

@app.route('/admin')
def admin():
    return '<h1> Welcome to Admin Page </h1>'

@app.route('/guest/<guest>')
def guest(guest):
    return f'<h1> Welcome to Guest Page, {guest} </h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest=name))

@app.route('/user/<int:uid>')
def user_id(uid):
    if uid == 1:
        return redirect(url_for('admin'))
    else:
        return f'<h1> Welcome to User Page, {uid} </h1>'

@app.route('/index/<username>')
def index(username):
    return render_template('index.html', name=username)


if __name__ == '__main__':
    app.run()