Algoritmo promedio_estudiantes
    Escribir "INGRESE LAS CALIFICACIONES"
    Escribir "Nota parcial 1: "
    Leer nota1
    Escribir "Nota parcial 2: "
    Leer nota2
    Escribir "Nota parcial 3: "
    Leer nota3
    sumatoria = nota1 + nota2 + nota3
    promedio = sumatoria / 3
    Si sumatoria >= 21 Entonces
        Escribir "APROBADO"
    SiNo
        Si sumatoria >= 18  Entonces
            Escribir "Nota remedial: "
            Leer remedial
            sumatoria = sumatoria + remedial
            promedio = sumatoria / 4
            Si sumatoria >= 28 Entonces
                Escribir "APROBADO CON REMEDIAL"
            SiNo
                Escribir "REPROBADO"
            Fin Si
        SiNo
            Escribir "REPROBADO"
        Fin Si
    Fin Si
    Escribir "PROMEDIO: ", promedio
FinAlgoritmo