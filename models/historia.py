from configs.db import Base
from sqlalchemy import Column, Text, Integer, Date, ForeignKey, Time, UniqueConstraint
from sqlalchemy.orm import relationship


class Historia(Base):

    __tablename__ = 'historias'

    __table_args__ = (
        UniqueConstraint('fecha_inicio', 'hora_inicio',
                         'paciente_id', name="u_historia"),
    )

    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    observacion = Column(Text, nullable=True)
    paciente_id = Column(Integer, ForeignKey(
        "pacientes.id"), nullable=False)

    odontogramas = relationship("Odontograma", back_populates="historia")

    def display_info(self):
        return f"{self.fecha_inicio} - {self.hora_inicio}"
