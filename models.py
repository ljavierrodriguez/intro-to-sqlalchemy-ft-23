from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeigKey, Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Session = sessionmaker()
session = Session()


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    active = Column(Boolean, default=True)
    perfil = relationship('Perfil', uselist=False, backref="usuario") # Join [<Perfil 1>] => <Perfil 1>
    publicaciones = relationship('Publicacion', backref="usuario") # [<Publicacion 1>, <Publicacion 2>]
    

class Perfil(Base):
    __tablename__ = 'perfiles'
    id = Column(Integer, primary_key=True)
    biografia = Column(Text, default="")
    usuarios_id = Column(Integer, ForeigKey('usuarios.id'), nullable=False, unique=True)
    
    
class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    titulo = Column(Text, nullable=False)
    usuarios_id = Column(Integer, ForeigKey('usuarios.id'), nullable=False, unique=True)
    
    
