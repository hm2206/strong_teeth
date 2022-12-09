from configs.db import Base
from enum import Enum as EnumLocal
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from models.persona import Persona


class PacienteCondicionEnum(EnumLocal):
    Embarazo = "Embarazo"
    Lactancia = "Lactancia"


class Paciente(Base):

    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    condicion = Column(Enum(PacienteCondicionEnum), nullable=True)
    persona_id = Column(Integer, ForeignKey("personas.id"),
                        nullable=False, unique=True)

    persona: Persona = relationship("Persona")
