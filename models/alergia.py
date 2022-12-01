from configs.db import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Text


class Alergia(Base):

    __tablename__ = 'alergias'

    __table_args__ = (
        UniqueConstraint('nombre'),
    )

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
