"""
    Construya un algoritmo que, dada la cantidad de vendedores
    de una empresa, pregunte por cada uno el número de ventas
    que realizó y el total de dinero recaudado producto de esas
    ventas y calcule el promedio de ventas de cada uno de ellos
    y el promedio general de ventas de la empresa.

    Entradas:
        Número de empleados
        Número de ventas por empleado
        Dinero recaudado por empleado
    Salidas:
        Promedio por empleados
        Promedio de la empresa
    Procesos:
        Calcular el promedio de ventas de un empleado, n veces.
        Sumar todos los promedios.
    Funciones:
        def imprimirTexto(mensaje): Imprime un mensaje.
        def leerInt(mensaje): Lee un entero.
        def imprimirPromedio(n): Calcula promedios.
        def main(): Ejecuta el programa.
    Variables:

"""

from funciones import leerInt, imprimirTexto

def imprimirPromedio(n): #Imprime los promedios requeridos
    numEmpleado=1
    contadorEmpleados=0
    promedioEmpleado=0
    sumaDinero=0
    sumaVentas=0
    promedioEmpresa=0

    while contadorEmpleados < n:
        ventas=leerInt("Ingrese la cantidad de ventas del empleado "+str(numEmpleado)+": ")
        dinero=leerInt("Ingrese el dinero recaudado por el empleado "+str(numEmpleado)+": ")
        promedioEmpleado=dinero/ventas
        imprimirTexto("Su promedio por venta es: "+str(promedioEmpleado))
        sumaDinero+=dinero
        sumaVentas+=ventas

        contadorEmpleados+=1
        numEmpleado+=1
    
    promedioEmpresa=sumaDinero/sumaVentas
    imprimirTexto("El promedio por ventas de la empresa es: "+str(promedioEmpresa))

def main():
    n=leerInt("Ingrese el número de empleados: ")
    imprimirPromedio(n)

main()