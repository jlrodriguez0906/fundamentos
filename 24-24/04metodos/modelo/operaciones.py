class Operaciones:

    def suma(self, num1, num2):
        res = num1 + num2
        return res
    
    def tabla(self, numero):
        for i in range(1, 11):
            res = numero * i
            print( numero, " * ", i, " = ", res )

    def comprobar(self, numero):
        if self.esPar(numero):
            return "PAR"
        return "IMPAR"

    def esPar(self, numero):
        if numero % 2 == 0 :
            return True
        return False