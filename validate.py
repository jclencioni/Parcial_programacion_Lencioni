def validar_maximo_minimo(numero: str, maximo: int, minimo: int) -> bool:
    """valida que un string contenga solo numeros enteros y a la vez sea igual o menor al máximo y mayor o igual al minimo.

    Args:
        numero (str): cadena que será evaluada
        maximo (int): maximo valor posible inclusive.
        minimo (int): minimo valor posible inclusive.

    Returns:
        bool: retorna True si cumple con los parámetros y False si no.
    """
    if validar_entero(numero):
        if int(numero) >= minimo and int(numero) <= maximo:
            return True
        else:
            return False
    else:
        return False

def validar_entero(entero: int|str) -> bool:
    """solicita un valor y valida que todos los caracteres sean números enteros mas allá del tipo de dato.

    Args:
        entero (int|str): valor que será evaludao 

    Returns:
        bool: retorna True si el valor es entero y False si no lo es.
    """
    entero = str(entero)
    bandera = True
    
    if len(entero) == 0:
        bandera = False
    
    for i in range(len(entero)):
        if ord(entero[i]) > 47 and ord(entero[i]) < 58:
            continue
        else:
            bandera = False
            break
        
    return bandera

def validar_nombre(nombre: str) -> bool:
    """Evalúa que el nombre que solicita commo parámetro tenga al menos 3 caracteres alfabéticos.

    Args:
        nombre (str): string que será evaludao 

    Returns:
        bool: retorna True si el nombre es válido y False si no lo es.
    """
    bandera = True
    
    if len(nombre) == 3: 
        bandera = validar_palabra_alfabetica(nombre)
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

def validar_longitud_minima_cadena(cadena: str, longitud_minima: int) -> bool:
    """valida que la longitud de una cadena cumpla con la cantidad miniima de caracteres que se le indique

    Args:
        cadena (str): cadena que será evaluada.
        longitud_minima (int): cantidad minima de caracteres que debe tener la cadena.

    Returns:
        bool: retorna True si la cadena cumple con la longitud minima y False si no.
    """
    bandera = True
    
    if len(cadena) < longitud_minima:
        bandera = False
    
    return bandera

def es_mayuscula(letra: str) -> bool:
    """Evalua si el caracter es una letra es mayuscula o no.

    Args:
        letra (str): caracter a evaluar.
    Returns:
        bool: retorna true si el caracter es una letra mayuscula y False si no.
    """
    letra = str(letra)
    
    if ord(letra) > 64 and ord(letra) < 91:
        return True
    elif ord(letra) == 165:
        return True
    else: 
        return False

def es_minuscula(letra: str) -> bool:
    """Evalua si el caracter es una letra es minuscula o no.

    Args:
        letra (str): caracter a evaluar.
    Returns:
        bool: retorna true si el caracter es una letra minuscula y False si no.
    """
    letra = str(letra)
    
    if ord(letra) > 96 and ord(letra) < 123:
        return True
    elif ord(letra) == 164:
        return True
    else: 
        return False
    
def validar_palabra_alfabetica(palabra: str) -> bool:
    """Evalua si todos los caracteres de una palabra, sin espacios, son letras de la a a la z.

    Args:
        palabra (str): plabra que será evaluada
    Returns:
        bool: retorna True si todos los caracteres de la palabra son letras del abecedario y False si no lo son o si hay espacios.
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