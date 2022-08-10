"""
    Cree un método que dado un número entero determine si es o nó un número perfecto. 

    Entradas: n
    Salidas: bool sobre si n es o nó un número perfecto
    Funciones:
        imprimirTexto(mensaje): Imprime un mensaje.
        leerInt(mensaje): Lee un entero.
        definirNumeroPerfecto(n): Define si un número es perfecto o no.
        imprimirMensajeDesicion(condicion, mensaje1, mensaje2): Imprime 1 de 2 mensajes, dependiendo de una condición
        main(): Ejecuta el programa.
    Variables:
        mensaje, valor, n, m, acumulador, perfecto, condicion, mensaje1, mensaje2, texto1, texto2
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

def imprimirMensajeDesicion(condicion, mensaje1, mensaje2): #Función que imprime 1 de 2 mensajes, dependiendo de un valor bool.
    if condicion == True:
        imprimirTexto(mensaje1)
    else:
        imprimirTexto(mensaje2)

def main(): #Función principal que ejecuta el programa
    texto1 = "El numero ingresado es perfecto."
    texto2 = "El numero ingresado no es perfecto."
    n = leerInt("Ingrese un número: ")
    perfecto = definirNumeroPerfecto(n)
    imprimirMensajeDesicion(perfecto, texto1, texto2)

main()