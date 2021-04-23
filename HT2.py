"""
Hoja de Trabajo 2
Josué Rodolfo Morales Castillo
Ejercicio:1
"""
try:
    print("<------------- Ejercicio 1 ---------------->")
    password=input("Ingrese un password: \n").upper().strip()
    print("********************************************")
    verificar=input("Ingrese de nuevo el password: \n").upper().strip()
    print("********************************************")
    if(password==verificar):
        print("El segundo password introducido coincide\ncon el primer password.")
    else:
        print("El segundo password introducido no coincide\ncon el primer password.")
    print("<------------------------------------------>")   
    print("")
    print("<------------- Ejercicio 2 ---------------->") 
    nombre=input("Ingrese su nombre (No use tildes):\n").upper().strip()
    print("********************************************")
    sexo=input("Ingrese su género; M->Masculino; F->Femenino:\n").upper().strip()
    print("********************************************")
    list_name=[]
    for i in nombre:
        list_name.append(i)
    if((65<=ord(list_name[0])<=76 and sexo=="F") or (79<=ord(list_name[0])<=90 and sexo=="M")):
        print("Pertenece al grupo A.")
    else:
        print("Pertenece al grupo B.")    
    print("<------------------------------------------>")   
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Introduzca lo que se le solicita por favor.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")