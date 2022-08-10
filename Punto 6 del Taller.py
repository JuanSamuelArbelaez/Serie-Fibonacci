#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#función que calcula el área de un rectangulo
def calcularAreaRectangulo (lado1, lado2):
    areaRectangulo = lado1*lado2
    return areaRectangulo

#función que permite sumar 3 datos
def calcularSuma (num1, num2, num3):
    suma=num1+num2+num3
    return suma

#función que calcula la cantidad de cajas necesarias
def calcularCajas (areaCasa, areaCaja):
    cant=(areaCasa//areaCaja)+1
    return cant

#función que calcula el sobrante
def calcularSobrante (areaCasa, areaCaja, cantCajas):
    sobrante= cantCajas - (areaCasa/areaCaja)
    return sobrante

#función que principal ejecuta el programa
def main ():
    ladoEspacio1=leerFloat("Introduzca el valor del lado del espacio 1: ")
    alturaEspacio1=leerFloat("Introduzca el valor de la altura del espacio 1: ")
    ladoEspacio2=leerFloat("Introduzca el valor del lado del espacio 2: ")
    alturaEspacio2=leerFloat("Introduzca el valor de la altura del espacio 2: ")
    ladoEspacio3=leerFloat("Introduzca el valor del lado del espacio 3: ")
    alturaEspacio3=leerFloat("Introduzca el valor de la altura del espacio 3: ")
    areaCajas=leerFloat("Introduzca el área que puede cubrir cada caja: ")
    areaEspacio1=calcularAreaRectangulo(ladoEspacio1, alturaEspacio1)
    areaEspacio2=calcularAreaRectangulo(ladoEspacio2, alturaEspacio2)
    areaEspacio3=calcularAreaRectangulo(ladoEspacio3, alturaEspacio3)
    areaTotal=calcularSuma(areaEspacio1, areaEspacio2, areaEspacio3)
    cantCajas=calcularCajas(areaTotal, areaCajas)
    sobrante=calcularSobrante(areaTotal, areaCajas, cantCajas)
    imprimirTexto("La cantidad mínima de cajas de baldosas que requiere para cubrir todas las superficies, son "+str(cantCajas)+", con un sobrante de "+str(sobrante)+" cajas.")

main()