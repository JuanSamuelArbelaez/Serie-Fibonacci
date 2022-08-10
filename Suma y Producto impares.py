from funciones import leerInt, imprimirTexto

def multiplicarImpares(n,m): #Función que calcula el producto de los impares entre n y m
    producto=1
    for i in range(n,(m+1)):
        if (i%2)!=0:
            producto=producto*i
    return producto

def sumarImpares(n,m): #Función que calcula la suma de los impares entre n y m
    suma=0
    for i in range(n,(m+1)):
        if (i%2)!=0:
            suma+=i
    return suma

def main():
    n=leerInt("Ingrese un número: ")
    m=leerInt("Ingrese un segundo número: ")
    suma=sumarImpares(n,m)
    producto=multiplicarImpares(n, m)
    print("La suma de los impares entre n y m es:", suma)
    print("El producto de los impares entre n y m es:", producto)

main()