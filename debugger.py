# UNDONE :(
#https://www.codewars.com/kata/54bebed0d5b56c5b2600027f
from functools import wraps
import inspect


class Debugger(object):
    attribute_accesses = []
    method_calls = []


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Full name of this method: {func.__qualname__} {args} {kwargs}")
        Debugger.method_calls.append({'class': func,  # class object, not string
                                      'method': func.__qualname__.split('.')[-1],  # method name, string
                                      'args': args,  # all args, including self
                                      'kwargs': kwargs})
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class Meta(type):

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj

    def __init__(self, *args, **kwargs):
        self.__setattr__ = self.my_setattr
        self.__getattribute__ = self.my_getattribute

    def __getattribute__(self, attr):
        original = super().__getattribute__(attr)
        if attr not in ('__dict__', 'my_setattr', 'my_getattribute', '__class__', '__module__', '__name__'):
            print(' META GET ', attr)
            Debugger.attribute_accesses.append({
                'action': 'get',  # set/get
                'class': self,  # class object, not string
                'attribute': attr,  # name of attribute, string
                'value': original  # actual value
            })
        if callable(original):
            original = original.__get__(self, type(self))
            return original
        return original

    def my_setattr(self, name, value):
        print(f'set {name}={value}')
        Debugger.attribute_accesses.append({
            'action': 'set',  # set/get
            'class': self,  # class object, not string
            'attribute': name,  # name of attribute, string
            'value': value  # actual value
        })

        return super().__setattr__(name, value)

    def my_getattribute(self, attr):
        original = super().__getattribute__(attr)
        if attr not in ('__dict__', 'my_setattr', 'my_getattribute', '__class__', '__module__', '__name__'):
            Debugger.attribute_accesses.append({
                'action': 'get',  # set/get
                'class': self,  # class object, not string
                'attribute': attr,  # name of attribute, string
                'value': original  # actual value
            })
        if callable(original):
            original = original.__get__(self, type(self))
            return original
        print(f'get {attr}')
        return original
