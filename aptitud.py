"""
    La oficina de incorporación del ejército necesita un algoritmo
    que le pueda permitir saber si un aspirante a ingresar a la
    institución como soldado es apto o no para poder vincularlo.

    Entrada: Genero, estatura, edad, y estado civil del Aspirante.
    Salida: Aptitud del Aspirante.
    Procesos:
        Definir si el aspirante es hombre o mujer.
        Definir si la estatura del aspirante.
        Definir la edad del Aspirante.
        Definir el esto civil del Aspirante.
        Definir la aptitud del Aspirante.
    Variables:
        valor, condicion, genero, estatura, edad, estado_civil,
        aptitud, texto1, texto2, texto3, texto4, texto5, texto6,
        aptitudAspirante.
"""

#Funciones básicas
def leerFloat(mensaje):
    valor= float(input(mensaje))
    return valor

def leerString(mensaje):
    valor= str(input(mensaje))
    return valor

def imprimirTexto(mensaje):
    print(mensaje)

def imprimirCondicionado(condicion, mensajeTrue, mensajeFalse):
    if condicion == True:
        imprimirTexto(mensajeTrue)
    else:
        imprimirTexto(mensajeFalse)

#Textos
texto1=("Indique si el Aspirante es de genero Femenino o Masculino: ")
texto2=("Indique la estatura en metros del Aspirante: ")
texto3=("Indique la edad en años del Aspirante: ")
texto4=("Indique si el Aspirante es soltero o no: ")
texto5=("El Aspirante es Apto para ingresar como Soladado.")
texto6=("El Aspirante no es Apto para ingresar como Soladado.")

#Funcion que define la aptitud del aspirante
def calcularAptitud (genero, estatura, edad, estado_civil):
    aptitud = False
    if genero == "Femenino" and estatura > 1.60 and edad >= 20 and edad <=25 and estado_civil == "Si":
        aptitud = True
    else:
        if genero == "Masculino:" and estatura > 1.65 and edad >= 18 and edad <=24 and estado_civil == "Si":
            aptitud = True
        else:
            aptitud = False
    return aptitud

#Funcion principal
def main():
    genero=leerString(texto1)
    estatura=leerFloat(texto2)
    edad=leerFloat(texto3)
    estado_civil=leerString(texto4)
    aptitudAspirante=calcularAptitud(genero, estatura, edad, estado_civil)
    imprimirCondicionado(aptitudAspirante, texto5, texto6)

main()
