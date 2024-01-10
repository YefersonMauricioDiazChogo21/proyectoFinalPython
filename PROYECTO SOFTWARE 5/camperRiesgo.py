import json
import os
archivo = "usuario.json"
with open(archivo,"r") as a:
    camper= json.loads(a.read())
def camperRiesgo():
    enRiesgo=[]
    cont=0
    for i in camper:
        if camper[i]["sub-estado"]=="en riesgo":
            enRiesgo.append(i)
            cont+=1
    if cont==0:
        print("No hay campers en riesgo")
    else:
        for i in enRiesgo:
            print(i,camper[i]["nombre"])
    input("Presione enter para salir\n")
    os.system('clear')

        
