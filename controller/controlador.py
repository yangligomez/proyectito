import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from modelo.estudiante_funciones import obtener_estudiante_por_usuario
from modelo.recepcionista_funciones import obtener_recepcionista_por_usuario



def verificar_credenciales_estudiante(usuario, password):
    """
    Verifica si existe un estudiante con el usuario y contraseña dados.
    Retorna el estudiante si es válido, o None si no lo es.
    """
    estudiante = obtener_estudiante_por_usuario(usuario)
    if estudiante and estudiante['password'] == password:
        return estudiante
    return None


def verificar_credenciales_recepcionista(usuario, password):
    recepcionista = obtener_recepcionista_por_usuario(usuario)
    if recepcionista and recepcionista['password'] == password:
        return recepcionista
    return None

from proyectito.modelo.administrador import Administrador

def agregar_recepcionista(datos):
    Administrador.agregar_recepcionista(datos)

def editar_recepcionista(cedula, nuevos_datos):
    Administrador.editar_recepcionista(cedula, nuevos_datos)

def eliminar_recepcionista(cedula):
    Administrador.eliminar_recepcionista(cedula)

def agregar_estudiante(datos):
    Administrador.agregar_estudiante(datos)

def editar_estudiante(cedula, nuevos_datos):
    Administrador.editar_estudiante(cedula, nuevos_datos)

def eliminar_estudiante(cedula):
    Administrador.eliminar_estudiante(cedula)

def agregar_curso(datos):
    Administrador.agregar_curso(datos)

def editar_curso(id_curso, nuevos_datos):
    Administrador.editar_curso(id_curso, nuevos_datos)

def eliminar_curso(id_curso):
    Administrador.eliminar_curso(id_curso)

def generar_informe_inscripciones():
    return Administrador.generar_informe_inscripciones()