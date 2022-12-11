from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship


class Odontograma(Base):
    from models.condicion_dental import CondicionDental

    __tablename__ = 'odontogramas'

    __table_args__ = (
        UniqueConstraint('historia_id', 'numero_diente', name="u_odontograma"),
    )

    id = Column(Integer, primary_key=True)
    numero_diente = Column(Integer, nullable=False)
    observacion = Column(Text, nullable=True)
    historia_id = Column(Integer, ForeignKey("historias.id"))
    condicion_id = Column(Integer, ForeignKey("condicion_dentales.id"))

    historia = relationship("Historia", back_populates="odontogramas")
    condicion = relationship(CondicionDental, back_populates="odontogramas")
