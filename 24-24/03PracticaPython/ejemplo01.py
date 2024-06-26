print("Ingrese nota 1:")
n1 = int( input() )
print("Ingrese peso 1:")
peso1 = int( input() )
promedio1 = n1*peso1/100

print("Ingrese nota 2:")
n2 = int( input() )
print("Ingrese peso 2:")
peso2 = int( input() )
promedio2 = n2*peso2/100

print("Ingrese nota 3:")
n3 = int( input() )
print("Ingrese peso 3:")
peso3 = int( input() )
promedio3 = n3*peso3/100

promedio_final = promedio1 + promedio2 + promedio3
print("El promedio pronderado es: ",promedio_final)