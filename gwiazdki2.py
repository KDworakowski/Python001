#! /usr/bin/env python

def gwiazdki(num):
    for x in range(0, num):
        for y in range(0, num):
            if (y == 0 or x == 0 or x == num - 1 or y == num - 1):
                print("*", end = " ")
            elif (x%2 != 0 and y%2 != 0) or (x%2 == 0 and y%2 == 0):
                print("x", end = " ")
            elif (x%2 != 0 and y%2 == 0) or (x%2 == 0 and y%2 != 0):
                print(" ", end = " ")
            else:
                print("D", end = " ")
        print("\n", end = "")

gwiazdki(10)

# 0,0 0,1 0,2 0,3 0,4 0,5
# 1,0 1,1 1,2 1,3 1,4 1,5
# 2,0 2,1 2,2 2,3 2,4 2,5
# 3,0 3,1 3,2 3,3 3,4 3,5
# 4,0 4,1 4,2 4,3 4,4 4,5
# 5,0 4,1 5,2 5,3 5,4 5,5