"""
    Cree un programa que permita imprimir los divisores comunes que hay entre dos números,
    es decir, los números que los dividan de forma exacta a ambos.

    Entradas: n y m.
    Salidas: los divisores comúnes entre n y m.
    Funciones:
        imprimirTexto(mensaje): Imprime un mensaje.
        leerInt(mensaje): Lee un entero.
        clasificarMayor(num1, num2): Retorna el mayor de 2 números.
        imprimirDivisoresComunes(num1, num2): Imprime los divisores comúnes entre n y m.
        main(): Ejecuta el programa
    Variables:
        mensaje, valor, num1, num2, numMayor, div1, mod1, mod2 n, m.
"""

def imprimirTexto(mensaje): #Funcion que imprime
    print(mensaje)

def leerInt(mensaje): #Funcion que lee enteros
    valor= int(input(mensaje))
    return valor

def clasificarMayor(num1, num2): #Funcion que obtiene el mayor de 2 números
    numMayor=0
    if num1 > num2:
        numMayor = num1
    else:
        numMayor = num2
    return numMayor

def imprimirDivisoresComunes(num1,num2): #Funcion que imprime los divisores comúnes entre n y m
    numMayor = clasificarMayor(num1, num2)
    div1 = numMayor
    while div1 >= 1:
        mod1 = num1%div1
        mod2 = num2%div1
        if mod1 == 0 and mod2 == 0:
            imprimirTexto(div1)
        div1 -= 1

def main(): #Funcion que ejecuta el programa
    n = leerInt("Ingrese un primer número: ")
    m = leerInt("Ingrese un segundo número: ")
    imprimirTexto("Los divisores comúnes entre " + str(n) + " y " + str(m) + " son: ")
    imprimirDivisoresComunes(n, m)

main()