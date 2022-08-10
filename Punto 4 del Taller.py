#Punto 4 del Taller

#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#funcion que permite calcular un valor a partir de un porcentaje
def calcularPrecioNuevo(precioActual):
    precioNuevo = precioActual - (precioActual*0.35)
    return precioNuevo

#funcion principal que ejecute el programa
def main():
    precioActual = leerFloat("Ingrese el valor actual del producto: ")
    precioNuevo = calcularPrecioNuevo(precioActual)
    imprimirTexto("Con un descuento del 35%, el precio de su producto es "+str(precioNuevo))

main()