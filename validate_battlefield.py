# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

import numpy as np
def validate_battlefield(field):
    boats = {4: 0, 3: 0, 2: 0, 1: 0}
    field = [[0]*12]+[[0]+l+[0] for l in field]+[[0]*12]
    def boat_size(i, j):
        dj = 0
        while field[i][j+dj] != 0:
            field[i][j + dj] = 2
            dj += 1
        di = 0
        while field[i+di][j] != 0:
            field[i + di][j] = 2
            di += 1
        return (di, 1) if di>dj else (1, dj)

    def check_boat(i, j, size):
        b = []
        for x in range(i-1,i+size[0]+1):
            b.append(field[x][(j - 1):(j + size[1] + 1)])
        return sum([sum(x) for x in b]) == size[0]*size[1]*2

    for i in range(1,11):
        for j in range(1,11):
            if field[i][j] == 1:
                size = boat_size(i, j)
                if size[0]*size[1]>4:
                    return False
                if check_boat(i, j, size):
                    boats[size[0]*size[1]] += 1
                else:
                    return False
    return boats[4] == 1 and boats[3] == 2 and boats[2] == 3 and boats[1] == 4

import codewars_test as test

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleField = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 0, 0, 1]]

test.assert_equals(validate_battlefield(battleField), True, "Yep! Seems alright", "Nope, something is wrong!");