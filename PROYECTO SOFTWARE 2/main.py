from registroUsuario import *
from gestionTrabajo import *
from registroPruebas import *
from gestorDeMatricula import *
from camperRiesgo import *
from reportes import *

saludo = "Bienvenidos al sistema de gestión de campers"
menuPrincipal = (
    "Elige la opción de nuestro menú que desees\n"
    "\t1. Registro de campers\n"
    "\t2. Gestión de trabajo\n"
    "\t3. Registro de pruebas\n"
    "\t4. Gestor de matrículas\n"
    "\t5. Campers en riesgo\n"
    "\t6. Reportes"
)
opc =0
def menu() -> int:
    global opc
    opc =0
    bandera = True
    while bandera:
        print(menuPrincipal)
        try:
            opc = int(input())
            
            return opc
        except ValueError:
            bandera = True
bandera2 = True
while bandera2:
        print(saludo)
        print(menuPrincipal)
        opc= int(input("\t"))
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
        elif opc > 6:
             print("Respuesta invalida")
