#tabalaDe=int(input('ingresa un numero: '))
#or numero in range(1,13): 




numero=int(input('ingrese un numero: '))
factorial=1
if numero == 0:
    print('el factorialde 0 es 0')
else:
    for num in range(1,numero+1):
        factorial=factorial*num
    print(factorial)