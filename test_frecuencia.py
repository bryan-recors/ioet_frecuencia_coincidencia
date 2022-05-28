from model import cargar_data, validar_data
from controller import obtener_frecuencia
import pytest


@pytest.mark.parametrize(
    "ruta, expected",
    {
        ('hola', None),
        ('prueba1.txt', None),
        ('prueba2.txt', None),
        ('prueba3.txt', None)
    }
)
def test_cargar_data(ruta, expected):
    assert cargar_data(ruta) == expected


def test_validar_data1():
    prueba = ['hola', 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
              'ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
    assert validar_data(prueba) == False


def test_validar_data2():
    prueba = ['ASTRID=MO25:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
    assert validar_data(prueba) == False


@pytest.mark.parametrize(
    "horarios_empleado_1, horarios_empleado_2, expected",
    {
        (('SU20:00-24:00',), ('SU20:00-21:00',), 0),
        (('SU13:00-16:00', 'TU20:00-24:00'), ('SU20:00-21:00', 'SU20:00-24:00'), 0),
        (('MO13:00-16:00', 'TH20:00-24:00'), ('MO13:00-16:00', 'TH20:00-24:00'), 2),
        (('MO13:00-16:00', 'TH20:00-24:00'), ('MO13:00-16:00', 'TH20:00-24:00'), 2),
        (('WE13:00-16:00', 'SU20:00-24:00'), ('MO13:00-16:00', 'SU20:00-24:00'), 1),
    }
)
def test_obtener_frecuencia(horarios_empleado_1, horarios_empleado_2, expected):
    assert obtener_frecuencia(horarios_empleado_1, horarios_empleado_2) == expected
