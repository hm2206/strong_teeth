from configs.db import Base
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship


class Tratamiento(Base):
    __tablename__ = 'tratamientos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
    precio = Column(Float, nullable=False, default=0)

    citas = relationship("Cita", back_populates="tratamiento")

    def display_info(self):
        return self.nombre
