3from bingo_jose.clases_bingo import InteraccionUsuario, GeneradorCartones
from bingo_jose.funciones_bingo import nueva_bolilla

if __name__ == "__main__":
    msg0 = [""]
    msg1 = ["*"*44,"*       BIENVENIDO AL JUEGO DE BINGO       *","*"*44]
    msg2 = ["Ingrese la cantidad de jugadores: ","Debe ingresar un número entre 1 y 9"]
    msg3 = ["Ingrese la cantidad de números por cartón: ","Debe ingresar un número entre 1 y 9"]
    msg4 = ["Cartón del jugador: "]
    msg5 = ["*" * 44, "*       FIN DEL JUEGO - HASTA LUEGO        *", "*" * 44]
    msg6 = ["Pulse Enter para obtener la primera bolilla, 'x' para salir:"]

    interaccion = InteraccionUsuario
    carton = GeneradorCartones

    interaccion.imprime_lineas(msg1)
    cant_cartones = int(interaccion.ingresar_numero(msg2))
    cant_num_carton = int(interaccion.ingresar_numero(msg3))
    for ind in range(cant_cartones):
        msg0[0] = msg4[0] + repr(ind + 1)
        interaccion.imprime_lineas(msg0)
        interaccion.imprime_listas(carton.genera_carton(cant_num_carton))

    seguir = True
    while seguir:
        op = input(f"\nPulse Enter para obtener la primera bolilla, 'x' para salir:")
        if op == 'x':
            seguir = False
        else:
            nueva_bolilla()
            seguir = False

    interaccion.imprime_lineas(msg5)
