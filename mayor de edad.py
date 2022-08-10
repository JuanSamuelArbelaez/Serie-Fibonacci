"""
    Construya un programa que permita determinar si una persona es mayor de edad o no.

    Entrada: Edad de una persona en años.
    Salida: Afirmación sobre si la persona es mayor de edad o no, a modo de cadena.
    Procesos:
        Comparar la edad ingresada con una constante definida, e indicar si es mayor-igual
        a otro, o no.
    Variables: valor, edad, num1, mayorEdad, condición, texto1, texto2, mayoriaEdad.
"""

#Funciones básicas
def leerFloat(mensaje):
    valor= float(input(mensaje))
    return valor
def imprimirTexto (mensaje):
    print(mensaje)

#Función que indica si un numero es mayor-igual a otro, o no
def compararValores (num1):
    if num1 >= 18:
        mayorEdad = True
    else: 
        mayorEdad = False
    return mayorEdad

#Funcion que permite imprimir 1 de 2 mensajes, dependiendo de una condicion
def imprimirMensajeDesicion (condicion, mensaje1, mensaje2):
    if condicion == True:
        imprimirTexto(mensaje1)
    if condicion == False:
        imprimirTexto(mensaje2)

#Textos determinados
texto1 = ("El Usuario es mayor de edad.")
texto2 = ("El Usuario es menor de edad.")

#Funcion principal que ejecuta el programa
def main():
    edad = leerFloat("Indique la edad del Usuario: ")
    mayoriaEdad = compararValores(edad)
    imprimirMensajeDesicion (mayoriaEdad, texto1, texto2)

main()