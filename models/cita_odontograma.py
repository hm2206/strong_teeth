from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey


class CitaOdontograma(Base):
    __tablename__ = 'cita_odontogramas'

    cita_id = Column(Integer, ForeignKey("citas.id"), primary_key=True)
    producto_id = Column(Integer, ForeignKey(
        "odontogramas.id"), primary_key=True)
