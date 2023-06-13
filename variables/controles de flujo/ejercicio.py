player1 = input("Jugador 1, ¿qué eliges? Piedra, papel o tijera: ")
player2 = input("Jugador 2, ¿qué eliges? Piedra, papel o tijera: ")

if player1 == player2:
    print("Empate")
elif player1 == "piedra":
    if player2 == "tijera":
        print("Jugador 1 gana")
    else:
        print("Jugador 2 gana")
elif player1 == "papel":
    if player2 == "piedra":
        print("Jugador 1 gana")
    else:
        print("Jugador 2 gana")
elif player1 == "tijera":
    if player2 == "papel":
        print("Jugador 1 gana")
    else:
        print("Jugador 2 gana")
else:
    print("Entrada inválida. Por favor ingresa piedra, papel o tijera.")