import os
gestion ={"trainers":{"1":{"name":"Miguel",
                        "Horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                        "rutas":[]},
                    "2":{"name":"Johlver",
                        "Horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                        "rutas":[]},
                    "3":{"name":"Juan",
                        "Horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                        "rutas":[]}
                    },
          "rutas":{"nodejs":{"nombre":"NodeJs",
                            "asignado":{"fundamentos":["introduccion a la algoritmia","PseInt","Python"],
                                         "web":["HTML","CSS","Bootstrap"]},
                            "elegido":{"formal":"nodejs",
                                        "SGDB":{"principal":"",
                                               "secundaria":""},
                                        "backend":""},
                            "cupo":[]    
                            },
                   "java":{"nombre":"Java",
                            "asignado":{"fundamentos":["introduccion a la algoritmia","PseInt","Python"],
                                         "web":["HTML","CSS","Bootstrap"]},
                            "elegido":{"formal":"java",
                                        "SGDB":{"principal":"",
                                               "secundaria":""},
                                        "backend":""},
                            "cupo":[]    
                            },
                   "netcore":{"nombre":"NetCore",
                            "asignado":{"fundamentos":["introduccion a la algoritmia","PseInt","Python"],
                                         "web":["HTML","CSS","Bootstrap"]},
                            "elegido":{"formal":"netcore",
                                        "SGDB":{"principal":"",
                                               "secundaria":""},
                                        "backend":""},
                            "cupo":[]    
                            }
                    },
          "areas":{"sputnik":{"6am":{"trainer":"","ruta":""},
                    "10am":{"trainer":"","ruta":""},
                    "2pm":{"trainer":"","ruta":""},
                    "6pm":{"trainer":"","ruta":""}},
                   "apolo":{"6am":{"trainer":"","ruta":""},
                   "10am":{"trainer":"","ruta":""},
                   "2pm":{"trainer":"","ruta":""},
                   "6pm":{"trainer":"","ruta":""}},
                   "artemis":{"6am":{"trainer":"","ruta":""},
                   "10am":{"trainer":"","ruta":""},
                   "2pm":{"trainer":"","ruta":""},
                   "6pm":{"trainer":"","ruta":""}}}
          }
def trainers():
    for i in gestion["trainers"]:
        print("ID:",i,"-",gestion["trainers"][i]["name"])
    bandera=True
    while bandera:
        print("\t1. Agregar trainer\n"
            "\t2. Asignar rutas y horarios al trainer\n"
            "\t3. Salir"
        )
        opc = int(input("\t"))
        if opc == 1:
            idTrainer= str(input("Ingrese el documento del trainer\n-"))
            gestion["trainers"][idTrainer] ={"name":str(input("Nombre completo del trainer\n-")),
                                            "horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                                            "rutas":[]
        }
        elif opc==2:
            for ruta in gestion["rutas"]:
                print(gestion["rutas"][ruta]["nombre"])
            idTrainer2= str(input("Ingrese el documento del trainer\n-"))
            rutasTrainer=str(input("Ruta\n"))
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
                rutasTrainer=gestion["trainers"][idTrainer2]["horarios"]["6am"]
            elif opc2==2:
                rutasTrainer=gestion["trainers"][idTrainer2]["horarios"]["10am"]
            elif opc2==3:
                rutasTrainer=gestion["trainers"][idTrainer2]["horarios"]["2pm"]
            elif opc2==4:
                rutasTrainer=gestion["trainers"][idTrainer2]["horarios"]["6pm"]
            elif opc2==5:
                bandera=False
            else:
                print("Opcion no valida")

        elif opc==3:
            bandera=False
            os.system('clear')
        else:
            print("OPcion no valida")
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

def gestionTrabajo():
    bandera=True
    while bandera:
        print("GESTION DE TRABAJO")
        opc = int(input("\t1. Trainers"
                    "\n\t2. Rutas de entrenamiento"
                    "\n\t3. Crear area de entrenamiento"
                    "\n\t4. Salir\n-"
                    ))
        if opc == 1:
            trainers()
        elif opc==2:
            rutas()
        elif opc==3:
            areas()
        elif opc==4:
            bandera =False
            os.system('clear')
        else:
            print("Opcion invalida")