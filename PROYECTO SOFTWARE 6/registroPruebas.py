import json
import os
alerta="Aun no codificado"
jsonCamper= "usuario.json"
with open(jsonCamper,"r") as a:
    camper= json.loads(a.read())
archivo = "pruebas.json"
with open(archivo, "r") as json_file:
    pruebas = json.loads(json_file.read())
def pruebaModulo():
    bandera=True
    while bandera:
        for i in camper:
            if camper[i]["estado"]== "aprobado":
                print("Id:",i,"-",camper[i]["nombre"],camper[i]["apellidos"])
        selec=int(input("Ingrese el id del camper"))
        
        print("Elija el modulo")
        opc=int(input("\t1. Fundamentos de programacion\n"
                    "\t2. Programacion Web\n"
                    "\t3. Programacion Formal\n"
                    "\t4. Base de datos\n"
                    "\t5. Backend\n"
                    "\t6. Salir\n"))
        if opc==1:
            bandera2=True
            while bandera2:
                print("Elija el sub-modulo")
                opc2=int(input("\t1. Introduccion a la programacion\n"
                            "\t2. PseInt\n"
                            "\t3. Python\n"
                            "\t4. Salir"))
                if opc2==1:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["introduccion a la algoritmia"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["introduccion a la algoritmia"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["introduccion a la algoritmia"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["introduccion a la algoritmia"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida") 
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["asignado"]["fundamentos"]["introduccion a la algoritmia"]["notaFinal"]= notaFinal
                        if notaFinal<= 60:
                            camper[id][sub-estado]="en riesgo"
                if opc2==2:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["PseInt"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["PseInt"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["PseInt"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["PseInt"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida") 
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["asignado"]["fundamentos"]["PseInt"]["notaFinal"]= notaFinal
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
                if opc2==3:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["Python"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["Python"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["Python"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["fundamentos"]["Python"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida") 
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["asignado"]["fundamentos"]["Python"]["notaFinal"]= notaFinal
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
                if opc2==4:
                    bandera2=False
                else:
                    print("Opcion invalida")
                with open(archivo, "w+") as json_file:
                        json_file.write(json.dumps(pruebas,indent=4))
        elif opc==2:
            bandera2=True
            while bandera2:
                print("Elija el sub-modulo")
                opc2=int(input("\t1. HTML\n"
                            "\t2. CSS\n"
                            "\t3. Bootstrap\n"
                            "\t4. Salir"))
                if opc2==1:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["HTML"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["HTML"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["HTML"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["HTML"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida")
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["asignado"]["web"]["HTML"]["notaFinal"]= notaFinal
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
                if opc2==2:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["CSS"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["CSS"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["CSS"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["CSS"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida")
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["asignado"]["web"]["CSS"]["notaFinal"]= notaFinal
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
                if opc2==3:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["Bootstrap"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["Bootstrap"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["Bootstrap"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["asignado"]["web"]["Bootstrap"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida")
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["asignado"]["web"]["Bootstrap"]["notaFinal"]= notaFinal 
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
                if opc2==4:
                    bandera2=False
                else:
                    print("Opcion invalida")
                with open(archivo, "w+") as json_file:
                        json_file.write(json.dumps(pruebas,indent=4))
        elif opc==3:
            bandera3=True
            while bandera3:
                print("Elija la asignacion")
                opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                if opc==1:
                    practica =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["formal"]["practica"]= str(practica)
                elif opc==2:
                    teorica =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["formal"]["teorica"]= str(teorica)
                elif opc==3:
                    quices =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["formal"]["quices"]= str(quices)
                elif opc==4:
                    trabajos =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["formal"]["trabajos"]= str(trabajos)
                elif opc==5:
                    bandera3=False
                else:
                    print("Opcion invalida")
                notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                pruebas[id]["elegido"]["formal"]["notaFinal"]= notaFinal
                if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
            with open(archivo, "w+") as json_file:
                json_file.write(json.dumps(pruebas,indent=4))
        elif opc==4:
            bandera2=True
            while bandera2:
                print("Elija la opcion")
                opc2=int(input("\t1. Principal\n"
                               "\t2. Secundaria\n"
                               "\t3. Salir"))
                if opc==1:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                                    "\t2. Teorica\n"
                                    "\t3. Quices\n"
                                    "\t4. Trabajos"
                                    "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBD"]["principal"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBDsecundaria"]["principal"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBDsecundaria"]["principal"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBDsecundaria"]["principal"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida")
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["elegido"]["SGBDsecundaria"]["principal"]["notaFinal"]= notaFinal
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
                elif opc==2:
                    bandera3=True
                    while bandera3:
                        print("Elija la asignacion")
                        opc3=int(input("\t1. Practica\n"
                                    "\t2. Teorica\n"
                                    "\t3. Quices\n"
                                    "\t4. Trabajos"
                                    "\t5. Salir"))
                        if opc==1:
                            practica= int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBD"]["secundaria"]["practica"]= str(practica)
                        elif opc==2:
                            teorica=int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBD"]["secundaria"]["teorica"]= str(teorica)
                        elif opc==3:
                            quices=int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBD"]["secundaria"]["quices"]= str(quices)
                        elif opc==4:
                            trabajos=int(input("Ingrese la nota"))
                            pruebas[id]["elegido"]["SGBD"]["secundaria"]["trabajos"]= str(trabajos)
                        elif opc==5:
                             bandera3=False
                        else:
                            print("Opcion invalida")
                        notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                        pruebas[id]["elegido"]["SGBD"]["secundaria"]["notaFinal"]= notaFinal
                        if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
            with open(archivo, "w+") as json_file:
                json_file.write(json.dumps(pruebas,indent=4))
        elif opc==5:
            bandera3 =True
            while bandera3:
                print("Elija la asignacion")
                opc3=int(input("\t1. Practica\n"
                            "\t2. Teorica\n"
                            "\t3. Quices\n"
                            "\t4. Trabajos"
                            "\t5. Salir"))
                if opc==1:
                    practica =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["backend"]["practica"]= str(practica)
                elif opc==2:
                    teorica =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["backend"]["teorica"]= str(teorica)
                elif opc==3:
                    quices =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["backend"]["quices"]= str(quices)
                elif opc==4:
                    trabajos =int(input("Ingrese la nota"))
                    pruebas[id]["elegido"]["backend"]["trabajos"]= str(trabajos)
                elif opc==5:
                    bandera3=False
                else:
                    print("Opcion invalida")
                notaFinal= ((practica*0.6)+(teorica*0.3)+(((trabajos/quices)/2)*0.1))
                pruebas[id]["elegido"]["backend"]["notaFinal"]= notaFinal
                if notaFinal<60
                            camper[id][sub-estado]="en riesgo"
            with open(archivo, "w+") as json_file:
                json_file.write(json.dumps(pruebas,indent=4))
        elif opc==6:
            bandera=False
        else:
            print("Opcion invalida")
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
            with open(jsonCamper, "w") as f:
                json.dump(camper, f, indent=4)
        elif opc==2:
            pruebaModulo()
        elif opc==3:
            bandera =False
            os.system('clear')
        else:
            print("Respuesta invalida")
