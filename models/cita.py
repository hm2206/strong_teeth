from configs.db import Base
from enum import Enum as EnumLocal
from sqlalchemy import Column, Text, Integer, Float, Time, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship


class CitaEstadoEnum(EnumLocal):
    Pendiente = "Pendiente"
    Proceso = "Proceso"
    Finalizado = "Finalizado"


class Cita(Base):

    __tablename__ = "citas"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctores.id"), nullable=False)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    estado = Column(Enum(CitaEstadoEnum), nullable=False)
    detalles = Column(Text, nullable=True)
    tratamiento_id = Column(Integer, ForeignKey("tratamientos.id"))
    precio = Column(Float, nullable=False)
    pagado = Column(Float, nullable=False)

    paciente = relationship("Paciente", back_populates="citas")
    doctor = relationship("Doctor", back_populates="citas")
    tratamiento = relationship("Tratamiento", back_populates="citas")
    odontogramas = relationship(
        "Odontograma", secondary="cita_odontogramas", back_populates="citas")
    productos = relationship(
        "Producto", secondary="cita_productos", back_populates="citas")

    def display_info(self):
        return f"{self.fecha} - {self.hora}"
