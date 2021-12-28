import math
def generate_diagonal(n, l):
    res=[math.factorial(n+i) / (math.factorial(i) * math.factorial(n)) for i in range(l)]
    return res
    res = []
    def C(n,k):
        return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
    for i in range(l):
        res.append(C(n+i, n))
    return res


import codewars_test as test
test.assert_equals(generate_diagonal(2, 5),[1, 3, 6, 10, 15])
test.assert_equals(generate_diagonal(1, 10),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test.assert_equals(generate_diagonal(3, 7),[1, 4, 10, 20, 35, 56, 84])