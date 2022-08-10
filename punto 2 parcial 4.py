"""
    Diseñe un algoritmo que permita calcular la nota definitiva de un examen,
    para ello se debe preguntar la cantidad de preguntas del examen y leer un
    arreglo de boolean (True o False) de ese tamaño, cada posición representa
    si la pregunta fue correcta o incorrecta, considere que el examen se
    califica sobre 5 y que cada pregunta tiene el mismo valor.


    Entradas: cantidad de preguntas, bool sobre la aprobación de cada preguntas
    
    Salidas: la nota definitivas
    
    Procesos:
        Leer la cantidad de preguntas
        Crear un arreglo de tipo booleano de la longitud requerida
        Leer como Bool cada posición del arreglo creado
        Calcular el valor individual de cada pregunta
        Calcular la nota final
    
    Funciones:
        leerArreglo_Bool: Esta función permite leer un arreglo
            de booleanos de longitud n
        
        calcular_ValorPregunta: Esta función permite calcular
            el valor de cada pregunta en un examen calificado
            sobre 5, si se conoce la cantidad de preguntas.
        
        calcular_NotaFinal: Esta función permite conocer la nota
            final de un examen calificado sobre 5, si se conoce
            la cantidad de preguntas y cuales fueron respondidas
            correctamente.
    
    Variables:
        preguntas, respuestasBooleano, i, cantPreguntas,
        valorPregunta, nota, notaFinal.
"""

from funciones import imprimirTexto, leerInt, leerStr

#Función que lee un arreglo de Booleanos. Retorna un arreglo Bool, que representa las respuestas del estudiante.
def leerArreglo_Bool(preguntas): 
    respuestasBooleano=[False]*preguntas
    for i in range (preguntas):
        respuesta=leerStr("Ingrese SI, si el estudiante respondió correctamente a la pregunta "+str(i+1)+". De lo contrario, responda NO: ").upper()
        if respuesta=="SI":                     
            respuestasBooleano[i]=True
        else:
            continue
    return respuestasBooleano

#Función que calcula cuanto vale cada pregunta del examen. Retorno del valor individual de cada pregunta
def calcular_ValorPregunta(cantPreguntas):
    valorPregunta=5/cantPreguntas #El examen se califica sobre 5
    return valorPregunta

 #Función que calcula la nota final del examen. Retorna el valor de la nota final.
def calcular_NotaFinal(respuestasBool, valorPregunta):
    nota=0
    for i in range (len(respuestasBool)):
        if respuestasBool[i]:
            nota+=valorPregunta
        continue
    return nota

#Función principal que ejecuta el programa
def main():
    cantPreguntas=leerInt("Ingrese la cantidad de preguntas del examen: ")
    respuestasBool=leerArreglo_Bool(cantPreguntas)
    valorPregunta=calcular_ValorPregunta(cantPreguntas)
    notaFinal=calcular_NotaFinal(respuestasBool, valorPregunta)
    imprimirTexto("La nota final es: "+ "{0:.2f}".format(notaFinal))

main()