from models.usuario import UsuarioRoleEnum


def role_to_str(value: UsuarioRoleEnum):
    data = {
        UsuarioRoleEnum.ADMIN: "Admin",
        UsuarioRoleEnum.DOCTOR: "Doctor",
        UsuarioRoleEnum.PACIENTE: "Paciente",
        UsuarioRoleEnum.BASICO: "Basico"
    }

    return data[value]


def str_to_role(value: str):
    data = {
        "Admin": UsuarioRoleEnum.ADMIN,
        "Doctor": UsuarioRoleEnum.DOCTOR,
        "Paciente": UsuarioRoleEnum.PACIENTE,
        "Basico": UsuarioRoleEnum.BASICO
    }

    return data[value]


def estado_to_str(value: bool):
    return "Activo" if value else "Inactivo"


def str_to_estado(value: str):
    return value == "Activo"
