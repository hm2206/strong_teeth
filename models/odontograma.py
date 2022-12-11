from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship


class Odontograma(Base):
    from models.condicion_dental import CondicionDental

    __tablename__ = 'odontogramas'

    __table_args__ = (
        UniqueConstraint('paciente_id', 'numero_diente', name="u_odontograma"),
    )

    id = Column(Integer, primary_key=True)
    numero_diente = Column(Integer, nullable=False)
    observacion = Column(Text, nullable=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    condicion_id = Column(Integer, ForeignKey("condicion_dentales.id"))

    paciente = relationship("Paciente")
    condicion = relationship(CondicionDental, back_populates="odontogramas")
