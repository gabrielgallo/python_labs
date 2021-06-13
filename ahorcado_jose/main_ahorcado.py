import random

from ahorcado_jose.funciones_ahorcado import busca_letra, busca_no_adivinadas, interaccion_usuario

if __name__ == "__main__":
    # diccionarios de palabras para jugar
    dict_palabras = {0:"natacion",
                     1:"murcielago",
                     2:"palabra",
                     3:"pandemia",
                     4:"manzana",
                     5:"tormenta",
                     6:"cordillera",
                     7:"mortadela",
                     8:"carniceria",
                     9:"poesia"}

    # diccionario de mensajes con datos variables
    # el caracter ~ debe ser reemplazado por el contenido de una variable
    linea_de_asteriscos = "*" * 44
    dic_msg = {1 : "\nAdivina cual es la palabra de ~ letras: ~",
               2 : "\nFijate bién!!!, ya intentaste con la letra: ~",
               3 : "Te faltan adivinar ~ letras: ~",
               4 : "\nNo acertaste con la letra: ~",
               5 : "\nBien!, acertaste con la letra: ~",
               6 : "Jugadas: ~, Aciertos: ~, Errores ~, ya intentaste con: ~",
               7 : linea_de_asteriscos,
               8 : "*     BIENVENIDO AL JUEGO DEL AHORCADO     *",
               9 : "*       FIN DEL JUEGO - HASTA LUEGO        *",
               10: "Ingresa una letra, '$' para salir: ",
               11: "GENIAL!!!!!, adivinaste la palabra!!!!",
               12: "Lo lamento, no lo lograste, estás ahorcado :)",
               13: "La palabra es: ~",
               14: "\nDigite Enter para intentarlo de nuevo, $ para Salir: "}

    # imprime el mensaje de bienvenida
    interaccion_usuario([dic_msg.get(7), 0])
    interaccion_usuario([dic_msg.get(8), 0])
    interaccion_usuario([dic_msg.get(7), 0])

    seguir = True
    while seguir:
        # Generar un numero aletorio para buscar una palabra en el diccionario de palabras
        ind_dict = int(random.random()*10)
        palabra = dict_palabras.get(ind_dict) # palabra seleccionada del diccionario para jugar
        cant_letras = len(palabra) # cantidad de letras de la palabra seleccionada
        incognita = "_" * cant_letras # palabra incognita para mostrarle al jugador

        interaccion_usuario([dic_msg.get(1), 2, [cant_letras, incognita]])
        jugadas = aciertos = errores = 0 # inicializa contadores
        intentos = list() # inicializa memoria de letras ingresadas por el jugador
        letra_ingresada = input(dic_msg.get(10)) # solicita que el jugador ingrese una letra
        if letra_ingresada == "$": # si ingresan $ entonces salir
            seguir = False

        while seguir:
            jugadas = jugadas + 1 # acumulador de jugadas realizadas
            if letra_ingresada in intentos: # verifica si la letra ingresada ya la habia ingresado antes
                interaccion_usuario([dic_msg.get(2), 1, [letra_ingresada]])
                interaccion_usuario([dic_msg.get(3), 2, [i, incognita]])
                letra_ingresada = input(dic_msg.get(10)) # solicita que el jugador ingrese nuevamente una letra
                if letra_ingresada == "$": # si ingresa $ salir
                    seguir = False
            else:
                intentos.append(letra_ingresada) # memoriza la letra ingresada por el jugador
                # si la letra ingresada está en la palabra que debe adivinar  entonces
                # la guardamos en una variable temporal
                temporal = busca_letra(palabra,letra_ingresada,incognita)
                # si la variable temporal es igual a la incógnita entonces
                # la letra ingresada no está en la palabra o sea es un error
                if temporal == incognita:
                    errores = errores + 1
                    interaccion_usuario([dic_msg.get(4), 1, [letra_ingresada]])
                else:
                    # si la variable temporal no es igual a la incógnita entonces
                    # la letra ingresada es acertada
                    aciertos = aciertos + 1
                    interaccion_usuario([dic_msg.get(5), 1, [letra_ingresada]])

                interaccion_usuario([dic_msg.get(6), 4, [jugadas, aciertos, errores, intentos]])
                incognita = temporal # pisamos la incógnita con el contenido de la temporal
                i = busca_no_adivinadas(incognita)
                if errores < 8: # con menos de 8 errores sigue jugando
                    if i > 0: # si todavía faltan letras por adivinar, solicita ingresar otra letra
                        interaccion_usuario([dic_msg.get(3), 2, [i, incognita]])
                        letra_ingresada = input(dic_msg.get(10))
                        if letra_ingresada == "$":
                            seguir = False
                    else:
                        interaccion_usuario([dic_msg.get(11), 0]) # fin del juego, el jugador ganó
                        interaccion_usuario([(incognita + "  ") * 5, 0])
                        letra_ingresada = input(dic_msg.get(14))
                        if letra_ingresada == "$":
                            seguir = False
                        break
                else:
                    interaccion_usuario([dic_msg.get(12), 0]) # game over, el jugador pedió
                    interaccion_usuario([dic_msg.get(13), 1, [palabra]])
                    letra_ingresada = input(dic_msg.get(14))
                    if letra_ingresada == "$":
                        seguir = False
                    break

    # imprime el mensaje de despedida
    interaccion_usuario([dic_msg.get(7), 0])
    interaccion_usuario([dic_msg.get(9), 0])
    interaccion_usuario([dic_msg.get(7), 0])
