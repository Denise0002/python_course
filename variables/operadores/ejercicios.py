DNI = input("ingresa tu DNI:")

if len(DNI) == 8:
    nombres = imput("Ingresa sus datos: ")
    print("tu DNI es :", DNI)
    print("tus nombres son:",nombres)
else:
    print("error: el DNI debe tener una longitud de 8 caracteres:")