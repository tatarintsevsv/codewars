#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(snail_map):
    move = [[0,1], [1,0], [0,-1], [-1,0]]
    [(x.insert(0,None)) for x in snail_map]
    [(x.append(None)) for x in snail_map]
    snail_map.insert(0,[None]*len(snail_map[0]))
    snail_map.append([None] * len(snail_map[0]))
    i=1
    j=1
    d=0
    res = []
    while snail_map[i][j]!=None:
        res.append(snail_map[i][j])
        snail_map[i][j] = None
        if snail_map[i+move[d][0]][j+move[d][1]] == None:
            d = d+1 if d<3 else 0
        i += move[d][0]
        j += move[d][1]
    return res
