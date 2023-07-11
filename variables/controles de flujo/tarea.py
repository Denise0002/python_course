# lista=[]

#for i in range(5):
   # palabra = input("ingresa una palabra: ")
#    lista.append(palabra)
#for indice, palabra in enumerate(lista):
#    if palabra == "disco":
 #       print("disco, indice: ", indice)

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
print('el texto disco se encuentre en el indice', indice)