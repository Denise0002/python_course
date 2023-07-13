# lista=[]

# for i in range(5):
#    palabra = input("ingresa una palabra: ")
#    lista.append(palabra)
# for indice, palabra in enumerate(lista):
#    if palabra == "disco":
#        print("disco, indice: ", indice)

import mensajes
lista=[]
indice=0
palabra=''
while len(lista)<5:
    dato=input("ingresa dato:")
    lista.append(dato)
for texto in range(0,len(lista)):
    if lista[texto] == 'disco':
        palabra=lista[texto]
        indice=texto
if indice==0 and palabra=='':
    print(mensajes.error('La palbra que buscas NO existe'))
else:
    print(mensajes.correcto(palabra,indice))
