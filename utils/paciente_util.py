from models.paciente import PacienteCondicionEnum


def condicion_to_str(value: PacienteCondicionEnum):
    match value:
        case PacienteCondicionEnum.Embarazo:
            return "Embarazo"
        case PacienteCondicionEnum.Lactancia:
            return "Lactancia"
        case _:
            return "N/A"
