# https://www.codewars.com/kata/56e02d5f2ebcd50083001300/train/python

from collections import defaultdict

class Decorator:
    def __init__(self,cls):
        self._obj = cls
        self._obj.vars = defaultdict(str)


    def __getattr__(self, item):
        if item == "_obj":
            return self._obj
        if self._obj.vars[item] == "":
            self._obj.vars[item] = "INIT"
        if self._obj.vars[item] == "DEL":
            my_type = type(f"type_{item}", (str,), {"get_change": self._obj.vars[item]})
            return my_type('')
        if not hasattr(self._obj,item):
            my_type = type(f"type_{item}", (), {"get_change": self._obj.vars[item]})
            return my_type(None)

        my_type = type(f"type_{item}", (type(getattr(self._obj, item)),), {"get_change": self._obj.vars[item]})
        return my_type(getattr(self._obj, item))

    def __setattr__(self, key, value):
        if key != '_obj':
            if self._obj.vars[key]=="":
                self._obj.vars[key] = "INIT"
            else:
                if value != getattr(self._obj, key):
                    self._obj.vars[key] = "MOD"
            return super(type(self._obj),self._obj).__setattr__(key, value)
        return super(Decorator, self).__setattr__(key, value)

    def __delattr__(self, item):
        self._obj.vars[item] = "DEL"
        return super(type(self._obj), self._obj).__delattr__(item)



def change_detection(cls):
    def wrapper(*args, **kwargs):
        return Decorator(cls(*args, **kwargs))
    return wrapper


import codewars_test as test

