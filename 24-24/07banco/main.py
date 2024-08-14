from modelo.cuenta import Cuenta

cue = Cuenta("José Rodríguez","100",20)
# cue.tipo_cuenta = "CORRIENTE"

print( cue.informacion_cuenta() )
print( cue.depositar(85) )
print( cue.depositar(35) )
print( cue.informacion_cuenta() )
print( cue.retirar(50) )
print( cue.informacion_cuenta() )
