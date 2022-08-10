"""
    Cree un programa que calcule la probabilidad de que n bebes compartan el mismo cumpleaños,
    si dicha probabilidad es el resultado de (364!) / ((365-n)*(365**(n-1)).

    Entradas: Numero de bebes
    Salida: Probabilidad de que n bebes compartan el mismo cumpleaños
    Procesos:
        Definir n bebes.
        Calcular la probabilidad según la formula.
    Funciones:
        def imprimirTexto(mensaje): Imprime un mensaje.
        def leerInt(mensaje): Lee un entero.
        def calcularFactorial_n(n): Calcula n!
        def calcularProbabilidad(n): Calcula la probabilidad de n en una fórmula específica.
        def main(): Ejecuta el programa
    Variables:
        mensaje, valor, n, factorial_total, probabilidad, bebes
"""

#Función que imprime
def imprimirTexto(mensaje):
    print(mensaje)

#Función que lee enteros
def leerInt(mensaje):
    valor= int(input(mensaje))
    return valor

#Función que calcula un Factorial
def calcularFactorial_n(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

#Función que calcula una probabilidad en una fórmula específica
def calcularProbabilidad(n):
    probabilidad = (1- ( (calcularFactorial_n(365) ) / ( (calcularFactorial_n(365-n)) * (365**(n)) ) )) * 100
    return probabilidad
 
#Función principal que ejecuta el programa
def main():
    mensaje = "Ingrese la cantidad de bebes: "
    bebes = leerInt(mensaje)
    probabilidad = calcularProbabilidad(bebes)
    imprimirTexto ("La probabilidad de que entre un grupo de " + str(bebes) + " bebes, un individuo comparta su fecha de cunpleaños con otro, es de: "+str(round(probabilidad, 2))+"%")

main()