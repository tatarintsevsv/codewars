#https://www.codewars.com/kata/591f3a2a6368b6658800020e

import numpy as np
USE_BREAK_DISPLAY = True        # to get more details in the console when a test fails


def arr_print(a):
    for i in range(len(a)):
        print(''.join(a[i]))


def break_evil_pieces(shape):

    def find_ribs(corner):
        ribs = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i, j = corner[0]+di,corner[1]+dj
            while field[i][j] in ('+', '-', '|'):
                if field[i][j] == '+':
                    ribs.append((i, j))
                    break
                i, j = i + di, j + dj
        return ribs

    def find_cycles(start, corner, visited=[]):
        for neighbor in corners[corner]:
            if len(visited)>1 and neighbor==start:
                cycle = sorted(visited+[corner])
                if cycle not in cycles:
                    cycles.append(cycle)
                return True
            if neighbor in visited:
                continue
            find_cycles(start, neighbor, visited+[corner])
        return False

    def render_figure(cycle):
        figure = [cycle[0]]
        min_i , min_j, max_i, max_j = cycle[0][0], cycle[0][1], 0, 0
        while len(cycle) > 0:
            neighbors = list(set(corners[figure[-1]]).intersection(cycle))
            if neighbors[0][0]<min_i:
                min_i = neighbors[0][0]
            if neighbors[0][1]<min_j:
                min_j = neighbors[0][1]
            if neighbors[0][0]>max_i:
                max_i = neighbors[0][0]
            if neighbors[0][1]>max_j:
                max_j = neighbors[0][1]
            figure.append(neighbors[0])
            cycle.remove(neighbors[0])
            if len(figure) > 3:
                if figure[-1][0] == figure[-3][0] or figure[-1][1] == figure[-3][1]:
                    del figure[-2]
        figure = figure[1:]
        if figure[0][0] == figure[-2][0] or figure[0][1] == figure[-2][1]:
            del figure[-1]
        if figure[1][0] == figure[-1][0] or figure[1][1] == figure[-1][1]:
            del figure[0]
        arr =  [[' ' for y in range(max_j+2)] for x in range(max_i+2)] # [[' ']*(max_j+2)]*(max_i+2)
        start_i, start_j = figure.pop()
        figure.insert(0,(start_i, start_j))
        last_i, last_j = start_i, start_j
        while len(figure) > 0:
            i, j = figure.pop()
            di = 0 if i == last_i else (-1 if i > last_i else 1)
            dj = 0 if j == last_j else (-1 if j > last_j else 1)
            x, y = i, j
            while x != last_i or y != last_j:
                arr[x][y] = '-' if last_i == x else '|'
                x, y = x + di, y + dj
            arr[i][j] = '+'
            last_i, last_j = i, j
        res = ''
        for l in arr[min_i:max_i+1]:
            res += ''.join(l[min_j:max_j+1]) + '\n'
        return res.strip('\n'), (min_i, min_j)

    def get_mask(fig, pos):
        def fill(i, j):
            if arr[i][j] != ' ':
                return
            arr[i][j] = '*'
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if arr[i + di][j + dj] in ('+', '|', '-'):
                        arr[i + di][j + dj] = '*'
                    fill(i + di, j + dj)
        fig1 = fig.split('\n')
        arr = [[' ' for y in range(len(field[0]) + 2)] for x in range(len(field) + 2)]
        for i in range(len(fig1)):
            for j in range(len(fig1[i])):
                arr[i+pos[0]][j+pos[1]] = fig1[i][j]
        for i in range(len(arr)):
            if '+' in arr[i]:
                fill(i + 1, arr[i].index('+') + 1)
                break
        return arr

    def overlap(fig1, fig2):
        arr = [[' ' for y in range(len(field[0]) + 2)] for x in range(len(field) + 2)]
        for i in range(len(fig1)):
            for j in range(len(fig1[0])):
                c = fig1[i][j]
                if fig1[i][j]=='*' and fig2[i][j] == '*':
                    c = '_'
                if fig1[i][j] == ' ' and fig2[i][j] == '*':
                    c = '#'
                arr[i][j] = c
        return arr

    def check_overlaps():
        def check_overlaps():
            has_empty = True
            while has_empty:
                has_empty = False
                for i in range(len(renders)):
                    mask = get_mask(renders[i], positions[i])
                    # print(renders[i])
                    # arr_print(mask)
                    for j in range(len(renders)):
                        if i == j:
                            continue
                        # print(renders[j])
                        mask2 = get_mask(renders[j], positions[j])
                        # arr_print(mask2)
                        mask = overlap(mask, mask2)
                        # arr_print(mask)
                        # print('\n\n')
                        t = ''.join(''.join(l) for l in mask)
                        t = t.replace(' ', '').replace('+', '').replace('-', '').replace('|', '').replace('_', '')
                        if len(t) == 0:
                            has_empty = True
                            del renders[i]
                            break
                    if has_empty:
                        break
    field = [[' ']+list(x)+[' '] for x in shape.split('\n')]
    maxlen = len(max(shape.split('\n'), key=len)) + 2
    field.insert(0,[' ']*maxlen)
    field.append(field[0])
    for i in range(len(field)):
        while len(field[i])<maxlen:
            field[i].append(' ')
    corners = {}
    cycles = []
    renders = []
    positions = []
    print(shape)

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '+':
                corners[(i,j)]=[]

    for corner in corners:
        corners[corner] = find_ribs(corner)

    for corner in corners:
        find_cycles(corner, corner)

    has_long_cycles = True
    while has_long_cycles:
        has_long_cycles = False
        for i in range(len(cycles)):
            for j in range(len(cycles)):
                if i == j or len(cycles[i]) == 0 or len(cycles[j]) == 0:
                    continue
                if np.array_equal(sorted(set(cycles[i]).intersection(cycles[j])),cycles[i]):
                    cycles[j]=[]
                    has_long_cycles = True
                    break

    for cycle in sorted(cycles):
        if len(cycle) == 0:
            continue
        fig, pos = render_figure(cycle)
        renders.append(fig)
        positions.append(pos)

    check_overlaps()

    for i in range(len(renders)):
        renders[i] = '\n'.join([l.rstrip() for l in renders[i].split('\n')]).rstrip('\n')

    return renders



