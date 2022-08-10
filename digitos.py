"""
    Cree un programa que lea un numero entero de 2 dígitos y determinecuál de los
    dos dígitos es mayor.

    Entradas: Un numero de 2 digitos.
    Salida: Una afirmación sobre cual de los 2 digitos es mayor.
    Procesos:
        Tomar el modulo 10 del numero ingresado. Hacer una division entera de base
        10 del numero ingresado. Comparar ambos resultados e indicar cual es mayor.
    Variables:
        valor, condicion, digito1, num1, digito2, num2, num1_Mayor, texto1, texto2,
        texto3, numero, mayor.
"""

#Funciones básicas
def leerFloat(mensaje):
    valor= int(input(mensaje))
    return valor
def imprimirTexto (mensaje):
    print(mensaje)

#Funcion que permite imprimir 1 de 3 mensajes, dependiendo de una condicion
def imprimirMensajeDesicion (condicion, mensaje1, mensaje2, mensaje3):
    if condicion == 1:
        imprimirTexto(mensaje1)
    if condicion == 2:
        imprimirTexto(mensaje2)
    if condicion == 3:
        imprimirTexto(mensaje3)

#Funcion que permite obtener el segundo digito de un numero entero de 2 digitos.
def calcularDigito1 (num1):
    digito1=num1 // 10
    return digito1

#Funcion que permite obtener el primer digito de un numero entero de 2 digitos.
def calcularDigito2 (num1):
    digito2= num1 % 10
    return digito2

#Función que indica el mayor de 2 numeros.
def comparar_Numeros (num1, num2):
    if num1 > num2:
        num1_Mayor = 1
    else:
        if num1 < num2:
            num1_Mayor = 2
        else:
            num1_Mayor = 3
    return num1_Mayor

#Textos predeterminados
texto1=("El primer digito del numero indicado es mayor que el segundo.")
texto2=("El segundo digito del numero indicado es mayor que el primero.")
texto3=("Ambos digitos del numero indicado son iguales.")

#Funcion principal que ejecuta el programa
def main():
    numero = leerFloat("Ingrese un numero entero de 2 digitos: ")
    digito1 = calcularDigito1 (numero)
    digito2 = calcularDigito2 (numero)
    mayor = comparar_Numeros (digito1,digito2)
    imprimirMensajeDesicion (mayor, texto1, texto2, texto3)

main()