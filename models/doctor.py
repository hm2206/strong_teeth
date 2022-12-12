from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Doctor(Base):

    __tablename__ = 'doctores'

    id = Column(Integer, primary_key=True)
    cmp = Column(String(10), nullable=False)
    trabajador_id = Column(Integer, ForeignKey("trabajadores.id"))

    trabajador = relationship("Trabajador", back_populates="doctor")
    citas = relationship("Cita", back_populates="doctor")

    def display_info(self):
        return self.trabajador.persona.display_info()
