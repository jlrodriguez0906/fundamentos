from modelo.fraccion import Fraccion

# Creando nueva instancia u objeto
fra = Fraccion()
fra.suma(3,7,2,5)
fra.resta(3,7,2,5)

a,b = fra.multiplicar(3,7,2,5)
print(a,"/",b)

a,b = fra.dividir(3,7,2,5)
print(a,"/",b)