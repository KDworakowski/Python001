import pytest
import funkcje

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

@pytest.mark.parametrize('min,max,count,expected', test_data1)
def test_ilosc_zwracanych_liczb_szybko(min, max, count, expected):
    test = funkcje.szybkie_losowanie(min, max, count)
    assert len(test) == expected

def test_czy_sie_powtarza_szybko():
    test = funkcje.szybkie_losowanie()
    assert len(test) == len(set(test))

