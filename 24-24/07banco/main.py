# from modelo.cuenta import Cuenta

# cue = Cuenta("José Rodríguez","100",20)
# # cue.tipo_cuenta = "CORRIENTE"

# print( cue.informacion_cuenta() )
# print( cue.depositar(85) )
# print( cue.depositar(35) )
# print( cue.informacion_cuenta() )
# print( cue.retirar(50) )
# print( cue.informacion_cuenta() )

# print("---------------------")

# tx = cue.transaccion
# num = 1
# for item in tx:
#     print( "%s. %s"%(num,item) )
#     num = num + 1

import os

cuentas = []

while True:
    os.system("cls")
    os.system("dir")
    print("BIENVENIDO - BANCO FLORES")
    print("=========================")
    print("1. Cuenta nueva")
    print("2. Depósito")
    print("3. Retiro")
    print("4. Consulta de saldo")
    print("5. Consulta de transacciones")
    print("6. Salir")
    print("")
    print("Ingrese opción: ")
    op = input()
    if op == "6":
        break