"""
    Determine si la suma de dos números ingresados por el usuario es menor que 100 o no lo es.

    Entradas: Numero 1, Numero 2.
    Salida: Afirmacion sobre si la suma de ambos es menor que 100 o no lo es, a modo de cadena.
    Procesos:
        Comparar la suma de ambos números con 100, e indicar si es menor que 100, o no.
    Variables: valor, num1, num2, condicion, minoria, texto1, texto2, texto3, entrada1, entrada2.
"""

#Funciones básicas
def leerFloat(mensaje):
    valor= float(input(mensaje))
    return valor
def imprimirTexto (mensaje):
    print(mensaje)

#Funcion que permite imprimir 1 de 3 mensajes, dependiendo de una condicion
def imprimirMensajeDesicion (condicion, mensaje1, mensaje2, mensaje3):
    if condicion == True:
        imprimirTexto(mensaje1)
    if condicion == False:
        imprimirTexto(mensaje2)
    if condicion == "ninguno":
        imprimirTexto(mensaje3)

#Funcion que indica si la suma de 2 numeros es menor que 100, o no
def compararSuma_Numeros (num1, num2):
    if num1+num2 < 100:
        minoria = True
    else:
        if num1 + num2 > 100:
            minoria = False
        else:
            minoria = "ninguno"
    return minoria

#Textos predeterminados
texto1=("La suma de los numeros ingresados es menor que 100.")
texto2=("La suma de los numeros ingresados es mayor que 100.")
texto3=("La suma de los numeros ingresados es igual a 100.")

#Funcion principal que ejecuta el programa
def main():
    entrada1 = leerFloat("Ingrese el valor del numero 1: ")
    entrada2 = leerFloat("Ingrese el valor del numero 2: ")
    sumaComparada = compararSuma_Numeros(entrada1, entrada2)
    imprimirMensajeDesicion (sumaComparada, texto1, texto2, texto3)

main()