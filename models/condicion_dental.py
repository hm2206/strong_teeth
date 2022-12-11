from configs.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class CondicionDental(Base):

    __tablename__ = 'condicion_dentales'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    color_fondo = Column(String(10), nullable=False)
    color_texto = Column(String(10), nullable=False)

    odontogramas = relationship(
        "Odontograma", back_populates="condicion")
