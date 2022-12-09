from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from models.paciente import Paciente
from models.condicion_dental import CondicionDental


class Odontograma(Base):
    __tablename__ = 'odontogramas'

    __table_args__ = (
        UniqueConstraint('paciente_id', 'numero_diente', name="u_odontograma"),
    )

    id = Column(Integer, primary_key=True)
    numero_diente = Column(Integer, nullable=False)
    observacion = Column(Text, nullable=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    condicion_id = Column(Integer, ForeignKey(
        "condicion_dentales.id"), nullable=False)

    paciente: Paciente = relationship("Paciente")
    condicion: CondicionDental = relationship("CondicionDental")
