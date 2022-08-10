
def leer_int (mensaje):
    x = int(input(mensaje))
    return x


def convertir_binario_a_decimal(numero):
    posicion = 0
    total_decimal = 0
    while numero > 0:

        valor = numero % 10   #ESTA LINEA VERIFICA EL VALOR DEL PRIMER DIGITO (DE DERECHA A IZQUIERDA)
        posicion += 1
        numero / 10

        if  valor == 1:
            total_decimal = total_decimal + 2**(posicion)
            posicion += 1
        else:
            valor == 0
            posicion +=  1

    return total_decimal


def main():
    x = leer_int("Ingrese un número  ")
    decimal=(convertir_binario_a_decimal(x))
    print(decimal)

main()