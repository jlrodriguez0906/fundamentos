import os
from modelo.cuenta import Cuenta

class Manejador:
    cuentas = []

    # Crear un nueva cuenta
    def crear_cuenta(self):
        os.system("cls")
        print("CREANDO NUEVA CUENTA")
        print("====================")
        print("Nombre del cliente:")
        nombre = input()
        print("Número de cuenta:")
        cuenta = input()
        print("Monto inicial:")
        monto = input()

        nuevo = Cuenta(nombre, cuenta, monto)
        self.cuentas.append(nuevo)
    
    # Mostrar todas las cuentas
    def mostrar_cuentas(self):
        os.system("cls")
        print("LISTA DE CLIENTES")
        print("====================")
        for item in self.cuentas:
            print("%s %s $%s"%(item.nro_cuenta, item.cliente, item.saldo)  )
        print("Presione enter para continuar...")
        input()

    # Depositar
    def depositar(self):
        os.system("cls")
        print("DEPOSITOS")
        print("====================")
        print("Ingrese número de cuenta: ")
        cuenta = input()

        print("Ingrese monto: ")
        monto = input()

        for item in self.cuentas:
            if(item.nro_cuenta == cuenta):
                print( item.depositar(monto) )
                
        print("Presione enter para continuar...")
        input()
