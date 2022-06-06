#activacion = input("Ingrese la letra 'a' para iniciar el tramite")

#num_tarjeta = int(input("Ingrese el numero de la tarjeta: "))


clave = 12345
dni = 12345678

def consultar_cuentas():
    print("a - Posición Global")
    print("b - Movimientos")
    opcion_cuentas = input()

        



clave_ingresada = 12345#int(input("Ingrese la clave: "))
if (clave_ingresada==clave) == False:
    contador_intentos = 0
    while contador_intentos<3 and (clave_ingresada==clave) == False:
        clave_ingresada = int(input("La clave ingresada es incorrecta, intente otra vez: "))
        contador_intentos = contador_intentos + 1
        if contador_intentos == 3 and (clave_ingresada==clave) == False:
            print("ATENCIÓN: Muchos intentos fallidos, tarjeta retenida.")
            exit()
dni_ingresado = 12345678 #int(input("Ingrese el numero de dni: "))
if (dni_ingresado==dni) == False:
    print("El DNI ingresado es incorrecto")
    exit()
print(" 1. Consultas   2. Retiros   3. Transferencias   4. Salir")

opcion_menu = int(input())
if opcion_menu == 1:
    tipo_moneda = input("Ingrese el tipo de moneda: ")
     
    consultar_cuentas()

else:
    print("nati")
    





    
