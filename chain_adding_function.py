# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python


class add(int):
    def __call__(self, *args, **kwargs):
        return add(self+args[0])

import codewars_test as test

@test.it("Basic tests")
def _():
    test.assert_equals(add(1), 1)
    test.assert_equals(add(1)(2), 3)
    test.assert_equals(add(1)(2)(3), 6)