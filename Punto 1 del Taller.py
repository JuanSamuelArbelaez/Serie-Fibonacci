#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#funcion que calcula un promedio de 3 notas
def calcularPromedio(nota1, nota2, nota3):
    promedio=(nota1+nota2+nota3)/3
    return promedio

#Funcion principal que ejecuta el programa
def main():
    nota1=leerFloat("ingrese el valor de la nota 1: ")
    nota2=leerFloat("ingrese el valor de la nota 2: ")
    nota3=leerFloat("ingrese el valor de la nota 3: ")
    promedioNotas=calcularPromedio(nota1,nota2,nota3)
    imprimirTexto("su promedio es "+str(promedioNotas))

main()