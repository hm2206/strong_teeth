from configs.db import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class Proveedor(Base):
    __tablename__ = 'proveedores'

    __table_args__ = (
        UniqueConstraint('razon_social', 'ruc'),
    )

    id = Column(Integer, primary_key=True)
    razon_social = Column(String(100), nullable=False)
    ruc = Column(String(40), nullable=False)
    direccion = Column(String(255), nullable=False)
    telefono = Column(String(12), nullable=False)
    representante_id = Column(
        Integer, ForeignKey("personas.id"), nullable=False)

    representante = relationship("Persona")
