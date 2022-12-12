from configs.db import Base
from enum import Enum as EnumLocal
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship


class PacienteCondicionEnum(EnumLocal):
    Embarazo = "Embarazo"
    Lactancia = "Lactancia"


class Paciente(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    condicion = Column(Enum(PacienteCondicionEnum), nullable=True)
    persona_id = Column(Integer, ForeignKey("personas.id"),
                        nullable=False, unique=True)

    persona = relationship("Persona")
    citas = relationship("Cita", back_populates="paciente")
    alergias = relationship(
        "Alergia", secondary="paciente_alergias", back_populates="pacientes", lazy='dynamic', passive_deletes=True)