@test.describe('Sample tests')
def sample_tests():
    class U:
        def __init__(self, x=0):
            self.x = x.x if isinstance(self, x.__class__) else x

        def f(self, y):
            return self.x + y

    @change_detection
    class Struct:
        x = 42
        no = None

        def __init__(self, y=0):
            self.y = y
            self.u = U(4)
            self.uuu = None

        def f(self):
            if self.tt.get_change:
                self.tt += 1
            else:
                self.tt = 0

    #a = Struct(11)

    Struct.x

    print(a.x)
    quit()

    @test.it('Object attributes')
    def it_1():
        test.assert_equals(a.y, 11, 'Instance attribute has a correct value')
        test.assert_equals(a.y.get_change, 'INIT', 'Initial state is correct')
        test.assert_equals(2 * a.y + 20, 42, 'Integer attributes should work as integers')
        a.y = 11
        msg = "The state doesn't change if the same value is assigned"
        test.assert_equals(a.y.get_change, 'INIT', msg)
        a.y = 12
        test.assert_equals(a.y.get_change, 'MOD', 'Attribute was modified')
        a.y = 12
        msg = 'Modified attribute was assigned the same value again'
        test.assert_equals(a.y.get_change, 'MOD', msg)
        del a.y
        test.assert_equals(a.y.get_change, 'DEL', 'Attribute was deleted')

    @test.it('Class attributes')
    def it_2():
        test.assert_equals(Struct.x, 42, 'Class attribute has a correct values')
        test.assert_equals(a.x, 42, 'Class attribute has a correct values')
        test.assert_equals(a.x.get_change, 'INIT', 'Initial state is correct')
        a.y = 12
        test.assert_equals(a.x - a.y, 30, 'Integer attributes should work as integers')
        a.x = '42'
        msg = 'Class attribute was changed on an instance'
        test.assert_equals(a.x, '42', msg)
        test.assert_equals(a.x.get_change, 'MOD', msg)
        test.assert_equals(a.x + '1', '421', 'String attributes should work as strings')
        del a.x
        msg = 'Class attribute was deleted on an instance'
        test.expect((a.x == 42 and a.x.get_change == 'INIT') or
                    (not a.x and a.x.get_change == 'DEL'), msg)

    @test.it('Undefined attributes')
    def it_3():
        test.assert_equals(a.z.get_change, '', 'Non-existent attribute has no state')
        test.assert_equals(a._mumu_.get_change, '', 'Non-existent attribute has no state')
        msg = 'No state should be assigned after trying to access it once'
        test.assert_equals(a._mumu_.get_change, '', msg)

    @test.it('When attribute is from Final class (None, bool)')
    def it_4():
        msg = "Value of None should equal to None. You can use predefined NONE."
        test.assert_equals(a.uuu, None, msg)
        msg = "None attributes should also support 'get_change'. Have you tried NONE?"
        test.assert_equals(a.uuu.get_change, 'INIT', msg)
        a.uuu = None
        msg = 'None was assigned to a None attribute'
        test.assert_equals(a.uuu, None, msg)
        test.assert_equals(a.uuu.get_change, 'INIT', msg)
        a.uuu = False
        msg = 'False was assigned to a None attribute'
        test.assert_equals(a.uuu, False, msg)
        test.assert_equals(a.uuu.get_change, 'MOD', msg)
        a.uuu = None
        msg = 'None was assigned to a None attribute back'
        test.assert_equals(a.uuu, None)
        test.assert_equals(a.uuu.get_change, 'MOD')
        test.assert_equals(Struct.no, None, 'None class attribute is None')
        test.assert_equals(a.no, None, 'None class attribute is also None on an instance')
        test.assert_equals(a.no.get_change, 'INIT', 'Initial state is correct')
        a.no = None
        msg = 'None was assigned to a None class attribute on the instance'
        test.assert_equals(a.no.get_change, 'INIT', msg)
        a.no = 0
        msg = '0 was assigned to a None class attribute on the instance'
        test.assert_equals(a.no, 0, msg)
        test.assert_equals(a.no.get_change, 'MOD', msg)

    @test.it('An instance of one class is an attribute of another class')
    def it_5():
        msg = "The instance's attribute has a correct value"
        test.assert_equals(a.u.x, 4, msg)
        msg = "The instance's state is correct"
        test.assert_equals(a.u.get_change, 'INIT', msg)
        msg = "The instance's method returns a correct value"
        test.assert_equals(a.u.f(10), 14, msg)
        msg = "The instance's state didn't change after its attributes were modified"
        test.assert_equals(a.u.get_change, 'INIT', msg)
        a.u.x += 8
        test.assert_equals(a.u.x, 12, "The instance's attribute was modified")

    @test.it('Methods should work')
    def it_6():
        test.assert_equals(a.tt.get_change, '', 'Non-existent attribute has no state')
        a.f()
        msg = 'An attribute was created by a method call'
        test.assert_equals(a.tt.get_change, 'INIT', msg)
        a.f()
        msg = 'An attribute was modified by a method call'
        test.assert_equals(a.tt, 1, msg)
        test.assert_equals(a.tt.get_change, 'MOD', msg)

    @test.it('Integer and boolean tests')
    def it_7():
        @change_detection
        class H(object):
            def __init__(self):
                self.a = 0
                self.b = 1
                self.c = False
                self.d = True

        a = H()

        test.assert_equals(a.a, 0, 'Initial value is correct')
        test.assert_equals(a.a.get_change, 'INIT', 'Initial state is correct')
        test.assert_equals(a.b, 1, 'Initial value is correct')
        test.assert_equals(a.b.get_change, 'INIT', 'Initial state is correct')
        test.assert_equals(a.c, False, 'Initial value is correct')
        test.assert_equals(a.c.get_change, 'INIT', 'Initial state is correct')
        test.assert_equals(a.d, True, 'Initial value is correct')
        test.assert_equals(a.d.get_change, 'INIT', 'Initial state is correct')

        a.a = False
        msg = 'False was assigned to 0 attribute'
        test.assert_equals(a.a, False, msg)
        test.assert_equals(a.a.get_change, 'MOD', msg)
        a.b = True
        msg = 'True was assigned to 1 attribute'
        test.assert_equals(a.b, True, msg)
        test.assert_equals(a.b.get_change, 'MOD', msg)
        a.c = 0
        msg = '0 was assigned to False attribute'
        test.assert_equals(a.c, 0, msg)
        test.assert_equals(a.c.get_change, 'MOD', msg)
        a.d = 1
        msg = '1 was assigned to True attribute'
        test.assert_equals(a.d, 1, msg)
        test.assert_equals(a.d.get_change, 'MOD', msg)