import json
import os
alerta ="Aun no codificado"
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
          "areas":{"sputnik":{"6am":"","10am":"","2pm":"","6pm":""},
                   "apolo":{"6am":"","10am":"","2pm":"","6pm":""},
                   "artemis":{"6am":"","10am":"","2pm":"","6pm":""}}
          }
def trainers():
    for id in gestion["trainers"]:
        print("ID:",id,"-",gestion["trainers"][id]["name"])
    bandera=True
    while bandera:
        print("1. Agregar trainer\n"
            "2. Asignar rutas y horarios\n"
            "3. Salir"
        )
        opc = int(input())
        if opc == 1:
            idTrainer= str(input("Ingrese el documento del trainer\n-"))
            gestion["trainers"][idTrainer] ={"Nombre":str(input("Nombre completo del trainer\n-")),
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
            
        elif opc==3:
            bandera=False
        else:
            print("OPcion no valida")
def rutas():
    bandera=True
    while bandera:
        for ruta in gestion["rutas"]:
            print(gestion["rutas"][ruta]["nombre"])
            opc=int(input("\t1. Editar ruta existente\n"
                        "\t2. Crear nueva ruta\n"
                        "\t3. salir"))
            if opc==1:
                for ruta in gestion["rutas"]:
                    print(gestion["rutas"][ruta]["nombre"])
                rutaExistente= input("Nombre de la ruta")
                gestion["rutas"][rutaExistente]["elegido"]= {"formal":rutaExistente,
                                        "SGDB":{"principal":str(input("Sistema de base de datos primaria o principal\n")),
                                               "secundaria":str(input("Sistema de base de datos secundaria\n"))},
                                        "backend":str(input("Backend\n"))}
            elif opc==2:
                rutaNueva= input("Nombre de la ruta")
                gestion["rutas"][rutaNueva]={"nombre":rutaNueva,
                                            "asignado":{"fundamentos":["introduccion a la algoritmia","PseInt","Python"],
                                                        "web":["HTML","CSS","Bootstrap"]},
                                            "elegido":{"formal":rutaNueva,
                                                        "SGDB":{"principal":str(input("Ingresé el sistema de base de datos principal\n")),
                                                                "secundaria":str(input("Ingrese el sistema de base de datos secundaria\n"))},
                                                        "Ingrese el backend":str(input("Backend\n"))
                                                        },
                                            "cupo":[]   
                                             }
                                    }
            elif opc==3:
                bandera=False
            else:
                print("Opcion invalida")
def areas():
   print(alerta)
def gestionTrabajo():
    bandera=True
    while bandera:
        opc = int(input("1. Trainers"
                    "\n2. Rutas de entrenamiento"
                    "\n3. areas de entrenamiento"
                    "\n4. Salir\n-"
                    ))
        if opc == 1:
            trainers()
        elif opc==2:
           rutas()
        elif opc==3:
            print()
        elif opc==4:
           bandera =False
           os.system('cls')
        else:
           print("Opcion invalida")