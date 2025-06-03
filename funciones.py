from inputs import *
from validate import *

def crear_array(cantidad_elementos: int, valor_inicial: any = None) -> list:
    """Crea un array con la cantidad y valor de los elementos que se le indique, por defecto el valor inical es None.

    Args:
        cantidad_elementos (int): cantidad de elementos que tendrá el array
        valor_inicial (any): valor que tendran los elementos creados.
    Returns:
        array (list): retorna el array ya creado.
    """
    array = [valor_inicial] * cantidad_elementos 
    
    return array
    
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    """Crea una matriz segun la cantidad de columnas y filas que se le indique

    Args:
        cantidad_filas (int): cantidad de filas que tendrá la matriz
        cantidad_columnas (int): cantidad de columnas que tendrá la matriz
        valor_inicial (any): valor inicial que tendrá cada elemento de a matriz

    Returns:
        list: retorna la matriz creada.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def cargar_nombres_participantes(array_nombres:list) -> list:
    """Carga los nombres ingresados en el array que se le brinde.

    Args:
        array_nombres (list): _description_
    """
    for i in range(len(array_nombres)):
        nombre = input(f"Ingrese nombre del participante {i+1}: ")
        while validar_nombre(nombre) == False:
            nombre = input("Por favor, ingrese un nombre válido, debe tener al menos 3 caracteres alfabéticos: ")
        array_nombres[i] = nombre

    return array_nombres

def cargar_puntuaciones(matriz_puntos:list, array_nombres: list) -> list:
    """Realiza una carga secuencial en la matriz que se le brinde y la devuelve ya con los datos ingresados.

    Args:
        matriz_puntos (list): es la matriz en la que se cargarán los puntajes
        array_nombres (list): array que contiene el nombre de los participantes.
    Returns:
        list: Retorna la matiz con los puntajes ya cargados
    """
    for fil in range(len(matriz_puntos)):
        for col in range(len(matriz_puntos[0])):
            puntaje = pedir_entero(f"Ingrese el puntaje del jurado {col + 1} para el participante {array_nombres[fil]}: ", f"La nota debe ser un número del 1 al 10. Por favor, reingrese la nota del jurado {col +1} para el participante {array_nombres[fil]}: ", 1, 10)
            matriz_puntos[fil][col] = puntaje
    
    return matriz_puntos

def mostrar_participante(matriz_puntajes:list, array_nombres: list, fila: int) -> None:
    """imprime en consola los puntajes y que recibió el participante indicado y su promedio.

    Args:
        matriz_puntajes (list): Matriz que contiene el puntaje de todos los participantes.
        array_nombres (list): array con los nombres de todos los participantes.
        fila (int): indice de la fila que correponde al participante en la matriz.
    """
    print(f"NOMBRE PARTICIPANTE: {array_nombres[fila]}")
    
    for col in range(len(matriz_puntajes[fila])):
        print(f"PUNTAJE DEL JURADO {col + 1}: {matriz_puntajes[fila][col]}")
        
    print(f"PUNTAJE PROMEDIO: {promediar_fila(matriz_puntajes, fila)}/10")

def mostrar_puntajes(matriz_puntajes: list, array_nombres: list) -> None:
    """imprime en consola los puntajes y promedios de todos los participantes.

    Args:
        matriz_puntajes (list): Matriz que contiene el puntaje de todos los participantes.
        array_nombres (list): array con los nombres de todos los participantes.
    """
       
    for fil in range(len(matriz_puntajes)):
        mostrar_participante(matriz_puntajes, array_nombres, fil)  
        print("")

def sumar_fila(matriz: list, fila: int) -> int:
    """Suma todos los valores de la fila que se le indique de una matriz

    Args:
        matriz (list): matriz que contiene todas las filas.
        fila (int): indice de la fila que sumará.

    Returns:
        int: retorna la suma de toda la fila
    """
    suma = 0
    
    for i in range(len(matriz[fila])):
        suma += matriz[fila][i]
    
    return suma

def promediar_fila(matriz_puntajes: list, fila: int) -> float:
    """realiza el promedio de todos los numeros que contenga una fila.

    Args:
        matriz_puntajes (list): matriz que contiene los puntajes de todos los participantes 
        fila (int): indice de la fila que promediará

    Returns:
        float: retorna el promedio de la fila.
    """
    promedio = sumar_fila(matriz_puntajes, fila) / len(matriz_puntajes[fila])    
    return round(promedio, 2)

def mostrar_participantes_superan_promedio(matriz_puntajes: list, array_nombres: list, promedio_a_superar: int|float) -> None:
    """Imprime los datos de todos los participantes que superen el promedio indicado.

    Args:
        matriz_puntajes (list): matriz que contiene los puntajes de todos los participantes.
        array_nombres (list): array que contiene los nombres de toods los participantes.
        promedio_a_superar (int | float): promedio que comparará con el promedio de todos los participantes para mostrarlos si lo supera.
    """
    bandera = False
    
    for fil in range(len(matriz_puntajes)):
        promedio = promediar_fila(matriz_puntajes, fil)
        if promedio > promedio_a_superar:
            bandera = True
            mostrar_participante(matriz_puntajes, array_nombres, fil)
            print("")
        else:
            continue
        
    if bandera == False:
        print(f"///Error. No existen participantes que hayan tenido un promedio mayor a {promedio_a_superar}.///")
        
def sumar_columna(matriz: list, columna: int) -> int:
    """Suma todos los valores de una columna perteneciente a una matriz.

    Args:
        matriz (list): matriz que usará para sumar una de sus columnas.
        columna (int): columna que sumará de una matriz.

    Returns:
        int: retorna la suma de todos los valores de la columna.
    """
    suma = 0
    for fila in range(len(matriz)):
        suma += matriz[fila][columna]
        
    return suma
        
def promediar_columna(matriz:list, columna: int)-> float:
    """Saca el promedio de la columna que se le indique perteneciente a la matriz que se le brinde.

    Args:
        matriz (list): matriz de la cual promediará una de sus columnas.
        columna (int): columna de la cual sacará un promedio de todos sus valores.

    Returns:
        float: retorna un float como promedio de los valores de la columna.
    """
    promedio = sumar_columna(matriz, columna) / len(matriz)        
    return promedio
    
def mostrar_jurado(matriz_puntajes: list, columna: int) -> None:
    """Imprime en consola los datos pertenecientes al jurado que pertenezca a la columna que se le indique. Los datos que imprime son el puntaje que el jurado le dió a cada participante y el promedio de sus puntajes.

    Args:
        matriz_puntajes (list): es la matriz de la que tomará los datos del jurado.
        columna (int): columna de la matriz a la que pertenece el jurado del cual se quieren mostrar los datos.
    """
    print(f"JURADO NUMERO {columna + 1}:")
    for fila in range(len(matriz_puntajes)):
        print(f"PUNTAJE AL PARTICIPANTE {fila + 1}: {matriz_puntajes[fila][columna]}")
    print(f"PROMEDIO JURADO {columna + 1}: {promediar_columna(matriz_puntajes, columna)}/10")

def mostrar_promedio_jurados(matriz_puntajes: list) -> None:
    """Imprime en consola los datos de todos los jurados del concurso.

    Args:
        matriz_puntajes (list): matriz a la cual pertenecen los jurados
    """
    for jurado in range(len(matriz_puntajes[0])):
        mostrar_jurado(matriz_puntajes, jurado)
        print("")
        
def encontrar_jurados_estrictos(matriz_puntajes: list) -> list:
    """Encuentra al jurado mas estricto del concurso y lo devuelve la columna a la que pertenece en una lista. Si hay mas de un jurado que coinciden en tener el promedio mas bajo de los puntajes que dieron devuelve a todos ellos.

    Args:
        matriz_puntajes (list): matriz a la cual pertenecen los jurados que se van a buscar

    Returns:
        list: retorna una lista con la o las columnas de los jurados mas estrictos del concurso
    """
    bandera = False
    cantidad_jurados = 1
    
    for jurado in range(len(matriz_puntajes[0])):
        promedio_jurado = promediar_columna(matriz_puntajes, jurado)
        if bandera == False:
            minimo = promedio_jurado
            jurados_estrictos = [jurado]
            bandera = True
        else:
            if promedio_jurado < minimo:
                minimo = promedio_jurado
                jurados_estrictos = [jurado]
            elif promedio_jurado == minimo:
                cantidad_jurados += 1
                array_auxiliar = crear_array(cantidad_jurados, None)
                for i in range(len(jurados_estrictos)):
                    array_auxiliar[i] = jurados_estrictos[i]
                array_auxiliar[-1] = jurado
                jurados_estrictos = array_auxiliar
            else:
                continue
            
    return jurados_estrictos

def mostrar_jurados_mas_estrictos(matriz_puntajes: list) -> None:
    """Imprime en consola los datos de el o los jurados mas estrictos del concurso

    Args:
        matriz_puntajes (list): matriz a la que pertenecen los jurados que se van a evaluar
    """
    jurados_estrictos = encontrar_jurados_estrictos(matriz_puntajes)
    
    for i in range(len(jurados_estrictos)):
        mostrar_jurado(matriz_puntajes, jurados_estrictos[i])
        print("")

def pasar_letra_a_minuscula(letra: str)-> str:
    """Convierte una letra mayúscula a minúscula y la devuelve. Si se le pasa un caracter que no es una letra mayuscula devuelve el mismo.

    Args:
        letra (str): Letra mayúscula que será cambiada a minúscula

    Returns:
        str: Reorna la letra en minúscula.
    """
    
    letra = str(letra)
    
    if ord(letra) > 64 and ord(letra) < 91:
        letra = chr(ord(letra) + 32)
    elif ord(letra) == 165:
        letra = chr(164)
    
    return letra
    
def pasar_cadena_a_minuscula(cadena: str) -> str:
    """Pasa todas las letras mayúsculas de una cadena a minúscula y la devuelve.

    Args:
        cadena (str): cadena que evaluará y de la cual pasará todas sus letras mayúsculas a minúscula

    Returns:
        str: retorna la cadena comletamente en minúscula.
    """
    cadena_aux = ""
    
    for i in range(len(cadena)):
        if es_mayuscula(cadena[i]):
            letra = pasar_letra_a_minuscula(cadena[i])
            cadena_aux += letra
        else:
            cadena_aux += cadena[i]
            
    return cadena_aux

def buscar_participante_exacto(matriz_puntajes: list, array_nombres: list) -> None:
    """Busca e imprime los nombres de los participantes que se le indique. Si el nombre de algún participante comienza con los caracteres ingresados también lo muestra.

    Args:
        matriz_puntajes (list): matriz en la cual buscará los datos del participante.
        array_nombres (list): lista en la que buscará el nombre del participante ingresado.
    """
    bandera = False
    
    nombre = input("Ingrese el nombre del participante que desea buscar: ")
    print(f"\nMOSTRANDO PARTICIPANTES LLAMADOS '{nombre}':")
    print("")
    
    for i in range(len(array_nombres)):
        nombre_a_comparar = pasar_cadena_a_minuscula(array_nombres[i])
        if nombre_a_comparar == nombre:
            bandera = True
            mostrar_participante(matriz_puntajes, array_nombres, i)
            print("")

    if bandera == False:
        print(f"///Error. No existen participantes llamados '{nombre}'.///")

def buscar_participantes(matriz_puntajes: list, array_nombres: list) -> None:
    """Busca e imprime los nombres de los participantes que se le indique. Si el nombre de algún participante comienza con los caracteres ingresados también lo muestra.

    Args:
        matriz_puntajes (list): matriz en la cual buscará los datos del participante.
        array_nombres (list): lista en la que buscará el nombre del participante ingresado.
    """
    bandera = False
    
    nombre = input("Ingrese el nombre del participante que desea buscar: ")
    print(f"\nMOSTRANDO PARTICIPANTES LLAMADOS '{nombre}' o que comienzan con los caracteres '{nombre}':")
    nombre_buscado = pasar_cadena_a_minuscula(nombre)
    print("")
    
    for i in range(len(array_nombres)):
        nombre_a_comparar = pasar_cadena_a_minuscula(array_nombres[i])
        if encontrar_subcadena(nombre_a_comparar, nombre_buscado):
            bandera = True
            mostrar_participante(matriz_puntajes, array_nombres, i)
            print("")

    if bandera == False:
        print(f"///Error. No existen participantes llamados '{nombre}'.///")

def encontrar_subcadena(cadena: str, subcadena: str) -> bool:
    """Busca una subcadena dentro de una cadena e indica si existe o no.

    Args:
        cadena (str): cadena dentro de la cual se buscará la subcadena. 
        subcadena (str): subcadena que se buscará dentro de la cadena.

    Returns:
        bool: Retorna True si se encontró la subcadena dentro de la cadena y False si no.
    """
    longitud_subcadena = len(subcadena)
    bandera = False
    
    if cadena[0:longitud_subcadena] == subcadena:
        bandera = True

    return bandera  

def pasar_cadena_a_minuscula(cadena: str) -> str:
    """Recibe una cadena y convierte todas sus letras mayúsculas a minúsculas

    Args:
        cadena (str): cadena de la cual se pasarán sus mayúsculas a minúsculas.

    Returns:
        str: Retorna la cadena con todas sus letras en minúsculas.
    """
    cadena_aux = ""
    
    for i in range(len(cadena)):
        if es_mayuscula(cadena[i]):
            letra = pasar_letra_a_minuscula(cadena[i])
            cadena_aux += letra
        else:
            cadena_aux += cadena[i]
            
    return cadena_aux
        
def intercambiar_valores(lista: list, valor_izq: any, valor_der: any) -> list:
    """intercambia dos valores de un array de posición.

    Args:
        lista (list): array que contiene los valores que se intercambiarán.
        valor_izq (any): indice del elemento que se cambairá por el valor_der.
        valor_der (any): indice del elemento que se cambairá por el valor_izq.

    Returns:
        list: Retorna la lista con los valores intercambiados
    """
    auxiliar = lista[valor_izq]
    lista[valor_izq] = lista[valor_der]
    lista[valor_der] = auxiliar
    
    return lista

def crear_lista_promedios(matriz_puntajes: list) -> list:
    """crea una lista con el promedio de cada fila a partir de una matriz.

    Args:
        matriz_puntajes (list): matriz que recibe para calular el promedio de cada fila.

    Returns:
        list: Retorna una lista con los promedios calculados de cada fila.
    """
    lista_promedios = crear_array(5, None)
    
    for i in range(len(matriz_puntajes)):
        promedio = promediar_fila(matriz_puntajes, i)
        lista_promedios[i] = promedio
        
    return lista_promedios

def mostrar_top_tres(matriz_puntajes: list, array_nombres: list) -> None:
    """imprime en consola los datos de los tres participantes con los promedios más altos.

    Args:
        matriz_puntajes (list): matriz que contiene los puntajes de todos los participantes.
        array_nombres (list): array que contiene los nombres de los participantes.
    """
    lista_promedios = crear_lista_promedios(matriz_puntajes)
        
    for izq in range(len(lista_promedios) - 1):
            for der in range(izq + 1, len(lista_promedios)):
                    if lista_promedios[izq] < lista_promedios[der]:
                        lista_promedios = intercambiar_valores(lista_promedios, izq, der)
                        matriz_puntajes = intercambiar_valores(matriz_puntajes, izq, der)
                        array_nombres = intercambiar_valores(array_nombres, izq, der)
                    else:
                        continue
    
    for i in range(3):
        mostrar_participante(matriz_puntajes, array_nombres, i)
        print("")
        
def mostrar_participantes_orden_alfabetico(array_nombres: list, matriz_puntajes: list) -> None:
    """imprime en consola los nombres de los participantes y su información por orden alfabético.

    Args:
        array_nombres (list): array que contiene los nombres de los participantes.
        matriz_puntajes (list): matriz que contiene los puntajes y de cada participante.
    """
    for izq in range(len(array_nombres) - 1):
            for der in range(izq + 1, len(array_nombres)):
                    if pasar_cadena_a_minuscula(array_nombres[izq]) > pasar_cadena_a_minuscula(array_nombres[der]):
                        matriz_puntajes = intercambiar_valores(matriz_puntajes, izq, der)
                        array_nombres = intercambiar_valores(array_nombres, izq, der)
                    else:
                        continue
                    
    mostrar_puntajes(matriz_puntajes, array_nombres)