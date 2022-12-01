from configs.db import Base
from enum import Enum as EnumLocal
from sqlalchemy import Column, UniqueConstraint, Integer, ForeignKey, Date, Time, Enum
from sqlalchemy.orm import relationship


class AgendaEstadoEnum(EnumLocal):
    Pendiente = "Pendiente"


class Agenda(Base):
    __tablename__ = 'agendas'

    __table_args__ = (
        UniqueConstraint('fecha', 'hora', 'doctor_id', name="u_agenda"),
    )

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    estado = Column(Enum(AgendaEstadoEnum), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctores.id"), nullable=False)

    doctor = relationship("Doctor")
