#Entradas

def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor
def imprimirTexto(mensaje):
     print(mensaje)
def calcularAreaTriangulo(base, altura):
    area=(base*altura)/2
    return area
def main():
    baseTriangulo=leerFloat("ingrese el valor de la base: ")
    alturaTriangulo= leerFloat("Ingrese la altura: ")
    areaTriangulo=calcularAreaTriangulo(baseTriangulo,alturaTriangulo)
    imprimirTexto("el area del traingulo es "+str(areaTriangulo))
if __name__ == '__main__':
    main()


#Funcion 1 calcular x
def calcularVar(var1):
    valor=var1+10
    return valor

