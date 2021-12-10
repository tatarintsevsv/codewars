#https://www.codewars.com/kata/5671d975d81d6c1c87000022
from itertools import *
d = {}
def genVars():
    def getH(s):
        m = 0
        v = 0
        for i in range(0, 4):
            if int(s[i]) > m:
                m = int(s[i])
                v += 1
        s = s[3] + s[2] + s[1] + s[0]
        m = 0
        vm = 0
        for i in range(0, 4):
            if int(s[i]) > m:
                m = int(s[i])
                vm += 1
        return str(v)+str(vm)
    for i in range(5):
        for j in range(5):
            d[str(i)+str(j)]=[]
    for s in permutations('1234'):
        ss = getH(s)
        d[getH(s)].append(''.join([x for x in s]))
        d[getH(s)[0]+'0'].append(''.join([x for x in s]))
        d['0'+getH(s)[1]].append(''.join([x for x in s]))
        d['00'].append(''.join([x for x in s]))
genVars()

def solve_puzzle (clues):
    def checkRes(arr):
        narr=['','','','']
        for i in range(4):
            for j in range(4):
                narr[i] += arr[j][i]
        res = True
        for i in range(4):
            x = str(clues[0+i])+str(clues[11-i])
            if not narr[i] in d[x]:
                res = False
        return res
    for r1 in d[str(clues[15])+str(clues[4])]:
        for r2 in d[str(clues[14])+str(clues[5])]:
            for r3 in d[str(clues[13])+str(clues[6])]:
                for r4 in d[str(clues[12])+str(clues[7])]:
                    if r1==[] or r2==[] or r3==[] or r4==[]:
                        continue
                    if checkRes([r1,r2,r3,r4]):
                        return (tuple(map(int,r1)),tuple(map(int,r2)),tuple(map(int,r3)),tuple(map(int,r4)))
    return []
