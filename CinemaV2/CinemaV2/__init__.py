"""
Inizializzazione dell'applicazione
"""
import os
from . import views
from flask import Flask, LoginManager



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(16)
login = LoginManager(app)
