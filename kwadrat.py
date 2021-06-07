#! /usr/bin/env python

def kwadrat(wielkosc: int) -> int:
    max, if_helper = ([wielkosc, 1] if wielkosc % 2 == 0 else [wielkosc - 1, 0])

    if (wielkosc < 1):
        print("Za male")
        return 1

    for obliczana_wysokosc in range(0, wielkosc):
        for obliczana_szerokosc in range(0, wielkosc):
            test1_helper = (max/2) - obliczana_wysokosc - if_helper
            test2_helper = (max/2) + obliczana_wysokosc
            test3_helper = (max/2) - obliczana_szerokosc + max - if_helper
            test4_helper = (max/2) + obliczana_szerokosc
            test1 = obliczana_szerokosc >= test1_helper
            test2 =  obliczana_szerokosc <= test2_helper
            test3 = obliczana_wysokosc <= test3_helper
            test4 = obliczana_wysokosc <= test4_helper

            test = test1 and test2 and test3 and test4

            if test:
                print("x", end = " ")
            else:
                print("_", end = " ")

            True
        print("\n", end = "")

    return 0

exit(kwadrat(1))


# _ _ x x x  &  x x x _ _  =  _ _ x _ _ 
# _ x x x x  &  x x x x _  =  _ x x x _ 
# x x x x x  &  x x x x x  =  x x x x x 
# x x x x x  &  x x x x x  =  x x x x x 
# x x x x x  &  x x x x x  =  x x x x x 
