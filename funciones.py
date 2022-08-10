def leerFloat(mensaje): #Función que lee un flotante
    valor= float(input(mensaje))
    return valor

def leerInt(mensaje): #Función que lee un entero
    valor= int(input(mensaje))
    return valor

def leerStr(mensaje): #Función que lee un string
    valor= str(input(mensaje))
    return valor

def imprimirTexto (mensaje): #Función que imprime
    print(mensaje)

def calcularSuma (num1, num2): #Función que calcula una suma
    suma= num1 + num2
    return suma

def calcularResta (num1, num2): #Función que calcula una rsta
    resta= num1 - num2
    return resta

def calcularAreaCuadrado(lado1): #Función que calcula el área de un cuadrado
    areaCuadrado = lado1**2
    return areaCuadrado

def calcularAlturaTriangulo(lado2): #Función que calcula la altura de un triángulo 
    alturaTriangulo =((lado2**2)-((lado2/2)**2))**(1/2)
    return alturaTriangulo

def calcularAreaTriangulo(base, alturaTriangulo): #Función que calcula el área de un triángulo
    areaTriangulo=(base*alturaTriangulo)/2
    return areaTriangulo

"----------------------------------------Sección If----------------------------------------"

def imprimirMensajeDesicion (condicion, mensaje1, mensaje2): #Función que imprime 1 de 2 mensajes, dependiendo de un valor bool.
    if condicion == True:
        imprimirTexto(mensaje1)
    if condicion == False:
        imprimirTexto(mensaje2)

def definirParidad_Numero (num1): #Función que calcula la paridad de un número
    modulo=num1%2
    if modulo == 0:
        paridad=True
    else: paridad=False
    return paridad

def clasificarMayor(num1, num2): #Función que obtiene el mayor de 2 números
    numMayor=0
    if num1 > num2:
        numMayor = num1
    else:
        numMayor = num2
    return numMayor

def clasificarMenor(num1, num2): #Función que obtiene el menor de 2 números
    numMenor=0
    if num1 < num2:
        numMenor = num1
    else:
        numMenor = num2
    return numMenor

def calcularValorAbsoluto(n): #Función que calcula el valor absuluto
    valorAbsoluto = n
    m=1-2
    if n < 0:
        valorAbsoluto = n*m
    return valorAbsoluto

"----------------------------------------Sección While----------------------------------------"

def calcularMultiplos(mayor, menor, factor): #Función que imprime múltiplos de factor n en un intervalo
    while mayor>=menor:
        if menor%factor==0:
            imprimirTexto(menor)
            menor+=1

