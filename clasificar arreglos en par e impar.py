from funciones import imprimirTexto, leerInt #Importación de funciones clave

def leerArreglo_Int(longitud, mensaje): #Función que lee un arreglo de longitud n de enteros
    arreglo=[0]*longitud
    for i in range(longitud):
        arreglo[i]=leerInt(mensaje) #Mensaje que solicita el entero
    return arreglo
            
def filtrarImpares_Arreglo(arreglo): #Función que filtra los impares dentro de un arreglo, y los organiza en otro arreglo
    arregloImpar=[]
    cont=0
    for i in range (len(arreglo)): #Ciclo que recorre el arreglo
        if arreglo[i]%2!=0: #Condición
            arregloImpar.append(arreglo[i]) #Se añaden al nuevo arreglo aquellos valores que cumplan con la condición
            cont+=1
    return arregloImpar #Retorno del nuevo arreglo

def filtrarPares_Arreglo(arreglo): #Función que filtra los pares dentro de un arreglo, y los organiza en otro arreglo
    arregloPar=[]
    cont=0
    for i in range (len(arreglo)): #Ciclo que recorre el arreglo
        if arreglo[i]%2==0: #Condición
            arregloPar.append(arreglo[i]) #Se añaden al nuevo arreglo aquellos valores que cumplan con la condición
            cont+=1
    return arregloPar #Retorno del nuevo arreglo

def main():
    longitud=leerInt("Ingrese la longitud del arreglo: ")
    arreglo=leerArreglo_Int(longitud, "Ingrese el valor: ")
    arregloImpar=filtrarImpares_Arreglo(arreglo)
    arregloPar=filtrarPares_Arreglo(arreglo)
    imprimirTexto("El arreglo de numeros pares es: "+str(arregloPar))
    imprimirTexto("El arreglo de numeros impares es: "+str(arregloImpar))
main()