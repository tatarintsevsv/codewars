# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
def power(x, n, i, mult):
    if n == 1:
        return x
    if n == 0:
        return i
    y = power(x, n // 2, i, mult)
    y = mult(y, y)
    if n % 2:
        y = mult(x, y)
    return y

def identity_matrix(n):
    return [[1 if i == j else 0 for i in list(range(n))] for j in list(range(n))]

def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b
                 for a, b in zip(row_a, col_b))
            for col_b in BT]
            for row_a in A]

def fib(n):
    if n==0:
        return 0
    sign = -1 if n%2==0 else 1
    F = power([[1, 1], [1, 0]], abs(n), identity_matrix(2), matrix_multiply)
    return F[0][1] if n>0 else sign*F[0][1]