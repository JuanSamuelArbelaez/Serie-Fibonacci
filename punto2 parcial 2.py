"""
    En la pastelería de la “Abuela” venden tortas para todos los gustos. Si la torta
    es entre 1 y 3 libras tiene un costo base de 35.000. Si es mayor a 3 lbs y menos
    de 10lbs, las 3 primeras libras tienen un costo de 35.000 y la libra adicional un
    costo de 10.000 por libra. Para 10 lbs o más, el costo de la libra adicional es
    de 8.000. Si la torta además debe ser decorada tiene un sobrecargo de 15.000.
    
    Construya un algoritmo que permita calcular el valor de la torta de acuerdo con las
    especificaciones del cliente quien deberá indicar la cantidad de libras, si es
    decorada o no, si es enviada o no y el sabor. Tenga en cuenta que si el costo de la
    torta supera los 50000 se le realizará un descuento del 5%.


    Entradas: Cantidad de Libras. Decoración. Envio. Sabor.
    Salidas: Precio a pagar. Especificaciones sobre decoración, envio y sabor.
    Procesos:
        Determinar el intervalo de libras al que pertenece.
        Determinar si tiene libras adicionales.
        Determinar si la torta debe ser decorada.
        Determinar descuento (si aplica).
        Determinar el precio a pagar.
    Variables:
        valor, condicion, descuento, cantidadLibras, decoracion, precio, descuento,
        precioFinal, envio, sabor.
    Funciones:
        determinarPrecio(cantLIbras, decoracion): Permite determinar cuanto es el valor
        neto a pagar, dependiendo el la cantidad de libras y la decoracion.

        determinarDescuento(precio): Permite determinar el descuento, dependiendo del precio.

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

#Funciones que determinan el precio
def determinarPrecio(cantLibras, decoracion):
    precio=0
    if cantLibras <= 3:
        if decoracion == "SI":
            precio = 50000
        else:
            precio = 35000
    else:
        if cantLibras > 3 and cantLibras< 10:
            if decoracion == "SI":
                precio = ((cantLibras-3)*10000)+50000
            else:
                precio = ((cantLibras-3)*10000)+35000
        else:
            if decoracion == "SI":
                precio = ((cantLibras-10)*8000)+50000
            else:
                precio = ((cantLibras-10)*8000)+35000
    return precio
    
def determinarDescuento(precio):
    if precio > 50000:
        descuento = precio * 0.05
    else:
        descuento = 0
    return descuento

def determinarPrecioFinal(precio, descuento):
    precioFinal = precio - descuento
    return precioFinal

#Funcion principal
def main():
    cantLibras = leerFloat ("Ingrese la cantidad de libras que desea comprar: ")
    sabor = leerString("Ingrese el sabor de la torta: ")
    decoracion = leerString("Ingrese si desea que su torta sea decorada, o no: ")
    envio = leerString("Ingrese si requiere envio o no: ")
    precio = determinarPrecio(cantLibras, decoracion)
    descuento = determinarDescuento(precio)
    precioFinal = determinarPrecioFinal(precio, descuento)
    imprimirTexto("El sabor de su torta es: "+str(sabor)+" . Requiere decoración: "+str(decoracion)+" . Requiere envio: "+str(envio)+" . Precio total: "+str(precioFinal))

main()