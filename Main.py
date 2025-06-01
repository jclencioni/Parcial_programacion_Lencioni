from funciones import *
import os
"""AGREGAR ACENTOS A LA VALIDACION"""
os.system("cls")

#array_nombres = crear_array(5, None)
#matriz_puntajes = crear_matriz(5, 3, None)
#DATOS HARCODEADOS
array_nombres = ["Tomas Rebord", "Jorge", "Juan", "Guille", "Galia"]
matriz_puntajes = [
    [3, 7, 1],
    [5, 2, 6],
    [5, 9, 4],
    [4, 1, 3],
    [4, 2, 7]
]

while True:
    print("MENÚ:\n1.  CARGAR PARTICIPANTES\n2.  CARGAR PUNTUACIONES\n3.  MOSTRAR PUNTUACIONES\n4.  MOSTRAR PARTICIPANTES CON PROMEDIO MAYOR A 4\n5.  MOSTRAR PARTICIPANTES CON PROMEDIO MAYOR A 7\n6.  MOSTRAR PROMEDIO DE CADA JURADO\n7.  JURADO MAS ESTRICTO\n8.  BUSCAR PARTICIPANTE POR NOMBRE\n9.  TOP 3\n10. MOSTRAR PARTICIPANTES ORDENADOS ALFABETICAMENTE\n11. SALIR")
    
    opcion = input("\nSu opción: ")
    print("")
    
    # VALIDAR QUE SOLO SE PUEDA ELEGIR ENTRE EL 1 Y EL 11. MIRAR EL PROGRAMA DEL REGISTRO.
    # AGREGAR VOCALES CON ACENTOS
    # PARA LAS BUSQUEDAS DE NOMBRES O COMPARACIONES TRANSFORMAR MAYUSCULAS EN MINUSCULAS 
    if opcion == "1":
        #os.system("cls")
        print("\nINGRESANDO NOMBRES DE LOS PARTICIPANTES.")
        cargar_nombres_participantes(array_nombres)
        print("\nPARTICIPANTES INGRESADOS CORRECTAMENTE.")
    elif opcion == "2":
        print("\nCARGANDO PUNTUACIONES:\n")
        cargar_puntuaciones(matriz_puntajes)
        print("PUNTAJES CARGADOS CORRECTAMENTE")
    elif opcion == "3":
        print("MOSTRANDO PUNTUACIONES:\n")
        mostrar_puntajes(matriz_puntajes, array_nombres)
    elif opcion == "4":
        print("MOSTRANDO PARTICIPANTES QUE TIENEN PROMEDIO MAYOR A 4:\n")
        mostrar_participantes_superan_promedio(matriz_puntajes, array_nombres, 4)
    elif opcion == "5":
        print("MOSTRANDO PARTICIPANTES QUE TIENEN PROMEDIO MAYOR A 7:\n")
        mostrar_participantes_superan_promedio(matriz_puntajes, array_nombres, 7)
    elif opcion == "6":
        print("MOSTRANDO PROMEDIO DE CADA JURADO:\n")
        mostrar_promedio_jurados(matriz_puntajes)
    elif opcion == "7":
        print("MOSTRANDO JURADO/S MÁS ESTRICTO/S:")
        mostrar_jurados_mas_estrictos(matriz_puntajes)
    elif opcion == "8":
        pass
    elif opcion == "9":
        pass
    elif opcion == "10":
        pass
    elif opcion == "11":
        print("Saliendo...")
        break
    
    input("\nPresione enter para continuar.")
    os.system("cls")
    
    
    