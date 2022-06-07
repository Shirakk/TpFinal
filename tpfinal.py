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



import os #<---- Este módulo provee una manera versátil de usar funcionalidades dependientes del sistema operativo
os.system('cls')  
clave_ingresada = int(input("Ingrese su clave: ")) #12345
if clave_ingresada != CLAVE:
    contador_intentos = 0
    while contador_intentos<3 and clave_ingresada != CLAVE:
        os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear) 
        clave_ingresada = int(input("La clave ingresada es incorrecta, intente otra vez: "))
        contador_intentos = contador_intentos + 1
        if contador_intentos == 3 and clave_ingresada != CLAVE:
            print("ATENCIÓN: Muchos intentos fallidos, tarjeta retenida.")
            exit()
dni_ingresado = int(input("Ingrese su numero de DNI: ")) #12345678 
if dni_ingresado != DNI:
    print("El DNI ingresado es incorrecto")
    exit()

#print(" 1. Consultas   2. Retiros   3. Transferencias   4. Salir")
#opcion_menu = int(input())
#if opcion_menu == 1:
tipo_moneda = int(input("Ingrese el tipo de moneda, presione 1 para Soles y 2 para Pesos Argentinos "))
#    consultar_cuentas()
menu()

print(" 1. Consultas   2. Retiros   3. Transferencias   4. Salir")

opcion_menu = int(input())
if opcion_menu == 1:
    tipo_moneda = input("Ingrese el tipo de moneda: ")

    consultar_cuentas()


