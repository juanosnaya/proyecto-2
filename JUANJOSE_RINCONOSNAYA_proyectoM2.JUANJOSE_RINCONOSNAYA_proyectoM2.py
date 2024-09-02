def longitud_palabra():
    #Aqui hacemos un buckle infinito para que el usuario pueda seguir ingresando palabras hasta que ponga una correcta
    while True:
        #Pedimos al usuario ingresar una palabra con la longitud deseada
        palabra = input("Por favor, ingrese una palabra entre 4 y 8 caracteres:")
        longitud = len(palabra)

        if 4 <= longitud <=8:
            print("La palabra es correcta.")
            #break sirve para salir del bucle si la palabra es correcta
            break
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras")
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")

longitud_palabra()