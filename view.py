def solicitar_ruta_archivo() -> str:
    """Función para solicitar la dirección del archivo txt para analizar"""
    print("\n\t Pares de empleados y la frecuencia con la que han coincidido en la oficina.\n")
    ruta_archivo = input("Ingrese la ruta o dirección del archivo: \n")
    if (ruta_archivo == ''):
        print('No ha ingresado ninguna dirección, se cargará el archivo por defecto\n')
        ruta_archivo = 'horario.txt'
    return ruta_archivo


def mostrar_resultados(pares_y_frecuencia: list) -> None:
    """Función para mostrar los resultados"""
    print("\n\t {} Resultados de los pares y frecuencias\n".format(len(pares_y_frecuencia)))
    for par_y_frecuencia in pares_y_frecuencia:
        print(par_y_frecuencia)


def mostrar_error_data() -> None:
    """Función para mostrar mensaje de error en la Data"""
    print(" existe errores en los registros")
