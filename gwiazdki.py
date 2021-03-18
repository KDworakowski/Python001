#! /usr/bin/env python
def make_odd(a):
    if (a % 2) == 0:
        a += 1
    return a


def gwiazdki(num1):
    num1 = make_odd(num1)
    for x in range(0,num1):
        for y in range(0,num1):
            arg1 = (y == (num1 - 1) / 2)
            arg2 = (x == (num1 - 1) / 2)
            if arg1 and arg2:
                print("x", end = " ")
            elif (y == 0 and x == 0) or (y == 0 and x == num1 - 1) or (y == num1 - 1 and x == 0) or (y == num1 - 1 and x == num1 - 1):
                print("X", end = " ")
            elif x == y or x == num1 - 1 - y:
                print("$", end = " ")
            elif x == 0 or x == num1 - 1 or y == 0 or y == num1 - 1:
                print("0", end = " ")
            else :
                print("*", end = " ")
                # print(f"[{x},{y}]", end = " ")
        print("\n", end = "")

gwiazdki(9)
