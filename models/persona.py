from enum import Enum as EnumLocal
from configs.db import Base
from sqlalchemy import Column, Integer, String, Date, UniqueConstraint, Enum


class PersonGeneroEnum(EnumLocal):
    Male = "M"
    Female = "F"


class Persona(Base):
    __tablename__ = 'personas'

    __table_args__ = (
        UniqueConstraint('numero_identidad'),
    )

    id = Column(Integer, primary_key=True)
    nombres = Column(String(40), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=True)
    numero_identidad = Column(String(10), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(Enum(PersonGeneroEnum), nullable=False)
