"""
    Cree un programa que calcule la multiplicación entre n y m usando sumas sucesivas

    Entradas: n y m.
    Salidas: Sumas sucesivas.
    Funciones:
        imprimirTexto(mensaje): Imprime un mensaje.
        leerInt(mensaje): Lee un entero.
        calcularMultiplicacion(num1, num2): Calcula una multiplicación por sumas sucesivas.
        main(): Ejecuta el programa
    Variables:
        mensaje, valor, num1, num2, suma, n, m
"""

def imprimirTexto(mensaje): #Función que imprime
    print(mensaje)

def leerInt(mensaje): #Función que lee enteros
    valor= int(input(mensaje))
    return valor

def calcularMultiplicacion(num1, num2): #Funcion que calcula una multiplicación entre 2 números, mediante sumas sucesivas.
    suma=0
    while num2 > 0:
        suma += num1
        num2 -= 1
        imprimirTexto(suma)

def main(): #Funcion que ejecuta el programa
    n = leerInt("Ingrese un primer número: ")
    m = leerInt("Ingrese un segundo número: ")
    calcularMultiplicacion(n, m)

main()