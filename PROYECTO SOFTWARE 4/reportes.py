from registroUsuario import *
from gestionTrabajo import *
from camperRiesgo import *
import os
archivo = "usuario.json"
alerta= "Aun no esta codificado"
with open(archivo,"r") as a:
    camper= json.loads(a.read())
def camEnRuta():
    print(alerta)
def resultadosMod():
    print(alerta)
def reportes():
    global alerta
    bandera =True
    while bandera:
        print("MODULO DE REPORTES")
        opc = int(input("\t1. Campers inscritos\n"
                        "\t2. Campers aprobados\n"
                        "\t3. Trainers\n"
                        "\t4. Campers con bajo rendimiento\n"
                        "\t5. Campers y entrenador en ruta\n"
                        "\t6. Resultados de pruebas en cada modulo\n"
                        "\t7. Salir\n"))
        if opc ==1:
            for i in camper:
                if camper[i]["estado"]=="inscrito":
                    print(i, camper[i]["nombre"])
        elif opc==2:
            for i in camper:
                if camper[i]["estado"]=="aprobado":
                    print(i, camper[i]["nombre"])
        elif opc==3:
            for i in gestion["trainers"]:
                print(i, gestion["trainers"][i]["nombre"])
        elif opc==4:
            camperRiesgo()
        elif opc==5:
            camEnRuta()
        elif opc==6:
            resultadosMod()
        elif opc==7:
            bandera =False
            os.system('cls')
        else:
            print("Opcion no valida")
