from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class PacienteTratamiento(Base):
    __tablename__ = 'paciente_tratamientos'

    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    tratamiento_id = Column(Integer, ForeignKey(
        "tratamientos.id"), nullable=False)

    paciente = relationship("Paciente")
    tratamiento = relationship("Tratamiento")
