from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey


class CitaProducto(Base):
    __tablename__ = 'cita_productos'

    cita_id = Column(Integer, ForeignKey("citas.id"), primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), primary_key=True)
