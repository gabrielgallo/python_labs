import juegos_modules.bingo_gog as bingo


print("Bienvenidos al sistema de Juegos")
print("-" * 60)

print("Elija el juego que desea iniciar:")
print("1 - Bingo")
print("2 - Ahorcadito")
print("3 - Adivinar frase revuelta")

op = int(input("Nro de opción: "))

if(op==1):
    bingo.bingo_start()
else:
    print("No es una opción válida")