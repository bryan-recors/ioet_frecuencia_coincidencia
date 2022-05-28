import re


def validar_data(data_archivo):
    """Validar que todos los registros en el archivo sean correctos
    """
    expresion_validar_nombre = "^[a-zA-Z]+="  # buscar cualquier nombre seguido del =
    expresion_dia = "^([MTWFS][OUEHRA])"
    expresion_Hora = "([0-1][0-9]|2[0-3])(:)([0-5][0-9])"
    expresion_validar_horario = (expresion_dia + expresion_Hora + '(-)' + expresion_Hora + '$')
    data_valida = False
    if len(data_archivo) >= 5:
        for valor in data_archivo:
            if re.findall(expresion_validar_nombre, valor):
                if (valor[-1] == '\n'):
                    horario = (valor[valor.find('=') + 1:len(valor) - 1])
                else:
                    horario = (valor[valor.find('=') + 1:len(valor)])
                horario = horario.split(",")
                for valor in horario:
                    if re.findall(expresion_validar_horario, valor):
                        data_valida = True
                    else:
                        data_valida = False
                        break
            else:
                break
    else:
        print("La data debe tener por lo menos 5 registros")
    return data_valida


def preparar_data(data_archivo: list) -> list:
    """formar una lista de diccionarios para devolver la data más organizada
    """
    data_preparada = []
    for valor in data_archivo:
        nombre = valor[:valor.find('=')]
        print(nombre)
        if (valor[-1] == '\n'):
            horario = (valor[valor.find('=') + 1:len(valor) - 1])
        else:
            horario = (valor[valor.find('=') + 1:len(valor)])
        horario = horario.split(",")
        empleado = {"nombre_empleado": nombre, "horario": horario}
        data_preparada.append(empleado)
    return data_preparada


def cargar_data(ruta: str) -> list:
    """Función para cargar la data que viene del archivo txt
    """
    try:
        with open(ruta) as file_object:
            data_archivo = file_object.readlines()
            if validar_data(data_archivo):
                data = preparar_data(data_archivo)
                return data
    except:
        print("Error la dirección del archivo es incorrecta")
        return None
