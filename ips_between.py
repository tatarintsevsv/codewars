# https://www.codewars.com/kata/526989a41034285187000de4/train/python
def ips_between(start, end):
    s = 0
    for x in start.split('.'):
        s <<= 8
        s += int(x)
    s_e = 0
    for x in end.split('.'):
        s_e <<= 8
        s_e += int(x)
    return abs(s-s_e)
import codewars_test as test
test.assert_equals(ips_between("10.0.0.0", "10.0.0.50"), 50)
test.assert_equals(ips_between("20.0.0.10", "20.0.1.0"), 246)