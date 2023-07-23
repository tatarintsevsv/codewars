# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python
def done_or_not(board):
    for i in range(9):
        col = ''.join(sorted([str(x) for x in board[i]]))
        row = ''.join(sorted([str(board[x][i]) for x in range(9)]))
        square = []
        for x in range(i // 3 * 3, i // 3 * 3 + 3):
            for y in range(i % 3 * 3, i % 3 * 3 + 3):
                square.append(str(board[x][y]))
        square = ''.join(sorted(square))
        if square != '123456789' or col != '123456789' or row != '123456789':
            return 'Try again!'
    return 'Finished!'

import codewars_test as test

test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');

test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');