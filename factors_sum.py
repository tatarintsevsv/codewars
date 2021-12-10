#https://www.codewars.com/kata/54d496788776e49e6b00052f
from collections import defaultdict
import math
def sum_for_list(lst):
    res = defaultdict(int)
    print(lst)
    for x in lst:
        curr = x
        x = abs(x)
        for i in range(2,x+1):
            if x<i:
                break
            if x%i==0:
                res[i]+=curr
                while x % i == 0:
                    x = int(x / i)
    return sorted([[x,res[x]] for x in res])
