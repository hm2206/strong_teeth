from configs.db import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Doctor(Base):

    __tablename__ = 'doctores'

    id = Column(Integer, primary_key=True)
    cmp = Column(String(10), nullable=False)
    personal_id = Column(Integer, ForeignKey("personales.id"), nullable=False)

    personal = relationship("Personal")
