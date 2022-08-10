#Punto 3 del Taller

#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#funcion que permite calcular un valor a partir de un porcentaje
def calcularPrecioNuevo(precioActual, porcentaje):
    precioNuevo = precioActual + (precioActual*(porcentaje/100))
    return precioNuevo

#funcion principal que ejecute el programa
def main():
    precioActual = leerFloat("Ingrese el valor actual del producto: ")
    porcentaje = leerFloat("Ingrese el porcentaje deseado: ")
    precioNuevo = calcularPrecioNuevo(precioActual,porcentaje)
    imprimirTexto("El nuevo precio del producto es "+str(precioNuevo))

main()