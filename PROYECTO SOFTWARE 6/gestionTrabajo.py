import os
import json
archivo = "gestion.json"
with open(archivo, "r") as json_file:
    gestion = json.loads(json_file.read())
def trainers():
    for i in gestion["trainers"]:
        print("ID:",i,"-",gestion["trainers"][i]["name"])
    bandera=True
    while bandera:
        print("\t1. Agregar trainer\n"
            "\t2. Asignar rutas y horarios  al trainer\n"
            "\t3. Salir"
        )
        opc = int(input("\t"))
        if opc == 1:
            idTrainer= str(input("Ingrese el documento del trainer\n-"))
            gestion["trainers"][idTrainer] ={"name":str(input("Nombre completo del trainer\n-")),
                                            "horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                                            "rutas":[]
        }
            with open(archivo, "w+") as json_file:
                json_file.write(json.dumps(gestion,indent=4))
        elif opc==2:
            idTrainer2= str(input("Ingrese el documento del trainer\n-"))
            for idRuta in gestion["rutas"]:
                print("Id:",idRuta,"-",gestion["rutas"][idRuta]["nombre"])
            ruta=str(input("ingrese el Id de la ruta Ruta\n"))
            rutasTrainer =gestion["rutas"][ruta]["nombre"]
            gestion["trainers"][idTrainer2]["rutas"].append(rutasTrainer)
            print(gestion["trainers"][idTrainer2]["horarios"])
            print("\tIngrese el horario asignado a la ruta\n",
            "\t1. 6am\n"
            "\t2. 10am\n"
            "\t3. 2pm\n"
            "\t4. 6pm\n"
            "\t5. Salir")
            opc2=int(input())
            if opc2==1:
                gestion["trainers"][idTrainer2]["horarios"]["6am"]=rutasTrainer
            elif opc2==2:
                gestion["trainers"][idTrainer2]["horarios"]["10am"]=rutasTrainer
            elif opc2==3:
                gestion["trainers"][idTrainer2]["horarios"]["2pm"]=rutasTrainer
            elif opc2==4:
                gestion["trainers"][idTrainer2]["horarios"]["6pm"]=rutasTrainer
            elif opc2==5:
                bandera=False
            else:
                print("Opcion no valida")
        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print("OPcion no valida")
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(gestion,indent=4))
def rutas():
    bandera=True
    while bandera:
        print("Rutas de entreamiento")
        for ruta in gestion["rutas"]:
            print(gestion["rutas"][ruta]["nombre"])
        opc=int(input("\t1. Editar ruta existente\n"
                        "\t2. Crear nueva ruta\n"
                        "\t3. salir\n"))
        if opc==1:
            for ruta in gestion["rutas"]:
                print(gestion["rutas"][ruta]["nombre"])
            rutaExistente= input("Nombre de la ruta")
            gestion["rutas"][rutaExistente]["elegido"]= {"formal":rutaExistente,
                                        "SGDB":{"principal":str(input("Base de datos primaria\n")),
                                            "secundaria":str(input("Base de datos secundaria\n"))},
                                        "backend":str(input("Ingrese el Backend\n"))}
        elif opc==2:
            rutaNueva= input("Nombre de la ruta")
            gestion["rutas"][rutaNueva]= {"nombre":rutaNueva,
                                        "asignado":{"fundamentos":["introduccion a la algoritmia","PseInt","Python"],
                                                        "web":["HTML","CSS","Bootstrap"]},
                                            "elegido":{"formal":rutaNueva,
                                                        "SGDB":{"principal":str(input("Sistema de base de datos primaria o principal\n")),
                                                                "secundaria":str(input("Sistema de base de datos secundaria\n"))},
                                                        "backend":str(input("Backend\n"))
                                                        },
                                            "cupo":[]   
            }
        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print(gestion["rutas"])
            print("Opcion invalida")
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(gestion,indent=4))
def areas():
    bandera =True
    while bandera:
        print("\t1. Listar areas existentes\n"
            "\t2. Crear nueva area\n"
            "\t3. Salir"
        )
        opc = int(input("\t"))
        if opc == 1:
            for i in gestion["areas"]:
                print(i)
        elif opc==2:
            for i in gestion["areas"]:
                print(i)
            areaNueva= str(input("Nombre de la area\n"))
            gestion["areas"][areaNueva]={"6am":{"trainer":"","ruta":""},
                    "10am":{"trainer":"","ruta":""},
                    "2pm":{"trainer":"","ruta":""},
                    "6pm":{"trainer":"","ruta":""}}
        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print("Opcion invalida")
        with open(archivo, "w+") as json_file:
            json_file.write(json.dumps(gestion,indent=4))

def gestionTrabajo():
    bandera=True
    while bandera:
        print("GESTION DE TRABAJO")
        opc = int(input("\t1. Trainers"
                    "\n\t2. Areas de entrenamiento"
                    "\n\t3. Rutas de entrenamiento"
                    "\n\t4. Salir\n-"
                    ))
        if opc == 1:
            print("TRAINERS")
            trainers()
        elif opc==2:
            print("AREAS")
            areas()
        elif opc==3:
            print("RUTAS")
            rutas()
        elif opc==4:
            bandera =False
            os.system('clear')
        else:
            print("Opcion invalida")