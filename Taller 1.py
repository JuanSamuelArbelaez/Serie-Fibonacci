"""
    Cree un procedimiento que imprima los múltiplos de 3 que se encuentren entre 6 y n,
    donde n tiene que ser superior a 6.

    Entradas: n
    Salidas: múltiplos de 3, mayores que 6, entre 6 y n.
    Funciones:
        imprimirTexto(mensaje): Imprime un mensaje.
        leerInt(mensaje): Lee un entero.
        calcularMultiplos(n, m): Imprime los múltiplos de 3 en un intervalo
    Variables:
        mensaje, valor, n, m
"""

def imprimirTexto(mensaje): #Función que imprime
    print(mensaje)

def leerInt(mensaje): #Función que lee enteros
    valor= int(input(mensaje))
    return valor

def calcularMultiplos(n, m): #Función que calcula múltiplos de 3 en un intervalo
    while n>=m:
        if m%3==0:
            print(m)
            m+=1

def main(): #Función principal que ejecuta el programa
    n = leerInt("Ingrese un número mayor a 6: ")
    m = 6
    calcularMultiplos(n, m)

main()