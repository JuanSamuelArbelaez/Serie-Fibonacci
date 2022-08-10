"""
    Crear un programa que, dado un número entero, debe garantizar que sea mayor a
    cero, calcule el promedio de los números cuyo último digito sea 3. Por
    ejemplo, si el numero ingresado es 40 el algoritmo debería mostrar promedio
    de: 3, 13, 23, 33, ya que estos son los números cuyo último dígito termina
    en 3.

    Entradas: Un número entero mayor a 0.
    Salidas: El promedio de todos los números cuyo ultimo digito sea 3, entre 0 y n.
    Procesos:
        Definir si n es mayor a 0
        Calcular el promedio de todos los números entre 0 y n, cuyo último dígito sea 3.
    Funciones:
        def imprimirTexto(mensaje): Imprime un mensaje.
        def leerInt(mensaje): Lee un entero.
        def definir_nMayor0(n): Define si un número es mayor a 0.
        def imprimirMensajeDesicion(texto1, texto2): Imprime 1 de 2 textos, dependiendo
            de una condición.
        def calcularPromedio_CUSTOM(n, mayor): Calcula el promedio de los números entre 0 y n,
            que cumplan con cierto criterio
        def main(): Función que ejecuta el programa.
    Variables:
        n, mayor, suma, divisor, contador, promedio, texto1, texto2.
"""

from funciones import imprimirTexto, leerInt, imprimirMensajeDesicion

def definir_nMayor0(n): #Función que define si un número es mayor a 0
    mayor = False
    if n > 0:
        mayor = True
    else:
        mayor = False
    return mayor

def calcularPromedio_CUSTOM(n, mayor): #Función que calcula el promedio de los números entre 0 y n
    suma=0
    divisor=0
    contador=0
    promedio=0

    while contador <= n:
        if (contador%10)==3 and mayor: #Define si el último digito es 3
            suma+=contador
            divisor+=1
            contador+=1
        else:
            contador+=1
    
    if mayor:
        promedio=suma/divisor
    return promedio

def main(): #Función principal que ejecuta el programa
    n=leerInt("Ingrese un número entero mayor a 0: ")
    mayor=definir_nMayor0(n)
    promedio=calcularPromedio_CUSTOM(n, mayor)
    texto1=("El promedio de los números entre 0 y "+str(n)+", cuyo último dígito sea 3, es: ")
    texto2=("Debe ingresar un número mayor a 0")
    imprimirMensajeDesicion(mayor, texto1, texto2)
    imprimirTexto(promedio)

main()