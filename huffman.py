# https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d/train/python

def gencodes(freqs):
    fx = [x for x in freqs]
    codes = {x[0]: "" for x in fx}
    while len(fx) > 1:
        fx.sort(key=lambda x: x[1])
        l = fx.pop(0)
        r = fx.pop(0)
        fx.append((l[0]+r[0],l[1]+r[1]))
        for c in codes:
            if c in l[0]:
                codes[c] = '1' + codes[c]
            if c in r[0]:
                codes[c] = '0' + codes[c]
    return codes


def frequencies(s):
    fx = []
    while len(s) > 0:
        fx.append((s[0],s.count(s[0])))
        s = s.replace(s[0],'')
    return fx


def encode(freqs, s):
    if len(freqs)<2:
        return None
    codes = gencodes(freqs)
    return ''.join(codes[c] for c in s)


def decode(freqs, bits):
    if len(freqs)<2:
        return None
    codes = {y:x for x,y in gencodes(freqs).items()}
    res = ''
    tmp = ''
    while len(bits):
        tmp += bits[0]
        bits = bits[1:]
        if tmp in codes:
            res +=codes[tmp]
            tmp=''
    return res

import codewars_test as test

test.describe("basic tests")
fs = frequencies("aaaabcc")
test.it("aaaabcc encoded should have length 10")
def test_len(res):
    test.assert_not_equals(res, None)
    test.assert_equals(len(res), 10)
test_len(encode(fs, "aaaabcc"))
s = encode(fs, "aaaabcc")
s = decode(fs,s)
test.it("empty list encode")
test.assert_equals(encode(fs, []), '')

test.it("empty list decode")
test.assert_equals(decode(fs, []), '')

def test_enc_len(fs, strs, lens):
    def enc_len(s):
        return len(encode(fs, s))
    test.assert_equals(list(map(enc_len, strs)), lens)

test.describe("length")
test.it("equal lengths with same frequencies if alphabet size is a power of two")
test_enc_len([('a', 1), ('b', 1)], ["a", "b"], [1, 1])

test.it("smaller length for higher frequency, if size of alphabet is not power of two")
test_enc_len([('a', 1), ('b', 1), ('c', 2)], ["a", "b", "c"], [2, 2, 1])

test.describe("error handling")
s = "aaaabcc"
fs = frequencies(s)
test.assert_equals( sorted(fs), [ ("a",4), ("b",1), ("c",2) ] )
test_enc_len(fs, [s], [10])
test.assert_equals( encode( fs, "" ), "" )
test.assert_equals( decode( fs, "" ), "" )

test.assert_equals( encode( [], "" ), None );
test.assert_equals( decode( [], "" ), None );
test.assert_equals( encode( [('a', 1)], "" ), None );
test.assert_equals( decode( [('a', 1)], "" ), None );