# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
def scramble(s1, s2):
    while len(s2) > 0:
        if s1.count(s2[0]) >= s2.count(s2[0]):
            s1 = s1.replace(s2[0], '')
            s2 = s2.replace(s2[0], '')
        else:
            return False
    return True


import codewars_test as test
test.assert_equals(scramble('rkqodlw', 'world'),  True)
test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
test.assert_equals(scramble('katas', 'steak'), False)
test.assert_equals(scramble('scriptjava', 'javascript'), True)
test.assert_equals(scramble('scriptingjava', 'javascript'), True)