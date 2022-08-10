"""
    Cree un programa que, usando el ciclo for permita calcular la cantidad de
    números que hay entre m y n cuyos dos últimos dígitos son iguales.


    Entradas: m y n

    Salidas: aquellos numeros entre m y n cuyos ultimos 2 digitos sean iguales

    Procesos:
        leer m y n
        determinar cual es mayor
        determinar cuantos numeros en el intervalo cumplen con la regla
    
    Funciones:
        filtrar_Intervalo: Esta función permite identificar cuantos
            numeros en un intervalo cumplen con cierta condición.
        
    Variables:
        mayor, menor, contador, digito1, digito2, m, n, numMayor,
        numMenor, numsFiltrados.
"""

from funciones import clasificarMayor, clasificarMenor, imprimirTexto, leerInt

#Función que filtra un intervalo, obteniendo aquellos numeros que cumplen con cierto parametro. Retorno de la cantidad de numeros filtrados.
def filtrar_Intervalo(mayor, menor):
    contador=0
    for i in range (menor, mayor):
        digito1=i%10 #Si el numero es 134, se obtiene 4
        digito2=(i%100)//10 #Si el numero es 134, se obtiene 3
        if digito1==digito2:
            contador+=1
    return contador

#Función principal que ejecuta el programa
def main():
    m=leerInt("Ingrese un primer numero: ")
    n=leerInt("Ingrese un segundo numero: ")
    numMayor=clasificarMayor(m, n)
    numMenor=clasificarMenor(m, n)
    numsFiltados=filtrar_Intervalo(numMayor, numMenor)
    imprimirTexto("Entre "+str(numMenor)+" y "+str(numMayor)+" hay "+str(numsFiltados)+" numeros cuyos ultimos 2 digitos son iguales")

main()