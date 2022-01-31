def perimeter(n):
    fib = [1, 1]
    sum = 2
    for i in range(2,n+1):
        e = fib[0] + fib[1]
        fib = [fib[1],e]
        sum += e
    return sum*4

import codewars_test as test
test.assert_equals(perimeter(5), 80)
test.assert_equals(perimeter(7), 216)
test.assert_equals(perimeter(20), 114624)
test.assert_equals(perimeter(30), 14098308)
test.assert_equals(perimeter(100), 6002082144827584333104)