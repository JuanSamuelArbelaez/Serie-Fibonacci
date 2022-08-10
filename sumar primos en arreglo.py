from funciones import leerInt, imprimirTexto, leerArreglo_Int

def sumarPrimos_Arreglo(arreglo):
    suma=0
    for indice in range(2, len(arreglo)):
        if definirPrimo(arreglo[indice]):
            suma+=arreglo[indice]
    return suma

def definirPrimo(n): #Funcion que define si un numero es primo
    primo=False
    for n in range(2, n):
        if n % n == 0:
            primo=False
        else:
            primo=True
    return primo

def main():
    longitud = leerInt("Ingrese la longitud de su arreglo: ")
    arreglo = leerArreglo_Int(longitud, ("Ingrese un numero: "))
    suma=sumarPrimos_Arreglo(arreglo)
    imprimirTexto("La suma de los numeros primos en el arreglo, es: "+str(suma))

main()