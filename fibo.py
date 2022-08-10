from funciones import imprimirTexto, leerInt

def serieFibonacci(n):
    contador=3
    fibo=1
    num1=1
    num2=1
    imprimirTexto(fibo)
    while contador<=n:
        imprimirTexto(fibo)
        fibo = num1 + num2
        num1 = num2
        num2 = fibo
        contador+= 1
    imprimirTexto(fibo)

def main():
    n=leerInt("Ingrese un número: ")
    serieFibonacci(n)
        
main()