def calcular_CantDigitos(n): #Función que calcula la cantidad de dígitos de un número
    contador = 1
    while (n//10) >= 1:
        n=n//10 
        contador += 1
    return contador

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
        imprimirTexto("--------------------------")

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

def serieFibonacci(n): #Función que imprime el n termino de la secuencia fibonacci (omitiendo el 0 como primier termino)
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

def definirNumeroPerfecto(n): #Función que define si un número es perfecto o no
    m = n-1
    acumulador = 0
    while m > 0:
        if n%m == 0:
            acumulador+=m
            m-=1
    return n==acumulador

def imprimirNumerosPerfectos(n): #Función que imprime los números perfectos entre 1 y n
    imprimirTexto("Los números perfectos entre 1 y " + str(n) + ", son: ")
    var = 1
    while var <= n:
        if definirNumeroPerfecto(var):
            imprimirTexto(var)
        var+=1

"----------------------------------------Sección For----------------------------------------"

def multiplicar(n): #Función que calcula n!
    producto=1
    for i in range(1,(n+1)):
        producto = producto*i
    return producto

def sumar(n): #Función que calcula la suma de los enteros entre 10 y n, donde n es mayor a 10
    suma=0
    for i in range(10,(n+1)):
        suma+=i
    return suma

def sumarCuadrados(n, m): #Función que calcula la suma de los cuadrados entre n y m
    suma=0
    for i in range(n,(m+1)):
        suma+=(i**2)
    return suma

"----------------------------------------Sección Arreglos----------------------------------------"

def leerArreglo_Int(longitud, mensaje): #Función que lee un arreglo de longitud n de enteros
    arreglo=[0]*longitud
    for i in range(longitud):
        arreglo[i]=leerInt(mensaje) #Mensaje que solicita el entero
    return arreglo

def leerArreglo_Str(longitud, mensaje): #Función que lee un arreglo de longitud n de cadenas
    arreglo=['']*longitud
    for i in range(longitud):
        arreglo[i]=leerInt(mensaje) #Mensaje que solicita el entero
    return arreglo

def leerArreglo_Bool(longitud, mensaje): #Función que lee un arreglo de Booleanos.
    respuestasBool=[False]*longitud
    for i in range (longitud):
        respuesta=leerStr(mensaje).upper()
        if respuesta=="SI":                    
            respuestasBool[i]=True
        else:
            continue
    return respuestasBool #Retorno de un arreglo Bool

def recorrerArreglo_Indice(arreglo): #Función que recorre un arreglo obteniendo el indice
    for indice in range(len(arreglo)):
       print(arreglo[indice])
      
def recorrerArreglo_Elemento(arreglo): #Función que recorre un arreglo obteniendo el elemento
    for elemento in arreglo:
       print(elemento)

def calcularPromedio_condicionArreglo(arreglo, condicion): #Función que calcula el promedio de los elementos dentro de un arreglo, que cumplen con una condicion
    promedio = 0
    for i in range(arreglo):
        if i == condicion: #Conficion filtro
            promedio+=i
    promedio = promedio/len(arreglo)
    return promedio

def calcularPorcentaje_Arreglo(arreglo, condicion): #Función que calcula el porcentaje de elementos dentro de un arreglo, que cumplen con una condicion
    porcentaje = 0
    for i in range(arreglo):
        if i == condicion: #Condición filtro
            porcentaje+=1
    porcentaje = porcentaje/len(arreglo)*100
    return porcentaje

def invertirArreglo(arreglo): #Funcion que invierte un arreglo de enteros
    contador = len(arreglo)
    inversion = [' ']*contador
    for i in range (len(arreglo)):
        inversion[contador-1]=arreglo[i]
        contador-=1
    return inversion

def definirPrimo(n): #Funcion que define si un numero es primo
    primo=False
    for n in range(2, n):
        if n % n == 0:
            primo=False
        else:
            primo=True
    return primo

def definirCant_Par(arreglo, longitud): #Función que define la cantidad de pares en un arreglo de enteros
    cantPar=0
    for i in range (longitud): #Ciclo que recorre el arreglo y devuelve la cantidad de Pares
        if (arreglo[i])%2==0: #Filtro
            cantPar+=1
    return cantPar #Retorno de la cantidad de Pares

def definirCant_Impar(arreglo, longitud): #Función que define la cantidad de impares en un arreglo de enteros
    cantImpar=0
    for i in range (longitud): #Ciclo que recorre el arreglo y devuelve la cantidad de Impares
        if (arreglo[i])%2!=0: #Filtro
            cantImpar+=1
    return cantImpar #Retorno de la cantidad de Impares

def filtrarPares_Arreglo(arreglo): #Función que filtra los pares dentro de un arreglo, y los organiza en otro arreglo
    arregloPar=[]
    cont=0
    for i in range (len(arreglo)): #Ciclo que recorre el arreglo
        if arreglo[i]%2==0: #Condición
            arregloPar.append(arreglo[i]) #Se añaden al nuevo arreglo aquellos valores que cumplan con la condición
            cont+=1
    return arregloPar #Retorno del nuevo arreglo

def filtrarImpares_Arreglo(arreglo): #Función que filtra los impares dentro de un arreglo, y los organiza en otro arreglo
    arregloImpar=[]
    cont=0
    for i in range (len(arreglo)): #Ciclo que recorre el arreglo
        if arreglo[i]%2!=0: #Condición
            arregloImpar.append(arreglo[i]) #Se añaden al nuevo arreglo aquellos valores que cumplan con la condición
            cont+=1
    return arregloImpar #Retorno del nuevo arreglo

def calcularPromedio_Arreglo(arreglo): #Función que calcula el promedio de los numeros en un arreglo
    suma=0
    for i in range(len(arreglo)): #Ciclo que calcula la suma de los numeros en un arreglo
        suma+=int(arreglo[i])
    return suma/(len(arreglo)) #Retorno del promedio de los numeros en un arreglo