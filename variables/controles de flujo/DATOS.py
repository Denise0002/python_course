#lista=[]
#print(lista)
#primerDato=input('ingresa una fruta: ')
#lista.append(primerDato)
#print(lista)
#segundoDato=input('ingresa una segunda fruta: ')
#lista.append(segundoDato)
#print(lista)
#lista = []
#while True:
    #entrada = input("Ingresa un dato o escribe/'si' para terminar: ")
 #   if entrada == "si":
 #       break
 #   lista.append(entrada)

#print("Datos ingresados:")
#for dato in lista:
 #   print(dato)

lista=[]
condicion=1
while condicion:
    pedirDato=input('ingrese un dato: ')
    if pedirDato == 'si':
        condicion=0
    lista.append(pedirDato)
print(lista)