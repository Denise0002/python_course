# Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres. La función debe encontrarlos y retornarlos en formato lista/array. Ambas cadenas de texto deben ser iguales en longitud.
#Las cadenas de texto son iguales elemento a elemento.
#No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente. Ejemplos:Me llamo jose / Me llemo jese -> ["e", "o"]
#hola como estas / holi come estus -> ["i", "e", "u"]


def encontrar_caracteres_diferentes(cadena1, cadena2):
    caracteres_diferentes = []
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            caracteres_diferentes.append(cadena2[i])
    return caracteres_diferentes

