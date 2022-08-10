"""
    Cree un programa que dado un número n imprima todos los números perfectos que hay en el rango de 1 a n.

    Entradas: n
    Salidas: Los números perfectos entre 1 y n.
    Funciones:
        imprimirTexto
        leerInt(mensaje): Lee un entero.
        definirNumeroPerfecto(n): Define si un número es perfecto o no.
        imprimirNumerosPerfectos(n): Imprime los numeros perfectos entre 1 y n
    Variables:
        mensaje, valor, n, m, acumulador, var
"""

def imprimirTexto(mensaje): #Función que imprime
    print(mensaje)

def leerInt(mensaje): #Función que lee enteros
    valor= int(input(mensaje))
    return valor

def definirNumeroPerfecto(n): #Función que define si un número es perfecto o no
    m = n-1
    acumulador = 0
    while m > 0:
        if n%m == 0:
            acumulador+=m
            m-=1
    return n==acumulador

def imprimirNumerosPerfectos(n): #Función que imprime los números perfectos entre 1 y n
    imprimirTexto("Los números perfectos entre 1 y " + str(n) + ", son: ")
    var = 1
    while var <= n:
        if definirNumeroPerfecto(var):
            imprimirTexto(var)
        var+=1

def main():
    n = leerInt ("Ingrese un número: ")
    imprimirNumerosPerfectos(n)

main()
