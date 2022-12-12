from models.cita import CitaEstadoEnum


def estado_to_str(value: CitaEstadoEnum):
    data = {
        CitaEstadoEnum.Pendiente: "Pendiente",
        CitaEstadoEnum.Proceso: "Proceso",
        CitaEstadoEnum.Finalizado: "Finalizado"
    }

    return data[value]


def str_to_estado(value: str):
    data = {
        "Pendiente": CitaEstadoEnum.Pendiente,
        "Proceso": CitaEstadoEnum.Proceso,
        "Finalizado": CitaEstadoEnum.Finalizado
    }

    return data[value]
