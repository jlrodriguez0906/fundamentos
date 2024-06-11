Algoritmo primos
	Escribir 'Ingrese un número: '
	Leer num
	esPrimo = 1
	Para i<-2 Hasta num-1 Con Paso 1 Hacer
		res = num % i
		Si res == 0 Entonces
			esPrimo = 0
		Fin Si
	Fin Para
	
	Si esPrimo == 1 Entonces
		Escribir "ES PRIMO"
	SiNo
		Escribir "NO ES PRIMO"
	FinSi
FinAlgoritmo
