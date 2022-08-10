#Punto 3 del Taller

#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#funcion que calcular el valor de un viaje basado en kilometros
def calcularPrecio(kilometros):
    precio = kilometros * 10000
    return precio

#funcion principal que ejecute el programa
def main():
    kilometros= leerFloat("Ingrese la distancia en kilometros del viaje: ")
    precio = calcularPrecio(kilometros)
    imprimirTexto("El precio de su Boleto es: "+str(precio))

main()