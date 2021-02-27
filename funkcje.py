import random #importuje funkcje random

#definicja wolnego losowania, losowanie odbywa sie poprzez wybieranie losowych liczb w zakresie od min do max
def losowanie(min = 1, max = 64, count = 6): #tworzy definicje losowania z parametrami min, max oraz count

    lista = list() #tworzy zmienna, lista oznacza funkcje liste

    if max - min < count: #jezeli parametr max odjety od parametru min jest mniejszy od parametru count
        count = max - min + 1 #zmienia parametr count dodajac do niego 1 aby rownalo sie 6?, nie za bardzo tego ogarniam

    # for _ in range(count):
    #     wynik = random.randint(min, max)
    #     if wynik not in lista:
    #         lista.append(wynik)
    # return lista

    while len(lista) != count: #kiedy ilosc liczb w zmiennej lista nie rowna sie count, czyli liczbie 6
        wynik = random.randint(min, max) #zmienna wynik oznacza losowanie
        if wynik not in lista: #jezeli zmienna wynik, czyli nasza wylosowana liczba nie znajduje sie na liscie
            lista.append(wynik) #dodaj wyloswoana liczbe do list
    return lista #zwroc wartosc listy?

#definicja szybkiego losowania, losowanie odbywa się poprzez wrzucenie liczb w zakresie od min do max do listy, nastepnie te liczby zostana pomieszane oraz zostanie wybrane pierwsze 6 liczb
def szybkie_losowanie(min = 1, max = 64, count = 6): #tworzy definicje losowania z parametrami min, max oraz count

    lista = list(range(min, max+1)) #tworzy zmienna, lista oznacza funkcje list w zakresie od min do max dodac 1, nie rozumiem troche dlaczego w tej zmiennej jest range, w poprzedniej tego nie bylo chociaz osobiscie wydaje mi sie ze jest to z powodu metody losowania ktora miesza liczby przez co najpierw musi miec z czego je wybierac, tylko dlaczego +1?
    random.shuffle(lista) #miesza zmienna lista, z ktorej nastepnie wybierze pierwsze 6 liczb

    if max - min < count: #jezeli parametr max odjety od parametru min jest mniejszy od count
        count = max - min + 1 #zmienia parametr count dodajac do niego 1 aby rownalo sie 6?, nie za bardzo tego ogarniam
    return lista[0:count] #zwroc wartosc listy? zwracajac wartosc listy zwroc liczby od 0 do count, czyli do 6 liczb.

#piszac wszedzie 6 liczb oczywiscie mialem na mysli parametr count