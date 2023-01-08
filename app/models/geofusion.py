from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db




class Municipios(db.Model):
    __tablename__ = "Municipio"
    __bind_key__ = 'geofusion'
    __table_args__ = {"schema": "enderecos"}
    idmunicipio = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String)
    datacadastro = db.Column(db.Integer)
    dataalterado = db.Column(db.DateTime, unique=False, nullable=False)
    bitativo = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Municipios %r>' % self.municipio


class Estados(db.Model):
    __tablename__ = "Estado"
    __bind_key__ = 'geofusion'
    __table_args__ = {"schema": "enderecos"}
    idestado = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=False)
    dataalterado = db.Column(db.DateTime, unique=False, nullable=False)
    bitativo = db.Column(db.Boolean, nullable=False)


 

    def __repr__(self):
        return '<Estados %r>' % self.estado

class Enderecos(db.Model):
    __tablename__ = "Endereco"
    __bind_key__ = 'geofusion'
    __table_args__ = {"schema": "enderecos"}

    idendereco = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String)
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String)
    tipo = db.Column(db.String)
    cep = db.Column(db.String)
    microregiao = db.Column(db.String)
    regiaogeografica = db.Column(db.String)
    enderecotipo = db.Column(db.String)
    datacadastrado = db.Column(db.DateTime, unique=False, nullable=False)
    dataalterado = db.Column(db.DateTime, unique=False, nullable=False)
    bitativo = db.Column(db.Boolean, nullable=False)
    bairro = db.Column(db.String)
    municipio = db.Column(db.String)
    estado = db.Column(db.String)
    idmunicipio = db.Column(db.Integer)
    idestado = db.Column(db.Integer)

   
    

    def __repr__(self):
        return '<Enderecos %r>' % self.idendereco
