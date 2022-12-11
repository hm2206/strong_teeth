from configs.db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    precio_compra = Column(Float, nullable=False, default=0)
    precio_venta = Column(Float, nullable=False, default=0)
    descripcion = Column(Text, nullable=True)
    marca_id = Column(Integer, ForeignKey("marcas.id"), nullable=True)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=True)

    marca = relationship("Marca")
    proveedor = relationship("Proveedor")
