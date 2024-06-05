Algoritmo primos
	Escribir 'Ingrese un número: '
	Leer num
	Para i<-2 Hasta num-1 Con Paso 1 Hacer
		res = num % i
		Si res == 0 Entonces
			Escribir "NO ES PRIMO"
		SiNo
			Escribir "ES PRIMO"
		Fin Si
	Fin Para
FinAlgoritmo
