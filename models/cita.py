from configs.db import Base
from sqlalchemy import Column, Text, Integer, Float, Time, ForeignKey
from sqlalchemy.orm import relationship


class Cita(Base):

    __tablename__ = "citas"

    id = Column(Integer, primary_key=True)
    asistencia = Column(Time, nullable=False)
    abono = Column(Float, nullable=False, default=0)
    descripcion = Column(Text, nullable=True)
    agenda_id = Column(Integer, ForeignKey("agendas.id"), nullable=False)
    tratamiento_id = Column(Integer, ForeignKey(
        "tratamientos.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)

    agenda = relationship("Agenda")
    tratamiento = relationship("Tratamiento")
    paciente = relationship("Paciente")
