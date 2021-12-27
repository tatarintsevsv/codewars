# https://www.codewars.com/kata/59a20f283203e8bd8c000006/train/python
import math
def generate_sequence(lower, upper):
    res = [0]*(upper-lower)
    for i in range(0,len(res)):
        if i*2<len(res)-1:
            res[i*2+1] = i+lower
        if i*2<len(res):
            res[i*2] = i+lower+math.floor(len(res)/2)
    return res

import codewars_test as test

test.describe('Basic tests')

testValues = (
    (1, 6),
    (1, 9),
    (2, 10),
    (2, 11)
)

for lower, upper in testValues:
    sequence = generate_sequence(lower, upper)
    print(sequence)
