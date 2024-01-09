import json
# archivo="modulo.json"
gestion ={"trainers":{},
          "rutas":{},
          "areas":{}}
# with open(archivo, "r") as a:
#         gestion = json.loads(a.read())
def trainers():
  for id in gestion["trainers"]:
    print(gestion["trainers"][id]["nombre"])
  print("1. Agregar trainer\n"
        "2. Asignar rutas y horarios"
       )
  opc = int(input())
  if opc == 1:
    idTrainer= input("Ingrese el documento del trainer\n-")
    gestion["trainers"][idTrainer] ={"Nombre":str(input("Nombre completo del trainer\n-")),
                                    "horarios":{"6am":"","10am":"","2pm":"","6pm":""},
                                    "Rutas":[]
    }
def rutas():
    for ruta in gestion["rutas"]:
        print(gestion["rutas"]["ruta"]["nombre"])
    print()
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
        else:
           print("Opcion invalida")