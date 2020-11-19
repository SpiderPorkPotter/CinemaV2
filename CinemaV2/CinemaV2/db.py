# coding: utf-8
#
# USATO sqlacodegen -->
#


from flask import Boolean, Column, Date, ForeignKey, Integer, String, Table, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash


Base = declarative_base()
metadata = Base.metadata


class Attori(Base):
    __tablename__ = 'Attori'

    idAttore = Column(Integer, primary_key=True)
    Nome = Column(String(50), nullable=False)
    Cognome = Column(String(50), nullable=False)
    AnnoNascita = Column(Integer, nullable=False)
    Nazionalita = Column(String(50), nullable=False)

    Film = relationship('Film', secondary='Recita')


class Film(Base):
    __tablename__ = 'Film'

    idFilm = Column(Integer, primary_key=True)
    Titolo = Column(String(50), nullable=False)
    DurataMin = Column(Integer, nullable=False)
    Descrizione = Column(String(500), nullable=False)
    Anno = Column(Integer, nullable=False)
    Studio = Column(String(50), nullable=False)


class Sale(Base):
    __tablename__ = 'Sale'

    idSala = Column(Integer, primary_key=True)
    Nome = Column(String(50), nullable=False)
    Capienza = Column(Integer, nullable=False)


class Utenti(Base):
    __tablename__ = 'Utenti'

    idUtente = Column(Integer, primary_key=True)
    Nome = Column(String(50), nullable=False)
    Cognome = Column(String(50), nullable=False)
    Telefono = Column(Integer, nullable=False)
    EMail = Column(String(50), nullable=False)
    Password = Column(String(200), nullable=False)
    Gestore = Column(Boolean, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

        def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)


class Proiezioni(Base):
    __tablename__ = 'Proiezioni'

    idProiezione = Column(Integer, primary_key=True)
    Orario = Column(Time, nullable=False)
    Data = Column(Date, nullable=False)
    idFilm = Column(ForeignKey('Film.idFilm'), nullable=False, index=True)
    idSala = Column(ForeignKey('Sale.idSala'), nullable=False, index=True)

    Film = relationship('Film')
    Sale = relationship('Sale')


t_Recita = Table(
    'Recita', metadata,
    Column('idAttore', ForeignKey('Attori.idAttore'), primary_key=True, nullable=False, index=True),
    Column('idFilm', ForeignKey('Film.idFilm'), primary_key=True, nullable=False, index=True)
)


class Prenotazioni(Base):
    __tablename__ = 'Prenotazioni'

    idProiezione = Column(ForeignKey('Proiezioni.idProiezione'), primary_key=True, nullable=False, index=True)
    Posto = Column(Integer, nullable=False)
    idUtente = Column(ForeignKey('Utenti.idUtente'), primary_key=True, nullable=False, index=True)

    Proiezioni = relationship('Proiezioni')
    Utenti = relationship('Utenti')
