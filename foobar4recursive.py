#real recursive

import math


def colcalc(curn):
    if curn > 189:
        return 19
    elif curn > 170:
        return 18
    elif curn > 152:
        return 17
    elif curn > 135:
        return 16
    elif curn > 119:
        return 15
    elif curn > 104:
        return 14
    elif curn > 90:
        return 13
    elif curn > 77:
        return 12
    elif curn > 65:
        return 11
    elif curn > 54:
        return 10
    elif curn > 44:
        return 9
    elif curn > 35:
        return 8
    elif curn > 27:
        return 7
    elif curn > 20:
        return 6
    elif curn > 14:
        return 5
    elif curn > 9:
        return 4
    elif curn > 5:
        return 3
    elif curn > 2:
        return 2
    


def col2(p):
    global tConf
    print('p:')
    print(p)
    tConf = tConf + math.trunc((p-1)/2)
    print('tConcol2bby:')
    print(tConf)


def multCol(k, c):
    global tConf
    global tCol
    tempN = k - c
    if c == 3:
        col2(tempN)
        while tempN >= 6:
            tempN -= 3
            col2(tempN)
    if c > 3:
        multCol(tempN, c - 1)
        while tempN >= (c*(c+1))/2:
            tempN -= c
            multCol(tempN, c - 1)
    

def solution(n):
    global tConf
    global tCol
    tConf = 0
    tCol = colcalc(n)

    col2(n)

    for i in range(3, tCol + 1):
        multCol(n, i)
        print('tConf1:')
        print(tConf)

    return tConf

    
arr = []

for x in range (3, 50):
    arr.append(solution(x))




print(arr)

#print(solution(35))
