from configs.db import Base
from sqlalchemy import Column, Integer, String


class CondicionDental(Base):

    __tablename__ = 'condicion_dentales'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
