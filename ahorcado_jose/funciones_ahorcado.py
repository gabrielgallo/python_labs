def busca_letra(palabra,letra_ingresada,incognita):
    i = 0
    b = ""
    for x in palabra:
        if x == letra_ingresada:
            b = b + letra_ingresada
        else:
            b = b + incognita[i]
        i = i + 1
    return b

def busca_no_adivinadas(incognita):
    i = 0
    for x in incognita:
        if x == "_":
            i = i + 1
    return i

def interaccion_usuario(x):
    i1 = i2 = 0
    z = ""
    if x[1] == 0:
        z = x[0]
    else:
        while i1 + 1 <= x[1]:
            for n in x[0]:
                if n == "~":
                    z = z + repr(x[2][i1])
                    i1 = i1 + 1
                else:
                    z = z + n
                i2 = i2 + 1
            i1 = i1 + 1
    print(z)