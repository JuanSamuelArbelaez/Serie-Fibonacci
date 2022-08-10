import math

def leerFloat(mensaje):
    valor= float(input(mensaje))
    return valor

def imprimirTexto(mensaje):
    print(mensaje)

def calcularGrado(aceleracion, friccion):
    grado=math.degrees(math.asin(((((9.8)**(1/2))*(friccion**3))+(((9.8)**2)*(friccion**2))-(friccion*(aceleracion**2)))/(9.8*(friccion+1))))
    return grado

def main():
    acel=leerFloat("Ingrese la aceleración: ")
    fricc=leerFloat("Ingrese la friccion: ")
    grado=calcularGrado(acel, fricc)
    imprimirTexto(str(grado))

main()