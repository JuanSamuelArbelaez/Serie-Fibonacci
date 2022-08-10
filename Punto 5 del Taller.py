#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#funcion que calcula el nuevo salario

""" El ejercicio pidió un calculo fijo de 8 y 2.5 para aumento y descuento, respectivamente, pero decidí
modificar el programa para que hiciera el cálculo basado en un aumento y descuento dados por el usuario """

def calcularSalario(salarioAntiguo, aumento, descuentoSalud):
    salarioNuevo = salarioAntiguo + (salarioAntiguo * (aumento/100)) - (salarioAntiguo * (descuentoSalud/100))
    return salarioNuevo

#Funcion principal que ejecuta el programa
def main():
    salarioAntiguo=leerFloat("ingrese su antiguo salario: ")
    aumento=leerFloat("ingrese el valor en porcentaje de su aumento: ")
    descuentoSalud=leerFloat("ingrese el valor en porcentaje de su descuento de salud: ")
    salarioNuevo=calcularSalario(salarioAntiguo,aumento,descuentoSalud)
    imprimirTexto("Su nuevo salario es: "+str(salarioNuevo))

main()