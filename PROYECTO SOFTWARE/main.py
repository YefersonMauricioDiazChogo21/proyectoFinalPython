from registroUsuario import *
from gestionTrabajo import *
from registroPruebas import *
from gestorDeMatricula import *
from camperRiesgo import *
from reportes import *
saludo = "Bienvenidos al sistema de gestios de campers"
menuPrincipal = "Elige la opcion de nuestro menu que desees\n\t1. Registro de campers\n\t2. Gestion de trabajo\n\t3. Registro de pruebas\n\t4. Gestor de matriculas\n\t5. campers en riesgo\n\t6. Reportes"
bandera =True
opc = 0
def menu():
    global bandera, menuPrincipal, opc 
    while bandera:
        print(menuPrincipal)
        try: 
            opc += int(input("\t -"))
        except Exception as Error:
            print(Error)
            bandera = True

bandera2 = True
while bandera2:
    menu()
    if opc == 1:
        registroCamper()
    elif opc == 2:
        gestionTrabajo()
    elif opc == 3:
        registroPruebas()
    elif opc == 4:
        gestionMatricula()
    elif opc == 5:
        camperRiesgo()
    elif opc == 6:
        reportes()
    else:
        print("Respuesta invalida")