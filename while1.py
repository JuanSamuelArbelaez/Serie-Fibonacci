
def leerFloat(mensaje):
    valor= float(input(mensaje))
    return valor

def ciclos(num1, num2):
    x=0
    y=0
    x=num1
    y=num2
    while x <= y:
        print (str(x))
        x=x+1

def main():
    var1=leerFloat("Ingrese un número entre 1 y 10: ")
    var2=leerFloat("Ingrese un número entre 11 y 20: ")
    ciclos(var1, var2)
main()