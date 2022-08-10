"""
    La empresa “Panela S.A.” lo contrata para crear un algoritmo que determine el
    valor a pagar por un cliente. El valor depende de: el tipo de panela: Estándar,
    Premium, Importada; y la cantidad de panelas.

    Para el tipo Estándar, se paga $5000 por cada par de panelas y $3000 por una
    panela adicional. Para el tipo Premium se para $10000 por cada par y $6000 por
    una panela adicional y finalmente para el tipo Importada se paga $7000 por cada
    par y $4000 por cada panela adicional.

    La empresa ofrece adicionalmente un descuento del 5% del total de la venta si
    el cliente lleva más de 20 panelas. El aplicativo debe mostrar el valor del
    descuento y el valor total que debe pagar el cliente.

    Entradas: Tipo de panela, cantidad de panelas.
    Salidas: Valor a pagar, y descuento (si aplica).
    Procesos:
        Determinar el tipo de panela.
        Determinar si la cantidad es par o no.
        Determinar si se llevan más de 20 panelas.
        Determinar el descuento (si aplica).
        Determinar el precio a pagar.
    Variables:
        valor, condicion, paridad, tipoPanela, panelaPar, cantidadPanela, descuento,
        precio, precioFinal.
    Funciones:
        calcularParidad(num): Permite definir la paridad de un número.
        
        determinarPrecio(tipoPanela, panelaPar, cantidadPanela): Permite determinar
        cuanto es el valor neto a pagar, dependiendo el tipo de panela, y el sistema
        de precio por unidades.

        determinarDescuento(precio, cantidadPanela): Permite determinar el descuento,
        dependiendo de la condición.

        determinarPrecioFinal(precio, descuento): Permite determinar el precio final.
"""

#Funciones básicas
def leerFloat(mensaje):
    valor= float(input(mensaje))
    return valor

def leerString(mensaje):
    valor= str(input(mensaje))
    return valor.upper()

def imprimirTexto(mensaje):
    print(mensaje)

#Funcion que determina si la cantidad es par
def calcularParidad(num):
    modulo=num%2
    if modulo == 0:
        paridad=True
    else:
        paridad=False
    return paridad

#Funciones que determinan el precio
def determinarPrecio(tipoPanela, panelaPar, cantidadPanela):
    precio=0
    if tipoPanela == "ESTÁNDAR" or tipoPanela == "ESTANDAR":
        if panelaPar == True:
            precio = (cantidadPanela/2) * 5000
        else:
            precio = ((cantidadPanela - 1)/2 * 5000) + 3000
    else:
        if tipoPanela == "PREMIUM":
            if panelaPar == True:
                precio = cantidadPanela/2 * 10000
            else:
                precio = ((cantidadPanela - 1)/2 * 10000) + 6000
        else:
            if panelaPar == True:
                precio = cantidadPanela/2 * 7000
            else:
                precio = ((cantidadPanela - 1)/2 * 7000) + 4000
    return precio

def determinarDescuento(precio, cantidadPanela):
    if cantidadPanela > 20:
        descuento = precio * 0.05
    else:
        descuento = 0
    return descuento

def determinarPrecioFinal(precio, descuento):
    precioFinal = precio - descuento
    return precioFinal

#Funcion principal
def main ():
    tipoPanela = leerString("Ingrese el tipo de panela que desea comprar: ")
    cantidadPanela = leerFloat("Ingrese la cantidad de panelas que desea comprar: ")
    panelaPar = calcularParidad(cantidadPanela)
    precio = determinarPrecio(tipoPanela, panelaPar, cantidadPanela)
    descuento = determinarDescuento(precio, cantidadPanela)
    precioFinal = determinarPrecioFinal(precio, descuento)
    imprimirTexto("El precio neto de la compra es: "+str(precio)+" , con un descuento de: "+str(descuento)+", para un total de: "+str(precioFinal))

main()