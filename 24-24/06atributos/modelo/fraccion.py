class Fraccion:

    # Atributos
    numerador = 1
    denominador = 1

    # Constructor
    def __init__(self, num, dem):
        self.numerador = num
        self.denominador = dem

    def toString(self):
        return "%s / %s"%(self.numerador,self.denominador)
    
    def __str__(self):
        return "%s / %s"%(self.numerador,self.denominador)

    def multiplicar(self, frac2):
        rnum = self.numerador * frac2.numerador
        rden = self.denominador * frac2.denominador
        # return rnum, rden 
        return Fraccion(rnum, rden )