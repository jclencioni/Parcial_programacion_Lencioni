from validate import *

def pedir_entero(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    """Solicita el ingreso de un numero entero y valida que lo sea y ademas esté dentro del rango de maximo y minimo inclusive.

    Args:
        mensaje (str): mensaje de solicitud de entero
        mensaje_error (str): mensaje de error en caso de que no cumpla con los parametros establecidos
        minimo (int): minimo valor permitido del numero, inclusive
        maximo (int): maximo valor permitido del numero, inclusive

    Returns:
        int: devuelve el numero ingresado en formato int.
    """
    numero = input(mensaje)
    
    while validar_maximo_minimo(numero, maximo, minimo) == False:
        numero = input(mensaje_error)
    
    entero = int(numero)
    return entero


    
