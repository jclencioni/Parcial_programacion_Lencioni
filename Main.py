from funciones import *
import os

os.system("cls")

array_nombres = crear_array(5, None)
matriz_puntajes = crear_matriz(5, 3, None)

nombres_cargados = False
puntajes_cargados = False

while True:
    print("MENÚ:\n1.  CARGAR PARTICIPANTES\n2.  CARGAR PUNTUACIONES\n3.  MOSTRAR PUNTUACIONES\n4.  MOSTRAR PARTICIPANTES CON PROMEDIO MAYOR A 4\n5.  MOSTRAR PARTICIPANTES CON PROMEDIO MAYOR A 7\n6.  MOSTRAR PROMEDIO DE CADA JURADO\n7.  JURADO MAS ESTRICTO\n8.  BUSCAR PARTICIPANTE POR NOMBRE\n9.  TOP 3\n10. MOSTRAR PARTICIPANTES ORDENADOS ALFABETICAMENTE\n11. SALIR")
    
    opcion = pedir_entero("\nSu opción: ", "Por favor, ingrese un numero del 1 al 11. Su opción: ", 1, 11)
    print("")
    
    while nombres_cargados == False and opcion != 1 and opcion != 11:
        opcion = pedir_entero("No hay participantes ingresados, su opción: ", "Por favor, ingrese un numero del 1 al 11. Su opción: ", 1, 11)
    
    while puntajes_cargados == False and opcion != 1 and opcion != 2 and opcion != 11:
        opcion = pedir_entero("No hay puntajes cargados, su opción: ", "Por favor, ingrese un numero del 1 al 11. Su opción: ", 1, 11)
    
    if opcion == 1:
        print("\nINGRESANDO NOMBRES DE LOS PARTICIPANTES.")
        cargar_nombres_participantes(array_nombres)
        print("\nPARTICIPANTES INGRESADOS CORRECTAMENTE.")
        nombres_cargados = True
    elif opcion == 2:
        print("\nCARGANDO PUNTUACIONES:\n")
        cargar_puntuaciones(matriz_puntajes, array_nombres)
        print("PUNTAJES CARGADOS CORRECTAMENTE")
        puntajes_cargados = True
    elif opcion == 3:
        print("MOSTRANDO PUNTUACIONES:\n")
        mostrar_puntajes(matriz_puntajes, array_nombres)
    elif opcion == 4:
        print("MOSTRANDO PARTICIPANTES QUE TIENEN PROMEDIO MAYOR A 4:\n")
        mostrar_participantes_superan_promedio(matriz_puntajes, array_nombres, 4)
    elif opcion == 5:
        print("MOSTRANDO PARTICIPANTES QUE TIENEN PROMEDIO MAYOR A 7:\n")
        mostrar_participantes_superan_promedio(matriz_puntajes, array_nombres, 7)
    elif opcion == 6:
        print("MOSTRANDO PROMEDIO DE CADA JURADO:\n")
        mostrar_promedio_jurados(matriz_puntajes)
    elif opcion == 7:
        print("MOSTRANDO JURADO/S MÁS ESTRICTO/S:")
        print("")
        mostrar_jurados_mas_estrictos(matriz_puntajes)
    elif opcion == 8:
        busqueda = pedir_entero("Ingrese:\n1. Para realizar una búsqueda exacta.\n2. Para buscar por coinidencia de los primeros caracteres: ", "Seleccione 1 o 2: ", 1, 2)
        if busqueda == 1:
            print("BUSCANDO PARTICIPANTES:")
            buscar_participante_exacto(matriz_puntajes, array_nombres)
        elif busqueda == 2:
            print("BUSCANDO PARTICIPANTES:")
            buscar_participantes(matriz_puntajes, array_nombres)
    elif opcion == 9:
        print("MOSTRANDO TOP 3:")
        mostrar_top_tres(matriz_puntajes, array_nombres)
    elif opcion == 10:
        mostrar_participantes_orden_alfabetico(array_nombres, matriz_puntajes)
    elif opcion == 11:
        print("Saliendo...")
        break
    
    input("\nPresione enter para continuar.")
    os.system("cls")
    
