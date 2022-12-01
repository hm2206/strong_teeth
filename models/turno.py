from configs.db import Base
from sqlalchemy import Column, Integer, String


class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), nullable=False)
