from models.persona import Persona, PersonGeneroEnum
from configs.db import session
from models.persona import Persona
from models.usuario import Usuario, UsuarioRoleEnum
from datetime import date

persona = Persona()
persona.id = 1
persona.nombres = "Dev"
persona.apellido_paterno = "prueva"
persona.apellido_materno = "prueva"
persona.numero_identidad = "999999999"
persona.fecha_nacimiento = date(1999, 6, 22)
persona.genero = PersonGeneroEnum.Male

session.add(persona)

usuario = Usuario()
usuario.email = "dev@gmail.com"
usuario.set_password("password123")
usuario.persona_id = persona.id
usuario.role = UsuarioRoleEnum.ADMIN
usuario.estado = True

session.add(usuario)

session.commit()
