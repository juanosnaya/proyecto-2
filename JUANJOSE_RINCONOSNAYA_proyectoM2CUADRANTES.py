#bucle para que el usuario pueda encontrar tantos puntos quiera
while True:
    #Titulo, nombre del programa
    print("Coordenadas de un punto en un plano cartesiano")
    #Pedimos al usuario poner coordenadas
    x = float (input ("Ingresa el valor de x: "))
    y = float (input ("Ingresa el valor de y: "))
        # Verificamos que ninguna coordenada sea 0
    if x == 0 or y == 0:
        print ("Las coordenadas no pueden ser 0.")

        # Determinamos el cuadrante en base a los valores de x e y
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III.")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV.")

