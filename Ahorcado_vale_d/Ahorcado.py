
print("Bienvenido al Juego Ahorcado")
try:
    file2 = open("Palabra.txt", "r")
    palabra = file2.read()
except FileNotFoundError:
    print("El archivo no existe" , FileNotFoundError)
except:
    print("Se produjo un error no esperado")
lista = list()
print("La palabra a adivinar tiene: " + str(len(palabra))
      + " letras")
for x in palabra:
    letra = "_"
    print(letra, end=" ")
    lista.append(letra)
print("\n")

error = 0
seguir = True
while seguir:
    op = input("Enter para ingresar la próxima letra, o '0' para salir:")
    letra = input("Ingrese una letra:")
    seguir = False if str("0") == op else True
    for i, l in enumerate(palabra):
        if l.lower() == letra.lower():
            lista[i] = l.upper()

    if letra.upper() not in lista:
        error = error + 1

    guion = "_"
    print("Cantidad de errores cometidos: " + str(error))
    print(lista)
    if op == "0" or letra == "0":
        break;
    if guion not in lista:
        print("Adivino la palabra!!!")
        break;
    if error == 7:
        print("Perdio el juego!!!")
        break;
