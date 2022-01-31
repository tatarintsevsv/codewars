# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
'''
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
'''
def score(dice):
    s = ''.join([str(x) for x in sorted(dice)])
    res = 0
    for i in range(1,7):
        res += s.count(str(i)*3)*((i*100) if i != 1 else 1000)
        s = s.replace(str(i) * 3, '')
        if i in (1, 5):
            res += s.count(str(i))*(100 if i == 1 else 50)
    return res


import codewars_test as test

test.describe("Example Tests")
test.it("Example Case")
test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)
test.assert_equals( score(  [1, 1, 1, 3, 1] ), 1100)
