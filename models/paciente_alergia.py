from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey


class PacienteAlergia(Base):
    __tablename__ = 'paciente_alergias'

    paciente_id = Column(Integer, ForeignKey("pacientes.id"), primary_key=True)
    alergia_id = Column(Integer, ForeignKey("alergias.id"), primary_key=True)
