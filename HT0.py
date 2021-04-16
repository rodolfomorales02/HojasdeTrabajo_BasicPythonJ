"""
Hoja de Trabajo 0
Josué Rodolfo Morales Castillo
Ejercicio:1
"""
import math
try:
    peso=float(input("¿Cuál es su peso en (kg)? \n"))
    altura=float(input("¿Cuál es su altura en (metros)? \n"))
    indice_masa_corporal=round((peso)/(altura**2),2)
    print("Tu Índice de Masa Corporal es:",indice_masa_corporal,("(kg/m2)"))
except:
    print("Debe ingresar un número.")