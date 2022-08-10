from funciones import leerInt, imprimirTexto, leerArreglo_Int

def invertirArreglo(arreglo): #Funcion que invierte un arreglo de enteros
    contador = len(arreglo)
    inversion = [' ']*contador
    for i in range (len(arreglo)):
        inversion[contador-1]=arreglo[i]
        contador-=1
    return inversion

def main():
    longitud = leerInt("Ingrese la longitud de su arreglo: ")
    arreglo = leerArreglo_Int(longitud, ("Ingrese un numero: "))
    inversion=invertirArreglo(arreglo)
    imprimirTexto(inversion)

main()