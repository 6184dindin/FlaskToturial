from flask import Blueprint, render_template, request, flash, redirect, url_for

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    return "Login"

@user.route('/register', methods=['GET', 'POST'])
def register():
    return "Register"

@user.route('/logout')
def logout():
    return "Logout"