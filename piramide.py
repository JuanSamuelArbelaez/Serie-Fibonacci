from funciones import imprimirTexto, leerInt

def triangulo(n): #Función que imprime una piramide de 1 a n
    m=1
    while m <= n:
        contador = 1
        linea=" "
        while contador <= m:
            linea+=str(m) + " "
            contador+=1
        imprimirTexto(linea)
        m+=1

def main():
    n=leerInt("Ingrese un número: ")
    triangulo(n)

main()