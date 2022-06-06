#activacion = input("Ingrese la letra 'a' para iniciar el tramite")

#num_tarjeta = int(input("Ingrese el numero de la tarjeta: "))


CLAVE = 12345
DNI = 12345678

def menu():
    print(" 1. Consultas   2. Retiros   3. Transferencias   4. Salir")
    opcion_menu = int(input())
    if opcion_menu == 1:
        consultar_cuentas()
    

def consultar_cuentas():
    print("a - Posición Global")
    print("b - Movimientos")
    opcion_cuentas = input()
    if opcion_cuentas == "a":
        if tipo_moneda == 1:
            print("Saldo displonible: 3.564 Soles")
        elif tipo_moneda == "2":
            print("Saldo disponible: 85.000 Pesos")

<<<<<<< HEAD
    
    
clave_ingresada = 12345#int(input("Ingrese la clave: "))
if (clave_ingresada==clave) == False:
=======



#import getpass
clave_ingresada = 12345 #int(input("Ingrese la clave: "))
if (clave_ingresada==CLAVE) == False:
>>>>>>> d3f122d1c772e1f7b00ddf445eac8b3984fb5ba6
    contador_intentos = 0
    while contador_intentos<3 and (clave_ingresada==CLAVE) == False:
        clave_ingresada = int(input("La clave ingresada es incorrecta, intente otra vez: "))
        contador_intentos = contador_intentos + 1
        if contador_intentos == 3 and (clave_ingresada==CLAVE) == False:
            print("ATENCIÓN: Muchos intentos fallidos, tarjeta retenida.")
            exit()
dni_ingresado = 12345678 #int(input("Ingrese el numero de dni: "))
if (dni_ingresado==DNI) == False:
    print("El DNI ingresado es incorrecto")
    exit()
<<<<<<< HEAD
#print(" 1. Consultas   2. Retiros   3. Transferencias   4. Salir")
#opcion_menu = int(input())
#if opcion_menu == 1:
tipo_moneda = int(input("Ingrese el tipo de moneda 1 para Soles y 2 para Pesos Argentinos "))
#    consultar_cuentas()
menu()
=======
print(" 1. Consultas   2. Retiros   3. Transferencias   4. Salir")

opcion_menu = int(input())
if opcion_menu == 1:
    tipo_moneda = input("Ingrese el tipo de moneda: ")

    consultar_cuentas()

>>>>>>> d3f122d1c772e1f7b00ddf445eac8b3984fb5ba6
