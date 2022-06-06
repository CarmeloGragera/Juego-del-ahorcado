import time 

# Introduce el usuario lapalabra
palabra_adivinar = input("Introduzca la palabra a adivinar").upper()

# Transformamos la palabra a una lista de caracteres ocultos (_)
lista_caracteres_ocultos = []
for char in palabra_adivinar:
    lista_caracteres_ocultos.append('_')

# Inicializamos fallos
fallos = 0

while fallos <= 5: # Mientras nos queden fallos seguimos en el juego
    time.sleep(1)
    letra_usuario = input("Introduzca una letra").upper()  # Introduce el usuario la letra
    # Comprobamos si la letra se encuentra, buscamos en qué posicion se encuentra, y aquellos que coincidan, sustituiremos el valor de esa letra en su posicion
    if letra_usuario in palabra_adivinar:
        for pos, letra in enumerate(palabra_adivinar):
            if letra == letra_usuario:
                lista_caracteres_ocultos[pos] = letra_usuario
    # Actualizamos la variable fallos, si llegamos a 6 se parará el bucle y mostrará por pantalla game over
    else: 
        fallos = fallos + 1
        print("Has fallado, llevas " + str(fallos) + ' fallos')
        if fallos == 6:
            print("Game over")
    # En cada letra se muestra la palabra oculta con las letras acertadas
    print(' '.join(lista_caracteres_ocultos))

    # Si no encuentra letras por adivinar, has ganado
    if '_' not in lista_caracteres_ocultos:
        print("Well done")
        break