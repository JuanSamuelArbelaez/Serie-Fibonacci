"""
    Cree un método que dado un número entero positivo, retorne la cantidad de dígitos que tiene el número

    Entradas: n
    Salidas: La cantidad de dígitos que tiene n
    Funciones:
        imprimirTexto(mensaje): Imprime un mensaje.
        leerInt(mensaje): Lee un entero.
        calcularValorAbsoluto(n): Calcula el valor absoluto.
        calcular_CantDigitos(n): Calcula la cantidad de dígitos de un número
    Variables:
        mensaje, valor, n, m, valorAbsoluto, contador, absoluto, digitos
"""

def imprimirTexto(mensaje): #Función que imprime
    print(mensaje)

def leerInt(mensaje): #Función que lee enteros
    valor= int(input(mensaje))
    return valor

def calcularValorAbsoluto(n): #Función que calcula el valor absuluto
    valorAbsoluto = n
    m=1-2
    if n < 0:
        valorAbsoluto = n*m
    return valorAbsoluto

def calcular_CantDigitos(n): #Función que calcula la cantidad de dígitos de un número
    contador = 1
    while (n//10) >= 1:
        n=n//10 
        contador += 1
    return contador

def main(): #Función principal que ejecuta el programa
    n = leerInt("Ingrese un número: ")
    absoluto = calcularValorAbsoluto(n)
    digitos = calcular_CantDigitos(absoluto)
    imprimirTexto(str(n) + " tiene " + str(digitos) + " digitos.")

main()