#https://www.codewars.com/kata/52bef5e3588c56132c0003bc
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
def get_by_level(node,curr,level):
    res = []
    if node==None:
        return res;
    if curr<level:
        res.extend(get_by_level(node.left,curr+1,level))
        res.extend(get_by_level(node.right,curr+1,level))
    if curr==level:
        res.append(node.value)
    return res

def tree_by_levels(node):
    res = []
    l = 1
    while True:
        nodes = get_by_level(node,1,l)
        res.extend(nodes)
        l += 1
        if len(nodes)==0:
            break
    return res
