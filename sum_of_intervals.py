# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
def sum_of_intervals(intervals):
    res = 0
    if len(intervals):
        last_tail = sorted(intervals)[0][0]
    for iv in sorted(intervals):
        if iv[1]>last_tail:
            res += abs(max(iv[1],last_tail)-max(last_tail, iv[0]))
            last_tail = iv[1]
    return res



import codewars_test as test
@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(sum_of_intervals([(-230, 125), (-252, 447), (-263, -260), (133, 492)]), 747)



