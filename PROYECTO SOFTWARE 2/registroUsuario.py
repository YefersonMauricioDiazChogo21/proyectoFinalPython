import json
archivo = "usuario.json"
camper ={}
with open(archivo, "r") as a: 
        camper = json.loads(a.read())
def registroCamper():
    bandera = True

    while bandera:
        print("REGISTRO CAMPERS")
        selec = int(input("\n\t1. Registrar camper\n"
                          "\t2. Listar campers inscritos\n"
                          "\t3. salir al menu principal\n\t"))
        if selec == 1:

            documento = input("Numero de Documento del camper:\n")
            camper[documento]={"nombre" :str(input("Nombres:\n")),
                            "apellidos" : str(input("Apellidos:\n")),
                            "direccion" : str(input("Ditreccion de residencia:\n")),
                            "acudiente": str(input("Nmbre del acudiente:\n")),
                            "telefonos": [],
                            "estado": "inscrito"
                            }
            bandera2=True
            while bandera2:
                telefonos={}
                selec2=0
                selec2= input("Ingrese el tipo de contacto:\n"
                                            "\t1. telefono fijo\n"
                                            "\t2. telefono celular\n-")
                tel = str(input("Ingrese el numero:\n"))
                if selec2 ==1:
                    telefonos["fijo"] = tel
                else:
                    telefonos["celular"] = tel
                camper[documento]["telefonos"].append(telefonos)
                opc3 = int(input("Desea agregar otro numnero mde telefono?"
                                 "\n1. no"
                                 "\n2. si\n-"))
                if opc3 == 1:
                    bandera2 = False
            with open(archivo, "w+") as a:
                a.write(json.dumps(camper,indent=4))
        elif selec==2:
            for id in camper:
                print(camper[id])
        elif selec ==3:
            bandera = False
        else:
            print("Opcion invalida")
            bandera = True
    