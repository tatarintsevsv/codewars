#https://www.codewars.com/kata/591f3a2a6368b6658800020e
USE_BREAK_DISPLAY = True        # to get more details in the console when a test fails


def arr_print(a):
    for i in range(len(a)):
        print('.'+''.join(a[i])+'.')

import numpy as np
from copy import deepcopy
import sys


def break_evil_pieces(shape):
    def get_mask():
        def fill(i, j):
            arr[i][j] = '*'
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if (i + di) > len(arr) - 1 or (j + dj) > len(arr[0]) - 1 or j < 0 or i < 0:
                        continue
                    if arr[i + di][j + dj] in ('+', '|', '-', '*'):
                        arr[i + di][j + dj] = '*'
                        continue
                    if arr[i + di][j + dj] == ' ':
                        fill(i + di, j + dj)
            return False

        arr = deepcopy(shape_array)
        for i in range(len(arr)):
            if '+' in arr[i]:
                idx = arr[i].index('+')
                if arr[i + 1][idx + 1] == ' ':
                    fill(i + 1, idx + 1)
                arr[i][idx] = '*'
                return arr, i, idx
        return [], 0, 0

    def expand_shape(figure):
        s = []
        for l in figure.split('\n'):
            l = l.replace('-', '--').replace('+', '+-').replace(' ', '  ').replace('|', '| ').replace('+-|', '+ |').replace('+- ', '+  ').replace('x', 'xx')
            s.append(l)
        tmp = [list(l) for l in s]
        tmp = np.rot90(tmp)
        s = []
        figure = '\n'.join([''.join(l) for l in tmp])
        for l in figure.split('\n'):
            l = l.replace('|', '||').replace('+', '+|').replace(' ', '  ').replace('-', '- ').replace('+|-', '+ -').replace('+| ', '+  ').replace('x', 'xx')
            while len(l) < 35:
                l += ' '
            s.append(l)
        tmp = [list(l) for l in s]
        tmp = np.rot90(tmp, -1)
        return '\n'.join([''.join(l) for l in tmp])

    def compress_figure(figure):
        figure = remove_pluses(figure)
        lines = [' '+l for l in figure.split('\n') if len(l.replace(' ', '')) > 0]
        res = []
        maxlen = len(max(lines, key=len))
        for i in range(len(lines)):
            line = lines[i].rstrip()[1:]
            while len(line) < maxlen:
                line += ' '
            if i % 2 == 0:
                res.append([line[n + 1] for n in range(0, len(line) - 1) if n % 2 == 0])
        res = np.rot90(res, -1)
        figure = '\n'.join([''.join(l) for l in res]).rstrip('\n')

        lines = [ l for l in figure.split('\n')]
        res = []
        for line in lines:
            if len(line.replace(' ', '')) > 0:
                res.append([line[n] for n in range(0, len(line))])
        res = np.rot90(res, 1)
        return '\n'.join([''.join(l).rstrip() for l in res]).rstrip('\n')

    def remove_pluses(figure):
        arr = [[' ']+list(l)+[' '] for l in figure.split('\n')]
        arr.insert(0,[' ']*len(arr[0]))
        arr.append(arr[0])
        for i in range(1, len(arr)-1):
            for j in range(1, len(arr[i])-1):
                if arr[i][j] != '+':
                    continue
                if arr[i][j+1] == '-' and arr[i][j-1] == '-' and arr[i+1][j] == ' ' and arr[i-1][j] == ' ':
                    arr[i][j] = '-'
                    continue
                if arr[i+1][j] == '|' and arr[i-1][j] == '|' and arr[i][j+1] == ' ' and arr[i][j-1] == ' ':
                    arr[i][j] = '|'
                    continue
        figure = '\n'.join([''.join(l).rstrip()[1:] for l in arr[1:-1]]).rstrip('\n')
        return figure

    sys.setrecursionlimit(25000)
    print(shape)

    maxlen = len(max(shape.split('\n'), key=len))
    ftmp = ''
    for l in shape.split('\n'):
        while len(l) < maxlen:
            l += ' '
        ftmp += ' ' + l + ' \n'
    shape = ' ' * (maxlen + 2) + '\n' + ftmp + ' ' * (maxlen + 2)

    f = expand_shape(shape)

    shape_array = [list(l) for l in f.split('\n')]
    figures = []

    while True:
        m, fig_i, fig_j = get_mask()
        if (fig_i, fig_j) == (0, 0):
            break
        if m[0][0] == '*':
            shape_array[fig_i][fig_j] = ' '
            continue
        figure = ''
        for i in range(1, len(m) - 2):
            for j in range(1, len(m[i]) - 2):
                figure += shape_array[i][j] if m[i][j] == '*' else ' '
            figure += '\n'
        shape_array[fig_i][fig_j] = ' '
        print(figure)
        figures.append(figure)
    res = []
    for f in figures:
        res.append(compress_figure(f))
    return res


shape = """

         +-+                +-+                +-+         
         +-+                | |                +-+         
                            ++++                           
                            ++++                           
                            ++++                           
        +----+              ++++                           
++      |+--+|  ++-------------+      ++                 ++
||      ||++||  ||   +--------+|      ||                 ||
++      ||++||  ++---+   +---+||      ++                 ++
        |+--+|           |+-+|||                           
        +----+           || ++||                           
                         |+---+|                           
                         +-----+                           
         +-+                +-+                +-+         
         +-+                +-+                +-+         
""".strip('\n')


res = break_evil_pieces(shape)
for r in res:
    print(r)