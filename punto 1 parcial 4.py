"""
    Diseñe un algoritmo que dado un vector de número enteros positivos de
    tamaño n, determine si el promedio de los números pares es mayor al
    promedio de los números impares. Valide la entrada de datos


    Entradas: un vector de tamaño n

    Salidas: una cadena que indique si el promedio de los numeros
        pares dentro del vector, es mayor al promedio de los numeros
        impares, o nó.
    
    Procesos:
        Leer la longitud del vector
        Leer un arreglo con la longitud anterior
        Validar la entrada de datos
        Obtener un arreglo con todos los Pares en el arreglo
        Obtener un arreglo con todos los Impares en el arreglo
        Promediar los Pares
        Promediar los Impares
        Comparar ambos promedios
    
    Funciones:
        validarEntrada: Esta función permite comprobar la
            validez del un valor ingresado.

        leerArreglo_Int: Esta función permite leer un arreglo
            de enteros comprobados.
        
        filtrarPares_Arreglo: Esta función permite crear un
            arreglo que contenga los numeros pares contenidos
            en un arreglo.
        
        filtrarImpares_Arreglo: Esta función permite crear un
            arreglo que contenga los numeros impares contenidos
            en un arreglo.
        
        calcularPromedio_Arreglo: Esta función permite calcular
            el promedio de un arreglo de enteros.
        
        indicar_ValorMayor: Esta función indica cual de 2
            valores es mayor, o si son iguales.
    
    Variables:
        entrada, validez, longitud, arreglo, i, valido,
        arregloPar, cont, arregloImpar, suma, valor1, valor2,
        longitudVector, vector, pares, impares, promedioPares,
        promedioImpares.
"""

from funciones import imprimirTexto, leerInt

#Función que valida un valor. Retorna un Bool para indicar si cumple con los parámetros.
def validarEntrada(entrada): 
	try:
		validez = int(entrada)
	except ValueError:
		return False 
	return validez >= 0

#Función que lee un arreglo de longitud n de enteros vaidados. Retorna un arreglo de longitud n.
def leerArreglo_Int(longitud): 
    arreglo=[0]*longitud
    for i in range(longitud):
        valido=False
        while not valido: #Si valido es False, el ciclo continua
            entrada=input("Ingrese un numero: ")
            if validarEntrada(entrada):
                arreglo[i]=entrada
                valido=True
            else:
                imprimirTexto("No es un valor valido")
    return arreglo

#Función que filtra los pares dentro de un arreglo, y los organiza en otro arreglo. Retorna los pares en un nuevo arreglo.
def filtrarPares_Arreglo(arreglo):
    arregloPar=[]
    cont=0
    for i in range (len(arreglo)): 
        if int(arreglo[i])%2==0:
            arregloPar.append(arreglo[i])
            cont+=1
    return arregloPar

#Función que filtra los impares dentro de un arreglo, y los organiza en otro arreglo. Retorna los impares en un nuevo arreglo.
def filtrarImpares_Arreglo(arreglo):
    arregloImpar=[]
    cont=0
    for i in range (len(arreglo)):
        if int(arreglo[i])%2!=0:
            arregloImpar.append(arreglo[i])
            cont+=1
    return arregloImpar

#Función que calcula el promedio de los numeros en un arreglo. Retorna el promedio.
def calcularPromedio_Arreglo(arreglo):
    suma=0
    for i in range(len(arreglo)):
        suma+=int(arreglo[i])
    return suma/(len(arreglo))

 #Función que indica cual es el mayor de 2 valores. Imprime una cadena indicando que valor es mayor.
def indicar_ValorMayor(valor1, valor2):
    if valor1 > valor2:
        imprimirTexto("El promedio de numeros pares ("+"{0:.2f}".format(valor1)+"), es mayor al promedio de los numeros impares ("+"{0:.2f}".format(valor2)+")")
    else:
        if valor1 == valor2:
            imprimirTexto("El promedio de numeros pares es igual al promedio de numeros impares ("+"{0:.2f}".format(valor1)+")")
        else:
            imprimirTexto("El promedio de numeros impares ("+"{0:.2f}".format(valor2)+"), es mayor al promedio de los numeros pares ("+"{0:.2f}".format(valor1)+")")

#Función principal que ejecuta el programa
def main():
    longitudVector=leerInt("Ingrese la longitud del vector: ")
    vector=leerArreglo_Int(longitudVector)
    pares=filtrarPares_Arreglo(vector)
    impares=filtrarImpares_Arreglo(vector)
    promedioPares=calcularPromedio_Arreglo(pares)
    promedioImpares=calcularPromedio_Arreglo(impares)
    indicar_ValorMayor(promedioPares,promedioImpares)

main()