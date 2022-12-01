from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, Enum
from sqlalchemy.orm import relationship


class PacienteAlergia(Base):
    __tablename__ = 'paciente_alergias'

    __table_args__ = (
        UniqueConstraint('paciente_id', 'alergia_id', name="u_paciente_ale"),
    )

    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    alergia_id = Column(Integer, ForeignKey("alergias.id"), nullable=False)

    paciente = relationship("Paciente")
    alergia = relationship("Alergia")
