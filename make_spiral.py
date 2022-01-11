# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python
import numpy as np
from itertools import cycle
def spiralize(size):
    spiral = [ [0]*size for i in range(size)]
    directions = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    i, j = 0, 0
    spiral[0][0] = 1
    for d in directions:
        break_me = True
        while 0 <= i+d[0] < size and 0 <= j+d[1] < size:
            i, j = i + d[0], j + d[1]
            if spiral[i][j] != 1:
                spiral[i][j] = 1
                break_me = False
            else:
                i, j = i - d[0], j - d[1]
                spiral[i][j] = 0
                i, j = i - d[0], j - d[1]
                break
        if break_me:
            if size%2==1:
                spiral[i + d[0]][j + d[1]] = 1
            break
    print(np.matrix(spiral))
    return spiral


import codewars_test as test



test.assert_equals(spiralize(5), [[1,1,1,1,1],
                                  [0,0,0,0,1],
                                  [1,1,1,0,1],
                                  [1,0,0,0,1],
                                  [1,1,1,1,1]])

test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                  [0,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,0,1],
                                  [1,0,0,0,0,1,0,1],
                                  [1,0,1,0,0,1,0,1],
                                  [1,0,1,1,1,1,0,1],
                                  [1,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,1,1]])

