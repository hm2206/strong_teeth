from configs.db import Base
from sqlalchemy import Column, Integer, Date, Time, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Horario(Base):
    __tablename__ = 'horarios'

    __table_args__ = (
        UniqueConstraint('turno_id', 'fecha'),
    )

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    hora_ingreso = Column(Time, nullable=False)
    hora_salida = Column(Time, nullable=False)
    turno_id = Column(Integer, ForeignKey("turnos.id"), nullable=False)

    turno = relationship("Turno")
