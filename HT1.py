"""
Hoja de Trabajo 1
Josué Rodolfo Morales Castillo
Ejercicio:1
"""
try:
    asterisco=""
    tree=int(input("Escriba un número entero: \n"))
    for j in range(tree):
        asterisco+="*"
        print(asterisco)
            
except:
    print("Ingrese un número entero.")
"""
Hoja de Trabajo 1
Josué Rodolfo Morales Castillo
Ejercicio:2
"""
try:
    cont=0
    primo=int(input("Escriba un número entero: \n"))
    for i in range(1,primo+1):
        if((primo%i)==0):
            cont+=1
    if(cont==2):
        print("El número ingresado es primo.")
    else:
        print("El número ingresado no es primo.")
            
except:
    print("Ingrese un número entero.")

