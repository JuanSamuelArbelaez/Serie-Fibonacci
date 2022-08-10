"""
    Crea un programa que dado un número entero positivo e impar,
    valide que se ingrese un numero correcto, imprima un triángulo
    donde el primer carácter de cada línea es el número de la fila
    y los demás representan el número de la columna.

    Entradas: n
    Salidas:
        Un triangulo donde el primer carácter de cada línea sea
        el número de la fila, y los demás el número de la columna.
    Procesos:
        definir la imparidad de n.
        imprimir el triangulo con las caracteristicas dadas.
    Funciones:
        def imprimirTexto(mensaje): Imprime un mensaje.
        def leerInt(mensaje): Lee un entero.
        def triangulo(n):
            Imprime una piramide con caracteristicas específicas,
            si n cumple con ciertas condiciones.
        def main(): Ejecuta el programa.
    Variables:
        n, modulo, fila, contador, linea
"""

from funciones import leerInt, imprimirTexto

def triangulo(n): #Función que imprime una piramide, donde el primer carácter de cada línea es el número de la fila y los demás representan el número de la columna.
    modulo=n%2
    if n > 0 and modulo !=0: #Filtro de condición que valida que n sea impar y mayor a 0
        m=2
        imprimirTexto(1) #Impresión de la punta de la piramide
        fila=1
        while m <= n: #Impresión de la piramide del nivel 2 en adelante
            contador = 2
            linea=" "
            fila+=1
            while contador <= m:
                linea+=str(contador) + " "
                contador+=1
            imprimirTexto(str(fila)+linea)
            m+=1
    else:
        imprimirTexto("Debe ingresar un número entero, impar, y mayor a 0")

def main():
    n=leerInt("Ingrese un número entero, impar, y mayor a 0: ")
    triangulo(n)

main()