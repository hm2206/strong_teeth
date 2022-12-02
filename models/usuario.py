from configs.db import Base
from enum import Enum as EnumLocal
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, UniqueConstraint, Enum
from sqlalchemy.orm import relationship
import bcrypt


class UsuarioRoleEnum(EnumLocal):
    ADMIN = "ADMIN",
    DOCTOR = "DOCTOR",
    BASICO = "BASICO",
    PACIENTE = "PACIENTE"


class Usuario(Base):

    __tablename__ = 'usuarios'

    __table_args__ = (
        UniqueConstraint('role', 'persona_id', name="u_usuario"),
    )

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UsuarioRoleEnum), nullable=False)
    estado = Column(Boolean, nullable=False, default=True)
    persona_id = Column(Integer, ForeignKey("personas.id"), nullable=False)

    persona = relationship("Persona")

    def set_password(self, password: str):
        password_hashed = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt(14))
        self.password = password_hashed.decode("utf-8")
