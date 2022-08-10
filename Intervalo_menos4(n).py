"""
    Entrada: 2 números enteros.
    Salida: Intervalo ascendente entre ambos números, exeptuando los mútliplos de 4
    Funciones: 
        def imprimirTexto(mensaje): Imprime un mensaje.
        def leerInt(mensaje): Lee un entero.
        def clasificarMayor (num1, num2): Retorna el mayor de 2 números.
        def clasificarMenor (num1, num2): Retorna el menor de 2 números.
        def imprimirIntervalo(num1, num2): Imprime un intervalo.
        def main(): Ejecuta el programa
    Variables:
        mensaje, valor, num1, num2, numMayor, numMenor, numero1, numero2, modulo.
"""

#Función que imprime
def imprimirTexto(mensaje):
    print(mensaje)

#Función que lee enteros
def leerInt(mensaje):
    valor= int(input(mensaje))
    return valor

#Función que obtiene el mayor de 2 números
def clasificarMayor (num1, num2):
    numMayor=0
    if num1 > num2:
        numMayor = num1
    else:
        numMayor = num2
    return numMayor

#Función que obtiene el menor de 2 números
def clasificarMenor (num1, num2):
    numMenor=0
    if num1 < num2:
        numMenor = num1
    else:
        numMenor = num2
    return numMenor

#Función que imprime un intervalo, exeptuando los múltiplos de 4
def imprimirIntervalo(num1, num2):
    modulo=0
    while (num1<=num2):
        modulo=num1%4
        if modulo==0:
            num1+=1
            continue
        imprimirTexto(num1)
        num1+=1

#Fución principal que ejecuta el programa
def main():
    numero1=leerInt("Ingrese el primer número: ")
    numero2=leerInt("Ingrese el segundo número: ")
    numMayor=clasificarMayor(numero1, numero2)
    numMenor=clasificarMenor(numero1, numero2)
    imprimirIntervalo(numMenor,numMayor)

main()