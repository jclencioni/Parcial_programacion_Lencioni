def validar_entero(entero: int|str) -> bool:
    """solicita un valor y valida que todos los caracteres sean números enteros.

    Args:
        entero (int|str): valor que será evaludao 

    Returns:
        bool: retorna True si el valor es entero y False si no lo es.
    """
    entero = str(entero)
    bandera = True
    
    for i in range(len(entero)):
        if ord(entero[i]) > 47 and ord(entero[i]) < 58:
            continue
        else:
            bandera = False
            break
        
    return bandera
    
def validar_nota(nota: str) -> bool:
    if validar_entero(nota):
        if int(nota) >= 1 and int(nota) <= 10:
            return True
        else:
            return False
    else:
        return False

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
        cantidad_filas (int): _description_
        cantidad_columnas (int): _description_
        valor_inicial (any): _description_

    Returns:
        list: _description_
    """
    matriz = crear_array(cantidad_filas, None)
    fila = [valor_inicial] * cantidad_columnas
    
    for i in range(cantidad_filas):
        matriz[i] = fila
     
    return matriz

def validar_longitud_minima_cadena(cadena, longitud_minima) -> bool:
    """valida que la longitud de una cadena cumpla con la cantidad miniima de caracteres que se le indique

    Args:
        cadena (_type_): _description_
        longitud_minima (_type_): _description_

    Returns:
        _type_: _description_
    """
    bandera = True
    
    if len(cadena) < longitud_minima:
        bandera = False
    
    return bandera

def es_mayuscula(letra: str) -> bool:
    """Evalua si la letra es mayuscula o no

    Args:
        letra (_type_): _description_
    """
    letra = str(letra)
    
    if ord(letra) > 64 and ord(letra) < 91:
        return True
    elif ord(letra) == 165:
        return True
    else: 
        return False

def es_minuscula(letra) -> bool:
    """Evalua si la letra es minuscula o no

    Args:
        letra (_type_): _description_
    """
    letra = str(letra)
    
    if ord(letra) > 96 and ord(letra) < 123:
        return True
    elif ord(letra) == 164:
        return True
    else: 
        return False

def evaluar_palabra_alfabetica(palabra: str) -> bool:
    """evalua si todos los caracteres de una palabra, sin espacios, son letras de la a a la z.

    Args:
        palabra (_type_): _description_
    """
    palabra = str(palabra)
    bandera = True
    
    for i in range(len(palabra)): 
            if es_mayuscula(palabra[i]) or es_minuscula(palabra[i]):
                continue
            else:
                bandera = False
                break
    
    return bandera
    
def validar_nombre(nombre: str) -> bool:
    """solicita un valor y valida que todos los caracteres sean números enteros.

    Args:
        entero (int|str): valor que será evaludao 

    Returns:
        bool: retorna True si el valor es entero y False si no lo es.
    """
    bandera = True
    nombre = str(nombre)
    
    if len(nombre) == 3: 
        bandera = evaluar_palabra_alfabetica(nombre)
    else:
        if validar_longitud_minima_cadena(nombre, 3) == True:
            for i in range(len(nombre)):
                if es_minuscula(nombre[i]) or es_mayuscula(nombre[i]) or ord(nombre[i]) == 32:
                    continue
                else:
                    bandera = False
                    break
        else:
            bandera = False
            
    return bandera

def cargar_nombres_participantes(array_nombres:list) -> list:
    """Carga los nombres ingresados en el array que se le brinde.

    Args:
        array_nombres (list): _description_
    """
    for i in range(len(array_nombres)):
        nombre = input(f"Ingrese nombre del participante {i+1}: ")
        while validar_nombre(nombre) == False:
            nombre = input("Por favor, ingrese un nombre válido: ")
        array_nombres[i] = nombre

    return array_nombres

def cargar_puntuaciones(matriz_puntos:list) -> list:
    for fil in range(len(matriz_puntos)):
        for col in range(len(matriz_puntos[0])):
            puntaje = input(f"Ingrese el puntaje del jurado {col + 1} para el participante {fil + 1}: ")
            while validar_nota(puntaje) == False:
                puntaje = input(f"La nota debe ser un número del 1 al 10. Por favor, reingrese la nota del jurado {col +1} para el participante {fil + 1}: ")
            matriz_puntos[fil][col] = int(puntaje)
    
    return matriz_puntos

def mostrar_participante(matriz_puntajes:list, array_nombres: list, fila: int) -> None:
    
    print(f"NOMBRE PARTICIPANTE: {array_nombres[fila]}")
    
    for col in range(len(matriz_puntajes[fila])):
        print(f"PUNTAJE DEL JURADO {col + 1}: {matriz_puntajes[fila][col]}")
        
    print(f"PUNTAJE PROMEDIO: {promediar_fila(matriz_puntajes, fila)}/10")

def mostrar_puntajes(matriz_puntajes: list, array_nombres: list) -> None:
    
    for fil in range(len(matriz_puntajes)):
        mostrar_participante(matriz_puntajes, array_nombres, fil)  
        print("")

def sumar_fila(matriz: list, fila: int) -> int:
    suma = 0
    
    for i in range(len(matriz[fila])):
        suma += matriz[fila][i]
    
    return suma

def promediar_fila(matriz_puntajes: list, fila: int) -> float:
    promedio = sumar_fila(matriz_puntajes, fila) / len(matriz_puntajes[fila])    
    return round(promedio, 2)

def mostrar_participantes_superan_promedio(matriz_puntajes: list, array_nombres: list, promedio_a_superar: int|float) -> None:
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
    suma = 0
    for fila in range(len(matriz)):
        suma += matriz[fila][columna]
        
    return suma
        
def promediar_columna(matriz:list, columna: int)-> float:
    promedio = sumar_columna(matriz, columna) / len(matriz)        
    return promedio
    
def mostrar_jurado(matriz_puntajes: list, columna: int) -> None:
    print(f"JURADO NUMERO {columna + 1}:")
    for fila in range(len(matriz_puntajes)):
        print(f"PUNTAJE PARTICIPANTE {fila + 1}: {matriz_puntajes[fila][columna]}")
    print(f"PROMEDIO JURADO {columna + 1}: {promediar_columna(matriz_puntajes, columna)}/10")

def mostrar_promedio_jurados(matriz_puntajes: list) -> None:
    for jurado in range(len(matriz_puntajes[0])):
        mostrar_jurado(matriz_puntajes, jurado)
        print("")
        
def encontrar_jurados_estrictos(matriz_puntajes: list) -> list:
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
    jurados_estrictos = encontrar_jurados_estrictos(matriz_puntajes)
    
    for i in range(len(jurados_estrictos)):
        mostrar_jurado(matriz_puntajes, jurados_estrictos[i])
        print("")

def pasar_letra_a_minuscula(letra):
    letra = str(letra)
    
    if ord(letra) > 64 and ord(letra) < 91:
        letra = chr(ord(letra) + 32)
    elif ord(letra) == 165:
        letra = chr(164)
    
    return letra
    
def pasar_cadena_a_minuscula(cadena: str) -> str:
    cadena_aux = ""
    
    for i in range(len(cadena)):
        if es_mayuscula(cadena[i]):
            letra = pasar_letra_a_minuscula(cadena[i])
            cadena_aux += letra
        else:
            cadena_aux += cadena[i]
            
    return cadena_aux

def buscar_participantes(matriz_puntajes: list, array_nombres: list) -> None:
    bandera = False
    
    nombre = input("Ingrese el nombre del participante que desea buscar: ")
    print(f"\nMOSTRANDO PARTICIPANTES LLAMADOS {nombre}:")
    nombre_buscado = pasar_cadena_a_minuscula(nombre)
    print("")
    
    for i in range(len(array_nombres)):
        nombre_a_comparar = pasar_cadena_a_minuscula(array_nombres[i])
        if encontrar_subcadena(nombre_a_comparar, nombre_buscado):
            bandera = True
            mostrar_participante(matriz_puntajes, array_nombres, i)
            print("")

    if bandera == False:
        print(f"///Error. No existen participantes llamados {nombre}.///")
    
def encontrar_subcadena(cadena: str, subcadena: str) -> bool:
    longitud_subcadena = len(subcadena)
    bandera = False
    
    for i in range(len(cadena) - longitud_subcadena + 1):
        if cadena[i:longitud_subcadena] == subcadena:
            bandera = True
            break
        else:
            longitud_subcadena += 1
            continue

    return bandera        
    
def intercambiar_valores(lista: list, valor_izq: int, valor_der: int) -> list:
    auxiliar = lista[valor_izq]
    lista[valor_izq] = lista[valor_der]
    lista[valor_der] = auxiliar
    
    return lista

def crear_lista_promedios(matriz_puntajes: list) -> list:
    lista_promedios = crear_array(5, None)
    
    for i in range(len(matriz_puntajes)):
        promedio = promediar_fila(matriz_puntajes, i)
        lista_promedios[i] = promedio
        
    return lista_promedios

def mostrar_top_tres(matriz_puntajes: list, array_nombres: list) -> None:
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

    for izq in range(len(array_nombres) - 1):
            for der in range(izq + 1, len(array_nombres)):
                    if pasar_cadena_a_minuscula(array_nombres[izq]) > pasar_cadena_a_minuscula(array_nombres[der]):
                        matriz_puntajes = intercambiar_valores(matriz_puntajes, izq, der)
                        array_nombres = intercambiar_valores(array_nombres, izq, der)
                    else:
                        continue
                    
    mostrar_puntajes(matriz_puntajes, array_nombres)