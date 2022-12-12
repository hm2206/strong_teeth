from configs.db import Base, engine
from models.persona import Persona
from models.marca import Marca
from models.proveedor import Proveedor
from models.producto import Producto
from models.tratamiento import Tratamiento
from models.contacto import Contacto
from models.turno import Turno
from models.horario import Horario
from models.trabajador import Trabajador
from models.doctor import Doctor
from models.alergia import Alergia
from models.paciente import Paciente
from models.odontograma import Odontograma
from models.paciente_alergia import PacienteAlergia
from models.usuario import Usuario
from models.historia import Historia
from models.paciente_tratamiento import PacienteTratamiento
from models.asistencia import Asistencia
from models.cita import Cita
from models.cita_odontograma import CitaOdontograma
from models.cita_producto import CitaProducto


class Migration:
    def run(self):
        Base.metadata.create_all(engine)
