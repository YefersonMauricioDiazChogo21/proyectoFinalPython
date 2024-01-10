import json
import os
alerta="Aun no codificado"
jsonCamper= "usuario.json"
with open(jsonCamper,"r") as a:
    camper= json.loads(a.read())
def pruebaModulo():
    for i in camper:
        id=i
        if camper[i]["estado"]== "aprobado":
            print(id,camper[i]["nombre"],camper[i]["apellidos"])
    
    print(alerta)
def registroPruebas():
    bandera =True
    while bandera:
        print("GESTION DE PRUEBAS")
        print("\t1. Ingresar resultados de prueba inicial\n"
            "\t2. Ingresar resultados de prueba por modulos\n"
            "\t3. salir")
        opc =int(input("-"))
        if opc==1:
            print("REGISTRO, PRUEBA INICIAL")
            for i in camper:
                print(i,camper[i]["nombre"])
            id = str(input("\tIngrese el documento\n\t"))
            print(camper[id]["nombre"])
            teorica=int(input("Ingrese puntaje de prueba teorica\n-"))
            practica=int(input("Ingrese puntaje de prueba practica\n-"))
            camper[id]["pruebas"]["iniciales"]["teorica"] =str(teorica)
            camper[id]["pruebas"]["iniciales"]["practica"] =str(practica)
            promedio=(teorica+practica)/2
            if promedio>=60:
                camper[id]["estado"] = "aprobado"
            else:
                camper[id]["estado"] = "no admitido"
            with open(archivo, "w") as f:
                json.dump(camper, f, indent=4)
        elif opc==2:
            pruebaModulo()
        elif opc==3:
            bandera =False
            os.system('clear')
        else:
            print("Respuesta invalida")
