#https://www.codewars.com/kata/520446778469526ec0000001
def same_structure_as(original,other):
    if type(original) in (int, str) and type(other) in (int, str):
        return True
    if type(original)!=type(other):
        return False
    if len(original) != len(other):
        return False
    for i in range(len(original)):
        if not same_structure_as(original[i],other[i]):
            return False
    return True
