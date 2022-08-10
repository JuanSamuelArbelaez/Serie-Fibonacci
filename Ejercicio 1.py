"""
    Cree un programa que permita imprimir los números pares que hay entre m y n de forma descendente.

    Entradas: m y n.
    Salidas: los numeros pares entre m y n de manera descendente.
    Funciones:
        imprimirTexto(mensaje): Imprime un mensaje.
        leerInt(mensaje): Lee un entero.
        clasificarMayor(num1, num2): Retorna el mayor de 2 números.
        clasificarMenor(num1, num2): Retorna el menor de 2 números.
        definirParidad_Numero(num1): Define la paridad de un número.
        imprimirIntervalo(numMenor, numMayor): Imprime los números pares, en un intervalo, de manera descendente
        main(): Ejecuta el programa
    Variables:
        mensaje, valor, num1, num2, numMayor, numMenor, modilo, paridad, n, m
"""

def imprimirTexto(mensaje): #Función que imprime
    print(mensaje)

def leerInt(mensaje): #Función que lee enteros
    valor= int(input(mensaje))
    return valor

def clasificarMayor(num1, num2): #Función que obtiene el mayor de 2 números
    numMayor=0
    if num1 > num2:
        numMayor = num1
    else:
        numMayor = num2
    return numMayor

def clasificarMenor(num1, num2): #Función que obtiene el menor de 2 números
    numMenor=0
    if num1 < num2:
        numMenor = num1
    else:
        numMenor = num2
    return numMenor

def definirParidad_Numero(num1): #Función que define la paridad de un número
    modulo=num1%2
    if modulo == 0:
        paridad=True
    else: paridad=False
    return paridad

def imprimirIntervalo(num1, num2): #Función que imprime los números pares, en un intervalo, de manera descendente
    paridad=0
    numMayor = clasificarMayor(num1, num2)
    numMenor = clasificarMenor(num1, num2)
    imprimirTexto("Los números pares entre "+ str(numMayor)+" y " + str(numMenor) + ", organizados de mayor a menor, son: ")
    while numMenor <= numMayor:
        paridad = definirParidad_Numero(numMayor)
        if paridad == False:
            numMayor -= 1
            continue
        else:
            imprimirTexto(numMayor)
            numMayor -= 1

def main(): #Función principal que ejecuta el programa
    n = leerInt("Ingrese un primer número: ")
    m = leerInt("Ingrese un segundo número: ")
    imprimirIntervalo(n, m)

main()