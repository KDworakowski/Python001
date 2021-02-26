import random

def losowanie(min = 1, max = 64, count = 6):

    lista = list()

    if max - min < count:
        count = max - min + 1

    # for _ in range(count):
    #     wynik = random.randint(min, max)
    #     if wynik not in lista:
    #         lista.append(wynik)
    # return lista

    while len(lista) != count:
        wynik = random.randint(min, max)
        if wynik not in lista:
            lista.append(wynik)
    return lista

def szybkie_losowanie(min = 1, max = 64, count = 6):

    lista = list(range(min, max+1))
    random.shuffle(lista)

    if max - min < count:
        count = max - min + 1
    return lista[0:count]
