"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from CinemaV2 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login_page')
def login_page():
    return render_template(
        'login.html',
        title = 'Effettua il login'
    )

@app.route('/register')
def register():
    return render_template(
        'register.html',
        title = 'Registrazione'  
    )
@app.route('/registration_processing')
def registration_processing():
    print("yeeeeeeeee sei registrato")

""" parte che processa i dati del login"""
@app.route('/login_processing')
def login_processing():
    print("yeeeeeeeee sei loggato")

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
