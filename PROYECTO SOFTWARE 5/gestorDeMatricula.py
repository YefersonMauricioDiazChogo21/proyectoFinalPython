from registroUsuario import *
from gestionTrabajo import *

alerta = "Aun no esta codificado"
def gestionMatricula():
    print("GESTION DE MATRICULA")
    bandera=True
    while bandera:
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
                opc= int(input("\t1. Asignar ruta de entrenamiento\n"
                            "\t2. Asignar fecha de inicio\n"
                            "\t3. Asignar fecha de finalizacion\n"
                            "\t4. Asignar trainer\n"
                            "\t5. Asignar salon\n"
                            "\t6. Salir\n\t"))
                if opc==1:
                    cont=0
                    for i in gestion["rutas"]:
                        print(i)
                    rutaCamper=   str(input("Escribe la ruta asignada"))
                    for i in gestion["rutas"][rutaCamper]["cupo"]:
                        cont+=1
                    if cont==33:
                        print("Ruta con cupo lleno")
                    else:
                        camper[id]["ruta"]= rutaCamper
                        gestion["rutas"][rutaCamper]["cupo"].append(id)
                elif opc==2:
                    camper[id]["fecha"]["inicio"]= str(input("Escribe la fecha de inicio"))
                elif opc==3:
                    camper[id]["fecha"]["final"]= str(input("Escribe la fecha de finalizacion"))
                elif opc==4:
                    camper[id]["trainer"]= str(input("Escribe el trainer asignado"))
                elif opc==5:
                    for i in gestion["areas"]:
                        print(i)
                    camper[id]["salon"]= str(input("Escribe el salon asignado"))
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