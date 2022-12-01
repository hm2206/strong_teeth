from configs.db import Base
from sqlalchemy import Column, Text, Integer, Date, ForeignKey, Time
from sqlalchemy.orm import relationship


class Historia(Base):

    __tablename__ = 'historias'

    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    observacion = Column(Text, nullable=True)
    paciente_id = Column(Integer, ForeignKey(
        "pacientes.id"), nullable=False, unique=True)

    paciente = relationship("Paciente")
