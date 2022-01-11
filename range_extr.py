def solution(args):
    if len(args) == 0:
        return ''
    res = []
    args = sorted(args)
    tmp = [args[0]]
    for i in range(1,len(args)):
        if args[i] == args[i-1]+1:
            tmp.append(args[i])
        else:
            res.append(tmp)
            tmp = [args[i]]
    if len(tmp)>0:
        res.append(tmp)
    return ','.join([str(x[0]) if len(x)==1 else f'{x[0]}-{x[-1]}' if len(x)>2 else f'{x[0]},{x[-1]}' for x in res])


import codewars_test as test

test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
test.assert_equals(solution([]), '')

