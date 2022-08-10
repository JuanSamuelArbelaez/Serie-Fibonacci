#función que permite leer un dato real
def leerFloat(mensaje):
     valor= float(input(mensaje))
     return valor

#función que permite imprimir un texto
def imprimirTexto(mensaje):
     print(mensaje)

#función que permite calcular una ganacia mediantes un valor, su interes agregado, y un descuento
def calcularGanancia (monto, interes):
    ganancia =(monto*(interes/100)) - (monto*(interes/100)*0.003)
    return ganancia

#función que permite sumar 2 valores
def calcularSuma (num1, num2):
    suma=num1+num2
    return suma

#función principal que ejecuta el programa
def main():
    monto1_Inicial = leerFloat("Digite el valor del monto 1: ")
    interes1 = leerFloat("Digite el valor del interés anual del monto 1, en porcentaje: ")
    monto2_Inicial = leerFloat("Digite el valor del monto 2: ")
    interes2 = leerFloat("Digite el valor del interés anual del monto 2, en porcentaje: ")
    monto1_ganancia = calcularGanancia(monto1_Inicial, interes1)
    monto2_ganancia = calcularGanancia(monto2_Inicial, interes2)
    monto1_Final = calcularSuma (monto1_Inicial, monto1_ganancia)
    monto2_Final = calcularSuma (monto2_Inicial, monto2_ganancia)
    sumaMontos = calcularSuma(monto1_Final, monto2_Final)
    imprimirTexto("El valor de su monto 1, será de: " +str(monto1_Final)+ ", al pasar 1 año, con una ganancia de: " +str(monto1_ganancia)+ ",con respecto a su valor inical de: "+str(monto1_Inicial))
    imprimirTexto("El valor de su monto 2, será de: " +str(monto2_Final)+ ", al pasar 1 año, con una ganancia de: " +str(monto2_ganancia)+ ", con respecto a su valor inical de: "+str(monto2_Inicial))
    imprimirTexto("La suma de ambos montos será de: " +str(sumaMontos)+ ", al pasar 1 año.")

main()