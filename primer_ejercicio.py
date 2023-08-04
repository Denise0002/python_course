# Crea una funciones, encargada de detectar si una cadena de texto es un heterograma.
#heterograma ==> frase que no contiene letra repetida ejem:centrifugado.

def es_heterograma(cadena):
    letras = []
    for letra in cadena:
        if letra.isalpha():
            if letra in letras:
                return False
            letras.append(letra)
    return True
    print(letras)