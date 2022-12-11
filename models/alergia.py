from configs.db import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Text
from sqlalchemy.orm import relationship


class Alergia(Base):

    __tablename__ = 'alergias'

    __table_args__ = (
        UniqueConstraint('nombre'),
    )

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)

    pacientes = relationship(
        "Paciente", secondary="paciente_alergias", back_populates="alergias")
