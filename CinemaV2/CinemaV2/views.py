"""
Routes and views for the flask application.
"""

from datetime import datetime
from . import app
from app import db.py
from flask import Flask, render_template, redirect, request, url_for, SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/cinemaDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
@app.route('/home')
def home():
    """Renderizza la home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

""" se la richiesta per questa pagina
viene effettuata con il metodo post, e quindi l'utente ha già inserito i dati
e ha premuto invia, viene fatto il login. Altrimenti viene renderizzata la
pagina di login normale (utente non loggatp) """
@app.route('/login_page', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        conn = engine.connect()
        risp = conn.execute('SELECT password FROM Utenti WHERE email = ?',
            [request.form['logEmail']])
        veraPwd = rs.fetchone('password')
        conn.close()
        if(request.form['logPassword'] == veraPwd):
            user = user_by_email(request.form['logEmail'])
            login_user(user)
            return redirect(url_for('home_adm'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))



@app.route('/register')
def register():
    return render_template(
        'register.html',
        title='Registrazione'
    )

@app.route('/logout')
@login_required
def logout():
   logout_user() #da implementare
   return redirect(url_for('home'))

#area riservata all'admin
@app.route('/privata')
def privata():
    return render_template(
        'privata.html',
        title='Area riservata',
        year=datetime.now().year,
        message='Da qui puoi gestire gli utenti'
    )
