# https://www.codewars.com/kata/56e02d5f2ebcd50083001300/train/python

class Property:
    def __new__(cls, *args, **kwargs):
        t = type(args)
        return super(t, cls).__new__(cls,args,kwargs)

    def __init__(self, *args, **kwargs):
        self.get_change = "INIT"
        self.value = args


class Decorator:
    def __init__(self,cls):
        self._obj = cls

    def __getattr__(self, item):
        #print(f" GET {item}")
        if item == "_obj":
            return self._obj
        return Property(getattr(self._obj, item))

    def __setattr__(self, key, value):
        if key != '_obj':
            print(f"SET {key}={value}")
            #old = getattr(self._obj, key)
            #if old != value:
            #    old.get_change = "MOD"
            return super(type(self._obj),self._obj).__setattr__(key, value)
        return super(Decorator, self).__setattr__(key, value)


def change_detection(cls):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        return Decorator(cls(*args, **kwargs))
    return a_wrapper_accepting_arbitrary_arguments


@change_detection
class Struct:
    x = 42
    no = None

    def __init__(self, y=0):
        self.y = y
        #self.u = U(4)
        self.uuu = None

    def f(self):
        if self.tt.get_change:
            self.tt += 1
        else:
            self.tt = 0


a = Struct(11)
print(a.x)
a.x = 12
xx = a.x
print(xx,a.x.get_change)
#print(a.x,a.uuu)
