from configs.db import Base
from sqlalchemy import Column, Integer, String, Text


class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
