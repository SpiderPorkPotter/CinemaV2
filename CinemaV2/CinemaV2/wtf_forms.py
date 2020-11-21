#pagina per gestire i form di registrazione e di login

from flask import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from .db import Utenti
#da implementare: https://www.youtube.com/watch?v=DbAKzi0kR80&ab_channel=SandeepSudhakaran
def credenziali_invalide(form, field):

    email_inserita = form.email.data
    password_inserita = field.data

    ut_obj = Utenti.query.filter_by(email = email.data).first()
    if ut_obj in None:
        raise ValidationError("Email o password errate")
    elif password_inserita != ut_obj.password:
        raise ValidationError("Email o password errate")

class FormRegistrazione(FlaskForm):
    """ form di registrazione nuovo utente """

    nome = StringField('nome_label',
        validators = [InputRequired(message = "Nome necessario"), Length(min = 4,
        max = 25, message = "Il nome dev'essere compreso tra 4 e 25 caratteri")])

    cognome = StringField('cognome_label',
            validators = [InputRequired(message = "Cognome necessario"), Length(min = 4,
            max = 25, message = "Il cognome dev'essere compreso tra 4 e 25 caratteri")])
    
    telefono = StringField('telefono_label',
        validators = [InputRequired(message = "numero di telfono necessario"), Length(min = 10,
        max = 12)])

    email = StringField('email_label',
        validators = [InputRequired(message = "Email necessaria"), Length(min = 4,
        max = 25, message = "L'email dev'essere compresa tra 4 e 25 caratteri")])
    
    password = PasswordField('password_label',
        validators = [InputRequired(message = "Password necessaria"), Length(min = 4,
        max = 25, message = "La password dev'essere compresa tra 4 e 25 caratteri")])
    
    conferma_pswd = PasswordField('conferma_pswd_label',
        validators = [InputRequired(message = "Password necessaria"),
        EqualTo('password', message = "Le password devono corrispondere")])

    submit_button = SubmitField('Registrati')

    def convalida_email(self, email):
        ut_obj = Utenti.query.filter_by(email = email.data).first()
        if ut_obj:
            raise ValidationError("L'email inserita esiste già. Inserisci un'email differente.")

class FormLogin(FlaskForm):
    """ Form per effettuare il login """

    email = StringField('email_label',
        validators = [InputRequired(message = "Email necessaria")])

    password = StringField('passord_label',
        validators = [InputRequired(message = 'Password necessaria'),
        credenziali_invalide])
    
    submit_button = SubmitField('Login')