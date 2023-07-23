# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python
def josephus_survivor(n,k):
    persons = [i for i in range(1,n+1)]
    i = 0
    while len(persons)>1:
        i = (i + k - 1) % len(persons)
        del persons[i]
    return persons[0]

import codewars_test as test
test.assert_equals(josephus_survivor(7,3),4)
test.assert_equals(josephus_survivor(11,19),10)
test.assert_equals(josephus_survivor(1,300),1)
test.assert_equals(josephus_survivor(14,2),13)
test.assert_equals(josephus_survivor(100,1),100)