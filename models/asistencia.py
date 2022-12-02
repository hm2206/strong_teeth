from enum import Enum as EnumLocal
from configs.db import Base
from sqlalchemy import Column, Integer, Time, Enum, ForeignKey


class AsistenciaTipoEnum(EnumLocal):
    Entrada = "Entrada"
    Salida = "Salida"


class Asistencia(Base):

    __tablename__ = 'asistencias'

    id = Column(Integer, primary_key=True)
    trabajador_id = Column(Integer, ForeignKey(
        "trabajadores.id"), nullable=False)
    horario_id = Column(Integer, ForeignKey("horarios.id"), nullable=False)
    tipo = Column(Enum(AsistenciaTipoEnum), nullable=False)
    marcaje = Column(Time, nullable=False)
