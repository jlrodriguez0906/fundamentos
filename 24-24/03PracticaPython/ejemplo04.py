print("ORDENAR 3 NÚMEROS")

print("Ingrese numero 1: ")
num1 = int(input())

print("Ingrese numero 2: ")
num2 = int(input())

print("Ingrese numero 3: ")
num3 = int(input())

if (num1 > num2) and (num2 > num3):
    print(num3, " - ", num2, " - ", num1)
elif num1 > num3 > num2:
    print(num2, " - ", num3, " - ", num1)
elif num2 > num1 > num3:
    print(num3, " - ", num1, " - ", num2)
elif num2 > num3 > num1:
    print(num1, " - ", num3, " - ", num2)
elif num3 > num1 > num2:
    print(num2, " - ", num1, " - ", num3)
else:
    # num3 > num2 > num1:
    print(num1, " - ", num2, " - ", num3)