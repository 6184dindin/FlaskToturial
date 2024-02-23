from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/index/<username>')
def index(username):
    return render_template('index.html', name=username)

if __name__ == '__main__':
    app.run()