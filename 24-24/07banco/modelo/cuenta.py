class Cuenta:

    # Atributos - Datos
    cliente = ""
    nro_cuenta = ""
    tipo_cuenta = "AHORRO"
    saldo = 0.00
    transaccion = []

    # Métodos - Operaciones
    def __init__(self, cli, nro, saldo):
        self.cliente = cli
        self.nro_cuenta = nro
        self.saldo = saldo
        self.transaccion.append("DEPOSITO: %s\tSALDO: %s"%(saldo,saldo) )

    def informacion_cuenta(self):
        return "C. %s %s - CLIENTE: %s - SALDO: $%s"%(self.tipo_cuenta,
                           self.nro_cuenta, self.cliente,
                           self.saldo)
    
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        self.transaccion.append("DEPOSITO: %s\tSALDO: %s "%(monto, self.saldo) )
        return "Depósito realizado con éxito ($%s)"%(monto)

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            self.transaccion.append("RETIRO: -%s\tSALDO: %s "%(monto, self.saldo) )
            return "Retiro realizado con éxito (- $%s)"%(monto)
        return "Saldo insuficiente"
