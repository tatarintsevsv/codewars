#https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

def is_solved(board):
    for i in range(3):
        col = ''.join([str(x) for x in board[i]])
        row = ''.join([str(board[x][i]) for x in range(3)])
        diag = ''.join([str(board[x][x]) for x in range(3)]) + ' ' + ''.join([str(board[x][2-x]) for x in range(3)])
        if col == '111' or row == '111' or diag.count('111')>0:
            return 1
        if col == '222' or row == '222' or diag.count('222')>0:
            return 2
    if str(board).count('0') > 0:
        return -1
    return 0


import codewars_test as test
# not yet finished
board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
#test.assert_equals(is_solved(board), -1)

# winning row
board = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
test.assert_equals(is_solved(board), 1)

# winning column
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
test.assert_equals(is_solved(board), 1)

# draw
board = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
test.assert_equals(is_solved(board), 0)