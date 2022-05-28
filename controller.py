from view import mostrar_error_data, solicitar_ruta_archivo, mostrar_resultados
from model import cargar_data


def obtener_frecuencia(horarios_empleado_1: list, horarios_empleado_2: list) -> int:
    """ función para comparar dos horarios y devolver la frecuencia con la que se repiten"""
    frecuencia = 0
    for horario_empleado_1 in horarios_empleado_1:
        for horario_empleado_2 in horarios_empleado_2:
            dia1 = horario_empleado_1[:2]
            dia2 = horario_empleado_2[:2]
            print("dias: "+dia1+" - "+dia2)
            intervalo_tiempo1 = horario_empleado_1[2:]
            intervalo_tiempo2 = horario_empleado_2[2:]
            print("intervalo: " + intervalo_tiempo1 +" - " +intervalo_tiempo2)
            if (dia1 == dia2):
                if (intervalo_tiempo1 == intervalo_tiempo2):
                    frecuencia = frecuencia + 1
    return (frecuencia)


def obtener_pares_y_frecuencias() -> None:
    """ función para generar conbinaciones en pares de una lista de empleados sin repetición  
        y posteriormente mandar a calcular la frecuncia con la que se coinciden en la oficina
    """
    resultado = []
    ruta_archivo = solicitar_ruta_archivo()
    empleados = cargar_data(ruta_archivo)
    if empleados:
        for indice1 in range(len(empleados)):
            for indice2 in range(indice1 + 1, len(empleados)):
                par = empleados[indice1]['nombre_empleado'] + '-' + empleados[indice2]['nombre_empleado']
                horarios_empleado_1 = empleados[indice1]['horario']
                horarios_empleado_2 = empleados[indice2]['horario']
                frecuencia = obtener_frecuencia(horarios_empleado_1, horarios_empleado_2)
                resultado.append(par + ' : ' + str(frecuencia))
        mostrar_resultados(resultado)
    else:
        mostrar_error_data()
