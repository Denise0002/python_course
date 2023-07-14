frutas=[]
while len(frutas)<5:
    nuevaFruta=input('ingresa una fruta: ')
    for fruta in frutas:
        if len(nuevaFruta) == len(fruta):
            print('misma longitud / ingresa otro')
            continue
    if nuevaFruta in frutas:
        print('Esta fruta ya existe / ingrese otra fruta: ')
    else:
        frutas.append(nuevaFruta)

def textoLargo(array):
    longitudTexto=0
    mostrarFruta=''
    for index in range(0,len(array)):
        if len(array[index]) > longitudTexto:
            longitudTexto=len(array[index])
            mostrarFruta=array[index]
            print
    return mostrarFruta

