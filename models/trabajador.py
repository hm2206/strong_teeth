from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Trabajador(Base):

    __tablename__ = 'trabajadores'

    id = Column(Integer, primary_key=True)
    numero_essalud = Column(String(30), nullable=True)
    turno_id = Column(Integer, ForeignKey("turnos.id"), nullable=False)
    persona_id = Column(Integer, ForeignKey("personas.id"),
                        nullable=False, unique=True)

    turno = relationship("Turno")
    persona = relationship("Persona")
