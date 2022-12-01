from configs.db import Base, engine
from models.persona import Persona
from models.marca import Marca
from models.proveedor import Proveedor
from models.producto import Producto
from models.tratamiento import Tratamiento
from models.contacto import Contacto
from models.turno import Turno
from models.horario import Horario
from models.personal import Personal
from models.doctor import Doctor
from models.agenda import Agenda
from models.alergia import Alergia
from models.paciente import Paciente
from models.odontograma import Odontograma
from models.paciente_alergia import PacienteAlergia
from models.usuario import Usuario
from models.historia import Historia
from models.paciente_tratamiento import PacienteTratamiento
from models.asistencia import Asistencia
from models.cita import Cita


class Migration:
    def run(self):
        Base.metadata.create_all(engine)
