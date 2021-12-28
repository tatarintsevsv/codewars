# https://www.codewars.com/kata/57ff9d3b8f7dda23130015fa/train/python
def open(row, col):
    res = result.split('\n')[row][col*2]
    if res == 'x':
        print("!!! ERROR !!!",row,col)
        print(np.matrix(arr))
    return res
import numpy as np

def solve_mine(map, n):
    def find_mines(i, j, num):
        cnt=0
        mcnt=0
        mines, empty, res = [], [], []
        for di in [-1,0,1]:
            for dj in [-1, 0, 1]:
                if i+di<0 or i+di>len(arr)-1:
                    continue
                if j+dj<0 or j+dj>len(arr[0])-1:
                    continue
                if arr[i+di][j+dj] in ('?', 'x'):
                    cnt += 1
                    if arr[i + di][j + dj] == '?':
                        res.append([i+di,j+dj])
                    if arr[i + di][j + dj] == 'x':
                        mcnt += 1
        if cnt<=int(num):
            mines = res
        if mcnt==int(num):
            empty = res
        return mines, empty

    arr = [list(l) for l in map.replace(' ','').split('\n')]
    print(np.matrix(arr))
    loop = True
    while loop:
        loop = False
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j].isnumeric():
                    mines, can_open = find_mines(i, j, arr[i][j])
                    for f in mines:
                        arr[f[0]][f[1]] = 'x'
                    for f in can_open:
                        arr[f[0]][f[1]] = open(f[0], f[1])
                    loop |= len(can_open) > 0
                    print(np.matrix(arr))
                    print('\n')

    mines = n
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] in ('x','X'):
                mines -= 1
    print(f"mines left = {mines}\n")
    print(np.matrix(arr))
    pass

gamemap = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""".strip()
result = """
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1
""".strip()

solve_mine(gamemap,6)