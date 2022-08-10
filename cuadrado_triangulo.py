#funcion que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#funcion que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#funciones que permiten realizar operaciones matemáticas
def calcularAreaCuadrado(lado1):
    areaCuadrado = lado1**2
    return areaCuadrado

def calcularAlturaTriangulo(lado2):
    alturaTriangulo =((lado2**2)-((lado2/2)**2))**(1/2)
    return alturaTriangulo

def calcularAreaTriangulo(base, alturaTriangulo):
    areaTriangulo=(base*alturaTriangulo)/2
    return areaTriangulo

def calcularAreaTotal(areaCuadrado, areaTriangulo):
    areaTotal=areaCuadrado+areaTriangulo
    return areaTotal

def calcularPerimetroCuadrado(lado1):
    perimetroCuadrado = lado1 *4
    return perimetroCuadrado

def calcularPerimetroTriangulo(lado2):
    perimetroTriangulo = lado2 *3
    return perimetroTriangulo

def calcularPerimetroTotal(lado1, lado2):
    primetroTotal=(lado1*3)+(lado2*2)
    return primetroTotal

#Funcion principal que ejecuta el programa
def main():
    lado1=leerFloat("Ingrese el valor de lado 1: ")
    lado2=leerFloat("Ingrese el valor de lado 2: ")
    areaCuadrado=calcularAreaCuadrado(lado1)
    alturaTriangulo=calcularAlturaTriangulo(lado2)
    areaTriangulo=calcularAreaTriangulo(lado1, alturaTriangulo)
    areaTotal=calcularAreaTotal(areaCuadrado+areaTriangulo)
    perimetroCuadrado=calcularPerimetroCuadrado(lado1)
    perimetroTriangulo=calcularPerimetroTriangulo(lado2)
    perimetroTotal=calcularPerimetroTotal(lado1, lado2)
    imprimirTexto ("El area del cuadrado es: "+str(areaCuadrado))
    imprimirTexto ("La altura del triangulo es: "+str(alturaTriangulo))
    imprimirTexto ("El area del triangulo es : "+str(areaTriangulo))
    imprimirTexto ("El area total es: "+str(areaTotal))
    imprimirTexto ("El perimetro del cuadrado es: "+str(perimetroCuadrado))
    imprimirTexto ("El perimetro del triangulo es: "+str(perimetroTriangulo))
    imprimirTexto ("El perimetro total es: "+str(perimetroTotal))
 
main()