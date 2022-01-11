# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

def puzzle_print(puzzle):
    for i in range(9):
        if i%3 == 0 and i !=0:
            print('───┼───┼───')
        s = [str(x) for x in puzzle[i]]
        print(''.join(s[:3]),'│',''.join(s[3:6]),'│',''.join(s[6:9]),sep='')

def sudoku(puzzle):
    row_candidates=[]
    col_candidates=[]
    squares_candidates = []
    for i in range(9):
        col_candidates.append(set(list(range(1,10))).difference(set([x for x in puzzle[i] if x != 0])))
        row_candidates.append(set(list(range(1,10))).difference(set([puzzle[x][i] for x in range(9) if puzzle[x][i] != 0])))
        square = []
        for x in range(i // 3 * 3, i // 3 * 3 + 3):
            for y in range(i % 3 * 3, i % 3 * 3 + 3):
                if puzzle[x][y] != 0:
                    square.append(puzzle[x][y])
        squares_candidates.append(set(list(range(1,10))).difference(set(square)))
    candidate = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                candidate[i][j] = puzzle[i][j]
                continue
            res = col_candidates[i].intersection(row_candidates[j])
            res = res.intersection(squares_candidates[i // 3*3 + j // 3])
            candidate[i][j] = res if len(res)>1 else res.pop()
    # clean resolved candidates
    modified = True
    while modified:
        modified = False
        row_candidates = []
        col_candidates = []
        squares_candidates = []
        for i in range(9):
            col_candidates.append(set(list(range(1, 10))).intersection(set([x for x in candidate[i] if type(x) != set])))
            row_candidates.append(set(list(range(1, 10))).intersection(set([candidate[x][i] for x in range(9) if type(candidate[x][i]) != set])))
            square = []
            for x in range(i // 3 * 3, i // 3 * 3 + 3):
                for y in range(i % 3 * 3, i % 3 * 3 + 3):
                    if type(candidate[x][y]) != set:
                        square.append(candidate[x][y])
            squares_candidates.append(set(list(range(1, 10))).intersection(set(square)))
        for i in range(9):
            for j in range(9):
                if type(candidate[i][j]) != set:
                    continue
                res = candidate[i][j].difference(row_candidates[j])
                res2 = candidate[i][j].difference(col_candidates[i])
                res3 = candidate[i][j].difference(squares_candidates[i // 3 * 3 + j // 3])
                res = res.intersection(res2).intersection(res3)
                if res != candidate[i][j] and len(res)>0:
                    candidate[i][j] = res if len(res) > 1 else res.pop()
                    modified = True
    return candidate

import codewars_test as test
test.describe('Sudoku')

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]


puzzle_print(puzzle)
test.it('Puzzle 1')
test.assert_equals(sudoku(puzzle), solution, "Incorrect solution for the following puzzle: " + str(puzzle));
puzzle_print(puzzle)