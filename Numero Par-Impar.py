"""
    Determine si un número ingresado por el usuario es par o impar.

    Entradas: Numero Entero.
    Salidas: Afirmación sobre si el número ingresado es par o impar, a modo de cadena.
    Proceso:
        Definir la paridad del número ingresado en Bool, obteniendo el
        modulo 2 de este.

        Decidir imprimir entre 2 textos determinados, basandose en la
        desición anterior.
    Variables: valor, modulo, condición, numero, paridad, textoPar, textoImpar.
"""

#Funciones básicas
def leerFloat(mensaje):
    valor= int(input(mensaje))
    return valor
def imprimirTexto (mensaje):
    print(mensaje)

#Funcion que permite calcular la paridad de un número
def definirParidad_Numero (num1):
    modulo=num1%2
    if modulo == 0:
        paridad=True
    else: paridad=False
    return paridad

#Funcion que permite imprimir 1 de 2 mensajes, dependiendo de una condicion
def imprimirMensajeDesicion (condicion, mensaje1, mensaje2):
    if condicion == True:
        imprimirTexto(mensaje1)
    if condicion == False:
        imprimirTexto(mensaje2)

#Textos determinados
textoPar=("El número ingresado es par.")
textoImpar=("El número ingresado es impar.")

#Funcion principal que ejecuta el programa
def main():
    numero = leerFloat("Ingrese un número Entero: ")
    paridad = definirParidad_Numero(numero)
    imprimirMensajeDesicion (paridad, textoPar, textoImpar)

main()