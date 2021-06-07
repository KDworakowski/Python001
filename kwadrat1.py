#! /usr/bin/env python
wielkosc = 5
def kwadrat(wielkosc):
    # max = (wielkosc - 1 )
    max, if_helper = ([wielkosc, 1] if wielkosc % 2 == 0 else [wielkosc - 1, 0])
    # if_helper = (1 if wielkosc % 2 == 0 else 0)
    if (wielkosc < 3):
        print("Za male")
        exit()
    for obliczana_wysokosc in range(0, wielkosc):
        for obliczana_szerokosc in range(0, wielkosc):
            if ( \
                obliczana_szerokosc == (max/2) - obliczana_wysokosc - if_helper or \
                obliczana_szerokosc == (max/2) + obliczana_wysokosc or \
                obliczana_wysokosc == (max/2) - obliczana_szerokosc + max - if_helper or \
                obliczana_wysokosc == (max/2) + obliczana_szerokosc \
                ):
                print("x", end = " ")
            else:
                print(" ", end = " ")
        print("\n", end = "")

kwadrat(wielkosc)







# $x$
# xxx
# $x$


# $$x$$
# $xxx$
# xxxxx
# $xxx$
# $$x$$

