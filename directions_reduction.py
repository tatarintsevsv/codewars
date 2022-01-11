# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
def dirReduc2(arr):
    visited = [[0, 0]]
    dx = {'NORTH': (-1, 0),'SOUTH': (1, 0), 'WEST': (0, -1), 'EAST': (0, 1), 'START':(0, 0)}
    pos = [0, 0]
    for d in arr:
        pos[0] += dx[d][0]
        pos[1] += dx[d][1]
        if pos in visited:
            print('already in ',visited.index(pos))
            visited = visited[:visited.index(pos)]
        visited.append([pos[0],pos[1]])
    dx = {dx[x]:x for x in dx}
    res = [dx[tuple(x)] for x in visited]
    return res[1:]

def dirReduc(arr):
    s = ','.join(arr) + ','
    l = 0
    while len(s) != l:
        l = len(s)
        s = s.replace('SOUTH,NORTH,','').replace('NORTH,SOUTH,','').replace('EAST,WEST,','').replace('WEST,EAST,','')
    return s.strip(',').split(',') if s.strip(',')!='' else []


import codewars_test as test
a = []
test.assert_equals(dirReduc(a), [])
