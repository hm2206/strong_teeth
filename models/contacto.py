from enum import Enum as EnumLocal
from configs.db import Base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey


class ContactoTipoEnum(EnumLocal):
    Telefono = "Telefono"
    Celular = "Celular"
    Correo = "Correo"


class Contacto(Base):

    __tablename__ = 'contactos'

    id = Column(Integer, primary_key=True)
    tipo = Column(Enum(ContactoTipoEnum), nullable=False)
    valor = Column(String(20), nullable=False)
    person_id = Column(Integer, ForeignKey("personas.id"), nullable=False)
