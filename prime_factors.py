# https://www.codewars.com/kata/542f3d5fd002f86efc00081a/train/python

def prime_factors (n):
    res = []
    i = 2
    while n>1:
        while n%i==0:
            res.append(i)
            n //=i
        i += 1
    return res


import codewars_test as test
test.assert_equals(prime_factors(1), [])
test.assert_equals(prime_factors(3), [3])
test.assert_equals(prime_factors(8), [2, 2, 2])
test.assert_equals(prime_factors(9), [3, 3])
test.assert_equals(prime_factors(12), [2, 2, 3])