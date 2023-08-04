# Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos. Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)  con el alfabeto y los números en "leet". (Usa la primera opción de cada transformación solo para reemplazar vocales: Por ejemplo "4" para la "a")
#ejemplo
#entrada==>eucalipto
#salida==>3(_)c4l1pt0

def leet_converter(text):
    leet_table = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        'u': '(_)',
    }
    leet_text = ''
    for char in text:
        if char.lower() in leet_table:
            leet_text += leet_table[char.lower()]
        else:
            leet_text += char
    return leet_text

texto_entrada = input("Ingrese el texto: ")
texto_salida = leet_converter(texto_entrada)
print("lenguaje hacker: ", texto_salida)