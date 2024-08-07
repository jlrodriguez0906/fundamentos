class Fraccion:

    # creando el método y sus parámetros
    def suma(self, n1, d1, n2, d2):
        nres = n1*d2 + d1*n2
        dres = d1 * d2
        print("Resp: ",nres,"/",dres)

    def resta(self, n1, d1, n2, d2): 
        self.suma( n1, d1, -1*n2, d2)

    def multiplicar(self, n1, d1, n2, d2): 
        nres = n1 * n2
        dres = d1 * d2
        return nres, dres
    
    def dividir(self, n1, d1, n2, d2):
        return self.multiplicar(n1,d2,d1,n2)