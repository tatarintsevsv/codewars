#https://www.codewars.com/kata/52ec24228a515e620b0005ef
from collections import defaultdict
def exp_sum(n):
    cache = defaultdict(int)
    def exp_sum_v(n,mx=-1,total='1'):
        c = cache[f'{n}-{mx}']
        if c != 0:
            return c
        res = 0
        if mx == -1:
            mx = n - 1
            res = 1            
        if n == 0:
            return 1
        for i in range(min(n, mx), 0, -1):
            if n - i >= 0:
                res += exp_sum_v(n - i, i, total + '+' + str(i))
        cache[f'{n}-{mx}'] = res
        return res
    return exp_sum_v(n)
