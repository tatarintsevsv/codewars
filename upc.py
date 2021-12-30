# https://www.codewars.com/kata/5b7dfd8cbfae24e5f200004d
# than
# https://www.codewars.com/kata/5bb2e1bfad558fc09d000063/train/python


def scanner(barcode):
    return read_barcode(barcode)


def read_barcode(barcode):
    d = {'L': {'0001101': '0',
                 '0011001': '1',
                 '0010011': '2',
                 '0111101': '3',
                 '0100011': '4',
                 '0110001': '5',
                 '0101111': '6',
                 '0111011': '7',
                 '0110111': '8',
                 '0001011': '9'},
         'R': {'1110010': '0',
               '1100110': '1',
               '1101100': '2',
               '1000010': '3',
               '1011100': '4',
               '1001110': '5',
               '1010000': '6',
               '1000100': '7',
               '1001000': '8',
               '1110100': '9'}
         }

    x = ''.join(['0' if c==' ' else '1' for c in barcode])[3:-3]
    backwards = False
    if not x[:7] in d['L']:
        backwards = True
        x = x[::-1]

    res_l = ''
    res_r = ''
    while len(x)>5:
        if backwards:
            res_l = res_l + d['R'][x[-7:]]
            res_r = d['L'][x[:7]] + res_r
        else:
            res_l = res_l + d['L'][x[:7]]
            res_r = d['R'][x[-7:]] + res_r
        x = x[7:-7]

    tmp = res_l+res_r if not backwards else (res_l+res_r)[::-1]
    # check
    o1=sum([int(tmp[x]) for x in range(len(tmp)) if x%2==0])*3
    o2=sum([int(tmp[x]) for x in range(1,len(tmp)-1) if x%2==1])
    M = (o1+o2) % 10
    if M != 0:
        M = 10 - M
    if int(tmp[-1])!=M:
        return 'error'
    res = f'{tmp[0]} {tmp[1:6]} {tmp[6:11]} {tmp[-1]}'
    return res

import codewars_test as test
# simple reader
'''
test.py.describe('should convert barcode to digits')

test.py.it("Campbell's Chicken Noodle Soup")
test.py.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'), '0 51000 01251 7')

test.py.it("Hershey's Natural Unsweetened Cocoa")
test.py.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍   ▍▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍▍▍  ▍ ▍ ▍▍▍  ▍ ▍'), '0 34000 05200 4')

test.py.it("Bob's Red Mill Corn Grits")
test.py.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍   ▍ ▍▍   ▍ ▍▍ ▍▍▍ ▍▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍ ▍▍  ▍ ▍'), '0 39978 00125 2')

test.py.it("Dutch Gold Pure Buckwheat Honey ")
test.py.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍▍▍▍ ▍  ▍▍  ▍ ▍▍▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍ ▍▍▍  ▍▍  ▍▍ ▍▍▍  ▍ ▍   ▍  ▍ ▍'), '0 73138 20410 7')

test.py.it("Black Bear Spicy Brown Mustard")
test.py.assert_equals(read_barcode('▍ ▍ ▍ ▍▍▍▍ ▍▍▍▍ ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍ ▍ ▍▍▍ ▍  ▍▍  ▍▍ ▍ ▍▍▍  ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍    ▍ ▍'), '6 30003 91455 6')

test.py.it("Barilla Fideo Cut Spaghetti Pasta")
test.py.assert_equals(read_barcode('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍ ▍▍▍▍ ▍▍ ▍▍▍   ▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍   ▍  ▍    ▍ ▍    ▍ ▍ ▍'), '0 76808 00073 3')

'''
# advanced

test.describe('should convert barcode to digits')
test.it("Campbell's Chicken Noodle Soup")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'), '0 51000 01251 7')

test.it("Hershey's Natural Unsweetened Cocoa")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍   ▍▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍▍▍  ▍ ▍ ▍▍▍  ▍ ▍'), '0 34000 05200 4')

test.it("Bob's Red Mill Corn Grits")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍   ▍ ▍▍   ▍ ▍▍ ▍▍▍ ▍▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍ ▍▍  ▍ ▍'), '0 39978 00125 2')

test.it("Dutch Gold Pure Buckwheat Honey ")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍▍▍▍ ▍  ▍▍  ▍ ▍▍▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍ ▍▍  ▍▍▍  ▍ ▍ ▍▍▍  ▍▍  ▍▍ ▍▍▍  ▍ ▍   ▍  ▍ ▍'), '0 73138 20410 7')

test.it("Black Bear Spicy Brown Mustard")
test.assert_equals(scanner('▍ ▍ ▍ ▍▍▍▍ ▍▍▍▍ ▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍ ▍ ▍▍▍ ▍  ▍▍  ▍▍ ▍ ▍▍▍  ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍    ▍ ▍'), '6 30003 91455 6')

test.it("Barilla Fideo Cut Spaghetti Pasta")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍ ▍▍▍▍ ▍▍ ▍▍▍   ▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍   ▍  ▍    ▍ ▍    ▍ ▍ ▍'), '0 76808 00073 3')


