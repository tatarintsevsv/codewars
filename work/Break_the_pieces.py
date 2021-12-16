#https://www.codewars.com/kata/591f3a2a6368b6658800020e
USE_BREAK_DISPLAY = True        # to get more details in the console when a test fails


def arr_print(a):
    for i in range(len(a)):
        if ''.join(a[i]).replace(' ','')!='':
            print('.'+''.join(a[i])+'.')

import numpy as np
from copy import deepcopy
import datetime

test_started = datetime.datetime.now()

def break_evil_pieces(shape):
    def fill_empty_space(i=0, j=0):
        shape_array[i][j] = '#'
        fill_list = []
        for di in (0, 1, -1):
            for dj in (1, 0, -1):
                if abs(di)+abs(dj) == 2 or di+dj == 0:
                    continue
                if (i + di) > len(shape_array) - 1 or (j + dj) > len(shape_array[0]) - 1 or j < 0 or i < 0:
                    continue
                c = 1
                while ((i + di*c) < len(shape_array) - 1) and ((j + dj*c) < len(shape_array[0]) - 1) and (i + di*c) >= 0 and (j + dj*c) >= 0:
                    if shape_array[i + di*c][j + dj*c] != ' ':
                        break
                    shape_array[i + di*c][j + dj*c] = '#'
                    fill_list.append((i + di*c, j + dj*c))
                    c += 1
        for c in fill_list:
            fill_empty_space(c[0],c[1])
        return

    def get_mask():
        def fill(i, j):
            arr[i][j] = '*'
            fill_list = []
            for di in (0, 1, -1):
                for dj in (1, 0, -1):
                    if (i + di) > len(arr) - 1 or (j + dj) > len(arr[0]) - 1 or j < 0 or i < 0:
                        continue
                    if arr[i + di][j + dj] in ('+', '|', '-'):
                        arr[i + di][j + dj] = '%'
                        continue
                    if arr[i + di][j + dj] == '#':
                        arr[i + di][j + dj] = 'X'
                        return
                    c = 1
                    while ((i + di * c) < len(arr) - 1) and ((j + dj * c) < len(arr[0]) - 1) and (i + di * c) >= 0 and (j + dj * c) >= 0:
                        if arr[i + di * c][j + dj * c] != ' ':
                            break
                        arr[i + di * c][j + dj * c] = '*'
                        fill_list.append((i + di * c, j + dj * c))
                        c += 1
            for c in fill_list:
                fill(c[0], c[1])
            return
        arr = deepcopy(shape_array)
        for i in range(len(arr)):
            if '+' in arr[i]:
                idx = arr[i].index('+')
                if arr[i + 1][idx + 1] == ' ' and arr[i + 1][idx] == '|' and arr[i][idx + 1] == '-':
                    arr[i][idx] = '*'
                    fill(i + 1, idx + 1)
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
        if figure == '':
            return ''
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

    started = datetime.datetime.now()
    print(started.strftime('%M:%S.%f'))
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
    fill_empty_space()

    figures = []
    while True:
        sm = datetime.datetime.now()
        m, fig_i, fig_j = get_mask()
        if (fig_i, fig_j) == (0, 0):
            break
        if m[0][0] == '*':
            shape_array[fig_i][fig_j] = ' '
            continue
        figure = ''
        tmp = np.array(m)
        count = tmp[tmp == 'X'].shape[0]
        mask_count = tmp[tmp == '*'].shape[0]
        if count != 0 or mask_count == 0 :
            shape_array[fig_i][fig_j] = ' '
            continue
        for i in range(1, len(m) - 2):
            for j in range(1, len(m[i]) - 2):
                figure += shape_array[i][j] if m[i][j] in ('*', '%') else ' '
                if m[i][j] == '*':
                    shape_array[i][j] = '#'
            figure += '\n'
        shape_array[fig_i][fig_j] = ' '
        #arr_print(m)
        #print('=========')
        #arr_print(shape_array)
        figures.append(figure)
        du = datetime.datetime.now() - sm
        print(f"fig: {du.seconds}.{du.microseconds}")

    res = []
    for f in figures:
        compressed = compress_figure(f)
        if len(compressed)>0:
            res.append(compressed)
    dur = datetime.datetime.now() - started
    print(f"duration: {dur.seconds}.{dur.microseconds}")
    dur = datetime.datetime.now() - test_started
    print(f"whole tests: {dur.seconds}.{dur.microseconds}")
    return res


shape = """
+--------+-+----------------+-+----------------+-+--------+
|        | |                | |                | |        |
|        | |                | |                | |        |
|        | |                | |           +----+ |        |
|      +-+ +-+            +-+ +-+         |+-----+    ++  |
|      |     |            |     |         ||          ||  |
+------+     +------------+     +------+  ||  +-------+| ++
|                                      |  ||  |     +--+ ||
+--------------------------------------+  ||  |     +---+++
|                                         ||  +--------+| |
|                                         |+-----------+| |
|                                         +----+ +------+ |
|                                              | |        |
|        +-+                +-+                | |        |
|        | |                | |                +-+        |
|        | |                | |                           |
|        | +-----+          | +-----+                     |
|        |    +-+|          |    +-+|                     |
|        +-+  | ||          +-+  | ||                     |
+-----+    +--+ |+-------+    +--+ |+--+                 ++
|     +--+      |        +--+      |   |                 ||
+----+   +---+  +-------+   +---+  +---+                 ++
|    |       |          |       |                         |
|    +---+ +-+          +---+ +-+                         |
|        | |                | |                           |
|        | |                | |                           |
|        | |                | |                +-+        |
|        +-+                | |                | |        |
|  +-----+ |    ++          ++++               | |        |
|  +-++----+    ++          ++++               | |        |
|    ++                     ++++             +-+ +-+      |
|    ||                     ++++             |     |      |
++   |+------------------------+      +------+     +------+
||   |               +--------+|      |                   |
++   +---+ +---------+   +---+||      +-------------------+
|        | |             |+-+|||                          |
|        | |             || ++||                          |
|        | |             |+---+|                          |
|        | |             +-----+                          |
|        | |                +-+                +-+        |
|        +-+                | |                | |        |
|                           ++++               | |        |
|                           ++++               | +-----+  |
|                           ++++               |    +-+|  |
|       +----+              ++++               +-+  | ||  |
++      |+--+|  ++-------------+      +-----+    +--+ |+--+
||      ||++||  ||   +--------+|      |     +--+      |   |
++      ||++||  ++---+   +---+||      +----+   +---+  +---+
|       |+--+|           |+-+|||           |       |      |
|       +----+           || ++||           +---+ +-+      |
|                        |+---+|               | |        |
|                        +-----+               | |        |
|        +-+                +-+                | |        |
|        | |                +-+                +-+        |
|        | |          +-----+ |    ++                     |
|        | |          +-++----+    ++                     |
|      +-+ +-+          ++                                |
|      |     |          ||                                |
+------+     +------+   |+-------------+                 ++
|                   |   |              |                 ||
+-------------------+   +---+ +--------+                 ++
|                           | |                           |
|                           | |                           |
|                           | |                           |
|                           | |                           |
|        +-+                | |                +-+        |
+--------+-+----------------+-+----------------+-+--------+
""".strip('\n')
print('==============================================================================')
res = break_evil_pieces(shape)
#for r in res:
#    print(f'---------------\n{r}\n---------------------')