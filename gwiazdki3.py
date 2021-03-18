#! /usr/bin/env python
# napisz funkcje ktora bedzie przyjmowala dwa parametry wysokosc oraz szerokosc choinki z uwzglednieniem pienka ktory zawsze bedzie wynosil dwa

def choinka(szerokosc, wysokosc):
    for obliczana_wysokosc in range(0, wysokosc):
        for obliczana_szerokosc in range(0, szerokosc):
            if ( \
                (obliczana_wysokosc == 0 and ( \
                    (szerokosc % 2 == 0 and ( \
                        obliczana_szerokosc == szerokosc / 2 or \
                        obliczana_szerokosc + 1 == szerokosc / 2) \
                    ) or \
                    (szerokosc % 2 == 1 and obliczana_szerokosc == (szerokosc - 1) / 2) \
                )) or (\
                obliczana_wysokosc == wysokosc - 3 and (obliczana_szerokosc == 0 or obliczana_szerokosc == szerokosc - 1) \
                ) \
            ):
                print("@", end = " ")
            elif ( \
                (obliczana_wysokosc == 0 and ( \
                    (szerokosc % 2 == 0 and ( \
                        obliczana_szerokosc == szerokosc / 2 or \
                        obliczana_szerokosc + 1 == szerokosc / 2) \
                    ) or \
                    (szerokosc % 2 == 1 and obliczana_szerokosc == (szerokosc - 1) / 2) \
                )) or (\
                obliczana_wysokosc <= wysokosc - 4 and (obliczana_szerokosc == 0 or obliczana_szerokosc == szerokosc - 1)) \
                or (\
                obliczana_wysokosc <= wysokosc - 6 and (obliczana_szerokosc == 1 or obliczana_szerokosc == szerokosc - 2)) \
                # or (\
                # obliczana_wysokosc <= wysokosc - 6 and (obliczana_szerokosc == 2 or obliczana_szerokosc == szerokosc - 3)) \
                # or (\
                # obliczana_wysokosc <= wysokosc - 6 and (obliczana_szerokosc == 3 or obliczana_szerokosc == szerokosc - 4)) \
            ):
            # elif ( \
            #     (szerokosc % 2 == 0 and ( \
            #         obliczana_wysokosc <= szerokosc / szerokosc))
            #     ):
                print(" ", end = " ")
            elif (obliczana_wysokosc >= wysokosc - 2):
                if ( \
                    (szerokosc % 2 == 0 and (obliczana_szerokosc == szerokosc / 2 or obliczana_szerokosc + 1 == szerokosc / 2)) or \
                    (szerokosc % 2) == 1 and (obliczana_szerokosc == (szerokosc - 1) / 2) \
                ): # <--- me learning python
                    print("$", end = " ")
                else:
                    print(" ", end = " ")
            else:
                print("*", end = " ")
        print("\n", end = "")

choinka(6,8)

#-----------
# nieparzyste += 0
# wys: 8
# wys_choinki: 6
# szerokosc: 5
# step: 6/5 = 1.2

#     @      0.0
#     *      1.2 <= 3.0 = 1
#     *      2.4 <= 3.0 = 1
#   * * *    3.6 <= 5.0 = 3
#   * * *    4.8 <= 5.0 = 3
# @ * * * @  6.0 <= 7.0 = 5
#     $     
#     $    

#-----------
# parzyste += 1
# wys: 8
# wys_choinki: 6
# szerokosc: 6
# step: 6/6 = 1

#     @ @     1.0 
#     * *     2.0 <= 2.0 = 2
#     * *     3.0 <= 4.0 = 2
#   * * * *   4.0 <= 4.0 = 4
#   * * * *   5.0 <= 6.0 = 4
# @ * * * * @ 6.0 <= 6.0 = 6
#     $ $     
#     $ $     