test.describe('should read backwards')
test.it("Campbell's Chicken Noodle Soup")
test.assert_equals(scanner('▍ ▍  ▍   ▍ ▍▍  ▍▍ ▍▍▍  ▍  ▍▍ ▍▍ ▍▍  ▍▍ ▍  ▍▍▍ ▍ ▍ ▍ ▍▍   ▍ ▍▍   ▍ ▍▍   ▍  ▍▍  ▍   ▍▍ ▍ ▍▍   ▍ ▍'), '0 51000 01251 7')

test.it("Hershey's Natural Unsweetened Cocoa")
test.assert_equals(scanner('▍ ▍  ▍▍▍ ▍ ▍  ▍▍▍ ▍  ▍▍▍  ▍▍ ▍▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍ ▍ ▍ ▍▍   ▍ ▍▍   ▍ ▍▍   ▍▍   ▍ ▍ ▍▍▍▍ ▍ ▍▍   ▍ ▍'), '0 34000 05200 4')

test.it("Bob's Red Mill Corn Grits")
test.assert_equals(scanner('▍ ▍  ▍▍ ▍▍ ▍▍▍  ▍  ▍▍ ▍▍ ▍▍  ▍▍ ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍ ▍▍▍ ▍▍ ▍▍ ▍▍▍ ▍▍ ▍   ▍▍ ▍   ▍ ▍▍▍▍ ▍ ▍▍   ▍ ▍'), '0 39978 00125 2')

test.it("Dutch Gold Pure Buckwheat Honey ")
test.assert_equals(scanner('▍ ▍  ▍   ▍ ▍  ▍▍▍ ▍▍  ▍▍  ▍▍▍ ▍ ▍  ▍▍▍  ▍▍ ▍▍ ▍ ▍ ▍▍▍ ▍▍ ▍ ▍▍▍▍ ▍  ▍▍  ▍ ▍▍▍▍ ▍▍ ▍▍▍ ▍ ▍▍   ▍ ▍'), '0 73138 20410 7')

test.it("Black Bear Spicy Brown Mustard")
test.assert_equals(scanner('▍ ▍    ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍  ▍▍▍ ▍ ▍▍  ▍▍  ▍ ▍▍▍ ▍ ▍ ▍ ▍▍▍▍ ▍ ▍▍   ▍ ▍▍   ▍ ▍▍   ▍ ▍▍▍▍ ▍▍▍▍ ▍ ▍ ▍'), '6 30003 91455 6')

test.it("Barilla Fideo Cut Spaghetti Pasta")
test.assert_equals(scanner('▍ ▍ ▍    ▍ ▍    ▍  ▍   ▍ ▍  ▍▍▍ ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍ ▍▍▍ ▍▍ ▍ ▍▍   ▍▍▍ ▍▍ ▍▍▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍▍   ▍ ▍'), '0 76808 00073 3')


test.describe('check digit verification should fail')
test.it("Campbell's Not Chicken Noodle Soup")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍   ▍  ▍▍  ▍  ▍▍  ▍  ▍▍  ▍  ▍▍  ▍ ▍ ▍ ▍▍▍  ▍ ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍  ▍▍ ▍   ▍  ▍ ▍'), 'error')

test.it("Hershey's Unnatural Unsweetened Cocoa")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍ ▍   ▍▍   ▍▍ ▍   ▍▍ ▍   ▍▍ ▍ ▍ ▍ ▍▍▍  ▍ ▍  ▍▍▍ ▍▍ ▍▍  ▍▍▍ ▍  ▍▍▍ ▍  ▍  ▍▍▍ ▍ ▍'), 'error')

test.it("Bob's Brown Mill Pea Grease")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍▍ ▍  ▍▍  ▍  ▍▍  ▍ ▍▍▍ ▍▍ ▍▍ ▍▍▍ ▍ ▍ ▍ ▍    ▍ ▍    ▍▍  ▍▍ ▍▍ ▍▍  ▍  ▍▍▍ ▍▍ ▍▍  ▍ ▍'), 'error')

test.it("Dutch Bronze Impure Buckwheat Honey")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍  ▍▍  ▍  ▍▍  ▍ ▍▍▍ ▍▍ ▍▍▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍    ▍ ▍▍▍  ▍ ▍ ▍▍▍  ▍▍  ▍▍ ▍▍▍  ▍ ▍   ▍  ▍ ▍'), 'error')

test.it("White Bear Spicy Purple Mustard")
test.assert_equals(scanner('▍ ▍ ▍ ▍▍▍▍ ▍▍▍▍ ▍   ▍▍ ▍  ▍▍  ▍  ▍  ▍▍ ▍▍▍▍ ▍ ▍ ▍ ▍▍▍ ▍  ▍▍  ▍▍ ▍ ▍▍▍  ▍  ▍▍▍ ▍  ▍▍▍ ▍ ▍    ▍ ▍'), 'error')

test.it("Barilla Fideo Cut Onion Paste")
test.assert_equals(scanner('▍ ▍   ▍▍ ▍ ▍▍▍ ▍▍ ▍ ▍▍▍▍ ▍▍ ▍▍▍   ▍▍ ▍ ▍▍ ▍▍▍ ▍ ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍▍▍  ▍ ▍   ▍  ▍    ▍ ▍▍  ▍▍ ▍ ▍'), 'error')
