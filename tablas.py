from funciones import imprimirTexto


def imprimirTablas(): #Función que imprime las tablas de multiplicar
    m=1
    num=1
    while num<=10:
        while m<=10:
            resultado=m*num
            imprimirTexto(str(m)+ " * " +str(num)+ " = " + str(resultado))
            m+=1
        num+=1
        m=1

def main():
    imprimirTablas()

main()
