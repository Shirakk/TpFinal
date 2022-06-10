CLAVE = 12345
DNI = 12345678
CUENTA_DESTINO = 98765
saldo_disponible_ars = 
saldo_disponible_pen = 3564

# la parte de menu de validacion de datos se podria poner en un def
# hay que solucionar que las opciones se vuelvan a mostrar en pantalla cada vez que el usuario vuelva al menu.
# problema solucionado
#meter todos los prints y inputs en una sola funcion
#pensar el codigo sin prints
# hayq ue solucionar el problema de los saldos



#import csv
import os #<---- Este módulo provee una manera versátil de usar funcionalidades dependientes del sistema operativo
import getpass #<---- Solicita al usuario una contraseña sin hacer eco (sin mostrarta en pantalla)

def consultar_cuentas():
    os.system('cls')
    print("a - Posición Global")
    print("b - Movimientos")
    opcion_cuentas = input()
    if opcion_cuentas == "a":
        tipo_moneda = int(input("Ingrese el tipo de moneda, presione 1 para Soles y 2 para Pesos Argentinos "))
        if tipo_moneda == 1:
            #saldo_disponible_pen = 3564
            print(f"Saldo displonible: {saldo_disponible_pen} Soles")
        elif tipo_moneda == 2:
            #saldo_disponible_ars = 85000
            print(f"Saldo disponible: {saldo_disponible_ars} Pesos")
    volver = input("""Desea regresar al menu de inicio?
    Presione 'y' para volver y 'n' para salir: """)
    if volver == 'y':
        os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear)
        menu()
    elif volver == 'n':
        os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear)
        print("Gracias por elegir InterBanca")
        exit()

#def retiros():



def transferencias():
    os.system('cls')
    tipo_moneda = int(input("Ingrese el tipo de moneda, 1 para pesos argentinos 2 para pesos peruanos: "))
    if tipo_moneda == 1:
        cantidad_ingresada = float(input("Ingrese la cantidad de dinero a transferir: "))
    if cantidad_ingresada > saldo_disponible_ars:
        print("Lo siento pero esa cantidad no esta disponible en su cuenta de pesos argentinos.")    
    cuenta_destino = int(input("Por favor ingrese el numero de cuenta de destino: "))
    if cuenta_destino != CUENTA_DESTINO:
        print("Lo siento pero cuando buscabamos esa cuenta no la encontramos, su dinero sera devuelto en 3 dias.")
        #saldo_disponible_ars = saldo_disponible_ars - cantidad_ingresada
    volver = input("Desea regresar al menu de inicio? presione y para si o n para no: ")
    if volver == 'y':
        menu()
    elif volver == 'n':
        exit()

def validacion():
    os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear)
    print("Por su seguridad su clave no sera mostrada en pantalla mientras la ingresa.")
    clave_ingresada = 12345#int(getpass.getpass("Ingrese su clave: ")) #12345
    if clave_ingresada != CLAVE:
        contador_intentos = 0
        while contador_intentos<3 and clave_ingresada != CLAVE:
            os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear)
            clave_ingresada = int(getpass.getpass("La clave ingresada es incorrecta, intente otra vez: "))
            os.system('cls')
            contador_intentos = contador_intentos + 1
            if contador_intentos == 3 and clave_ingresada != CLAVE:
                print("ATENCIÓN: Muchos intentos fallidos, tarjeta retenida.")
                exit()
    dni_ingresado = 12345678#int(input("Ingrese su numero de DNI: ")) #12345678
    if dni_ingresado != DNI:
        print("Lo sinto pero el DNI que ha ingresado no esta en nuestra base de datos.")
        exit()
    return validacion()

def menu():
    """
    Imprime un menú, le pide al usuario que elija una opción y luego llama a la función apropiada.
    """
    os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear)
    # fin = False
    # while not(fin): <--- otra forma de solucionar el menu() de los otros def. en mi opinion es mejor el menu()
    print("""          ************** Bienvenido a InterBanca *********************
          * 1. Consultas   2. Retiros   3. Transferencias   4. Salir *
          ************************************************************ """)
    opcion_menu = int(input("Ingrese su opcion: "))
    if opcion_menu == 1:
        consultar_cuentas()

    elif opcion_menu == 2:
        retiros()
    elif opcion_menu == 3:
        transferencias()
    elif opcion_menu == 4:
        os.system('cls') #<--- Limpia la pantalla (SOLO OS DE WINDOWS, PARA LINUX O MAC CAMBIAR cls POR clear)
        print("Gracias por elegir InterBanca.")
        print("Recuerde retirar su tarjeta.")
        exit()





def menu_prints():
    
menu()



