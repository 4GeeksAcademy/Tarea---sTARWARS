import os
import sys
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column, relationship

Base = declarative_base()



class Usuario(Base):
    __tablename__ = "usuario"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    # variable que tiene la lista de ,is favoritos 
    favoritos = relationship(back_populates="user")
   


class Personajes(Base):
    __tablename__ = "personajes"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    tamaño = mapped_column(String(50))

   
class Planetas(Base):
    _tablename_ = "planetas"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    
    

class Favoritos(Base):
    _tablename_ = "favoritos"

    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False) 
    planeta_id = mapped_column(Integer, ForeignKey("planetas.id"), nullable=True)  
    personajes_id = mapped_column(Integer, ForeignKey("personajes.id"), nullable=True)
    usuario_id = mapped_column(Integer, ForeignKey("usuario.id"))
    # variables vistuales 
    personajes = relationship(backref="personajes")
    planetas =  relationship(backref="planetas")
    user = relationship(back_populates="favoritos")


# Relacion bidirecional una llama a la otra 
# user = relationship(back_populates="favoritos")
# favoritos = relationship(back_populates="user")

# backref 
   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')