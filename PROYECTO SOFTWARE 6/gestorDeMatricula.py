from registroUsuario import *
from gestionTrabajo import *
archivo = "pruebas.json"
with open(archivo, "r") as json_file:
    pruebas = json.loads(json_file.read())
archivo2 = "usuario.json"
with open(archivo2, "r") as a: 
        camper = json.loads(a.read())
alerta = "Aun no esta codificado"
def gestionMatricula():
    print("GESTION DE MATRICULA")
    bandera=True
    while bandera:
        for i in camper:
            if camper[i]["estado"]=="aprobado":
                print("Id:",i,"-",camper[i]["nombre"])
        id= input("Ingrese el documento del camper a gestionar\n")
        bandera2=True
        while bandera2:
            siEsta=False
            noEsta=False
            noAprobado=False
            for i in camper:
                if i ==id and camper[i]["estado"]=="aprobado":
                    siEsta =True
                else:
                    bandera2=False
                # elif i ==id and camper[i]["estado"]=="inscrito":
                #     noAprobado= True
                #     noA="El camper no ha sido aprobado"
                # else:
                #     noEsta=True
                #     no="No hay registro del documento"
            # if noEsta==True:
            #     print(no)
            #     bandera2=False
            # elif noAprobado==True:
            #     print(noA)
            #     bandera2=False
                
                
            while siEsta:
                global alerta
                print(id,"-",camper[id]["nombre"],camper[id]["apellidos"])
                opc= int(input("\t1. Asignar ruta de entrenamiento\n"
                            "\t2. Asignar fecha de inicio\n"
                            "\t3. Asignar fecha de finalizacion\n"
                            "\t4. Asignar trainer\n"
                            "\t5. Asignar salon\n"
                            "\t6. Salir\n\t"))
                if opc==1:
                    cont=0
                    for i in gestion["rutas"]:
                        print("Id:",i,"-",gestion["rutas"][i]["nombre"])
                    rutaCamper=   str(input("Escribe el id de la ruta asignada\n-"))
                    for i in gestion["rutas"][rutaCamper]["cupo"]:
                        cont+=1
                    if cont==33:
                        print("Ruta con cupo lleno")
                    else:
                        camper[id]["ruta"]= rutaCamper
                        gestion["rutas"][rutaCamper]["cupo"].append(id)
                        pruebas[id]={"nombre": gestion["rutas"][rutaCamper]["nombre"],
                        "asignado": {
                            "fundamentos": {
                            "introduccion a la algoritmia": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                            },
                                "PseInt": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                                },
                                "Python": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                                }
                            },
                            "web": {
                                "HTML": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                                },
                                "CSS": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                                },
                                "Bootstrap": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                                }
                            },
                            "elegido": {
                                "formal": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""
                                },
                                "SGDB": {
                                "principal": {
                                    "practica": "",
                                    "teorica": "",
                                    "quices": "",
                                    "trabajos": "",
                                    "notaFinal":""
                                },
                                "secundaria": {
                                    "practica": "",
                                    "teorica": "",
                                    "quices": "",
                                    "trabajos": "",
                                    "notaFinal":""
                                    }
                                    },
                                "backend": {
                                "practica": "",
                                "teorica": "",
                                "quices": "",
                                "trabajos": "",
                                "notaFinal":""}
                                }
                                }}
                    with open(archivo, "w+") as json_file:
                        json_file.write(json.dumps(pruebas,indent=4))
                    with open(archivo2, "w+") as json_file:
                        json_file.write(json.dumps(camper,indent=4))
                elif opc==2:
                    fecha=str(input("Escribe la fecha de inicio\n"))
                    camper[id]["fecha"]["inicio"]=fecha
                    with open(archivo2, "w+") as json_file:
                        json_file.write(json.dumps(camper,indent=4))
                elif opc==3:
                    fecha=str(input("Escribe la fecha de finalizacion\n"))
                    camper[id]["fecha"]["final"]=fecha
                    with open(archivo2, "w+") as json_file:
                        json_file.write(json.dumps(camper,indent=4))
                elif opc==4:
                    for i in gestion["trainers"]:
                        print("Id:",i,gestion["trainers"][i]["name"])
                    idTrainer= str(input("Escribe el id del trainer asignado\n"))
                    camper[id]["trainer"]=gestion["trainers"][idTrainer]["name"]
                    with open(archivo2, "w+") as json_file:
                        json_file.write(json.dumps(camper,indent=4))
                elif opc==5:
                    for i in gestion["areas"]:
                        print(i)
                    camper[id]["salon"]= str(input("Escribe el salon asignado\n"))
                    with open(archivo2, "w+") as json_file:
                        json_file.write(json.dumps(camper,indent=4))
                elif opc==6:
                    opc2=int(input("Desea realizar la asignacion de otro camper?\n"
                                  "\t1. Si\n"
                                  "\t2. No\n"))
                    if opc2==1:
                        siEsta=False
                        os.system('cls')
                    else:
                        siEsta=False
                        bandera =False
                        os.system('cls')
                else:
                    print("Opcion no valida")