# Driver Code

import codewars_test as test

shape = """

 +------------+ x  
 |            | x
 |            | x
 |            | x
 +------++----+ x
 |      ||    | x
 |      ||    | x
 +------++----+ x
        ||      x
    +---+|      x 
    +----+      x         
 xxxxxxxxxxxxxxxx
 
 xx
 xxxxxxx
 xxxxxxx  
""".strip('\n')



#quit()
#res = break_evil_pieces(shape)
#for r in res:
#    print(r)


field = [[' ']*30]*20

def get_mask(fig, pos):
    def fill(i, j):
        if arr[i][j] in ('+', '|', '-'):
            #arr[i][j] = 'x'
            return
        if arr[i][j] != ' ':
            return
        arr[i][j] = '*'
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (i + di)>len(arr)-1 or (j + dj)>len(arr[0])-1 or j<0 or i<0:
                    continue
                #if arr[i + di][j + dj] in ('+', '|', '-'):
                #    arr[i + di][j + dj] = '*'
                fill(i + di, j + dj)

    fig1 = fig.split('\n')
    arr = [[' ' for y in range(len(field[0]) + 2)] for x in range(len(field) + 2)]
    for i in range(len(fig1)):
        for j in range(len(fig1[i])):
            arr[i + pos[0]][j + pos[1]] = fig1[i][j]

    while True:
        for i in range(len(arr)):
            if '+' in arr[i]:
                idx = arr[i].index('+')
                fill(i + 1, idx+1)
                arr[i][idx] = 'x'
                arr_print(arr)
                break


    return arr

def expand_shape():
    s=[]
    for l in shape.split('\n'):
        l = l.replace('-', '--') \
            .replace('+','+-') \
            .replace('|', '|.') \
            .replace(' ', '  ') \
            .replace('x', 'xx')
        s.append(l)
    arr_print(s)

expand_shape()
quit()
m = get_mask(shape,(0,0))
arr_print(m)