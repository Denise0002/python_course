# Crea un programa que analice texto y obtenga:
#=>Número total de palabras (no espacios).
#=>Número de oraciones del texto (cada vez que aparecen una coma).
#=>Encuentre la palabra más larga. Todo esto utilizando un único bucle.

# Entrada=>"soy un texto escrito por pc, y hoy hace mucho frio"

#palabras=39
#oraciones=2
#texto largo=escrito

#texto = "soy un texto escrito por pc, y hoy hace mucho frio"

palabras = 0
oraciones = 0
textoLargo = ""

texto = input("Ingrese el texto: ")
for palabra in texto.split():
    palabras += 1
    if len(palabra) > len(textoLargo):
        textoLargo = palabra
oraciones = texto.count(',')

print("Número total de palabras:", palabras)
print("Número de oraciones:", oraciones)
print("Palabra más larga :", textoLargo)