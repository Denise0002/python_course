# lista=['a','e','i','o']

# for indice,valor in enumerate(lista):
#     if valor == 'i':
#         print(valor,indice)

# TEORICO

# lista=['a','e','i','o']

# for indice,_ in enumerate(lista):
#     if _ == 'i':
#         print(indice)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def obtener_numeros_pares(lista):
#     numeros_pares = []
#     for numero in lista:
#         if numero % 2 == 0:
#             numeros_pares.append(numero)
#     return numeros_pares

# lista_resultado = obtener_numeros_pares(lista)
# print(lista_resultado)

# FORMA RAPIDA DE CODIGO
 
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for _,num in enumerate(lista):
#     if num%2==0:
#         print(num) 

# PROFESOR

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def numeros_pares(lista):
#     nueva_lista =[]
#     for _,num in enumerate(lista):
#         if num%2==0:
#             nueva_lista.append(num)
#     return nueva_lista
# print(numeros_pares(lista))

# texto='hola'
# print(lista(texto))
# print(texto.split(''))

def contar_vocales(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    for letra in texto:
        if letra.lower() in vocales:
            contador += 1
    return contador

texto = input("Ingresa un texto: ")
cantidad_vocales = contar_vocales(texto)
print("El texto tiene", cantidad_vocales, "vocales.")