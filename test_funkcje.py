import pytest #importuje funkcje pytest
import funkcje #importuje funkcje

#w zmiennej test data podajemy parametry, nadpisujemy nimi parametry funkcji.
test_data1 = [
    (1, 2, 6, 2),
    (1, 64, 6, 6),
    (1, 1000, 1000, 1000),
    (1, 10000, 10000, 10000)
]

# @pytest.mark.parametrize('min,max,count,expected', test_data1)
# def test_ilosc_zwracanych_liczb(min, max, count, expected):
#     test = funkcje.losowanie(min, max, count)
#     assert len(test) == expected

# def test_czy_sie_powtarza():
#     test = funkcje.losowanie()
#     assert len(test) == len(set(test))

@pytest.mark.parametrize('min,max,count,expected', test_data1) #program testuje funkcje z parametrami ze zmiennej test_data1 oraz dodaje nowa funkcje expected
def test_ilosc_zwracanych_liczb_szybko(min, max, count, expected): #tworzy definicje testu ilosci zwracanych liczb w szybkim losowaniu z parametrami min, max, count oraz expected
    test = funkcje.szybkie_losowanie(min, max, count) #tworzy zmienna test ktora wlacza funkcje szybkiego losowania z funkcji, z parametrami min, max, count
    assert len(test) == expected #funkcja sprawdza czy ilosc znakow ktore da nam zmienna test jest rowna parametrowi expected

def test_czy_sie_powtarza_szybko(): #tworzy definicje test czy powtarza sie szybko
    test = funkcje.szybkie_losowanie() #tworzy zmienna test ktora wlacza funkcje szybkiego losowania
    assert len(test) == len(set(test)) #funkcja sprawdza czy ilosc znakow ktore da nam zmienna test rowna sie ilosci unilalnych znakow w zmiennej test

