def crear_lista_objetos(lista):
    lista_objetos = []
    for posicion, elemento in enumerate(lista):
        objeto = {
            'longitud': len(elemento),
            'nombre': elemento,
            'posicion': posicion
        }
        lista_objetos.append(objeto)
    return lista_objetos

lista = ["bosque", "vih", "bonorrea"]
lista_objetos = crear_lista_objetos(lista)
print(lista_objetos)