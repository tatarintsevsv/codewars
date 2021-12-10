#https://www.codewars.com/kata/51b66044bce5799a7f000003
class RomanNumerals:

    def to_roman(val):
        print(val)
        r = (('M', 'C', 'X', 'I'),('_', 'D', 'L', 'V'))
        v = [int(v) for v in str(val)]
        while len(v)<4:
            v.insert(0,0)
        res = ''
        for i in range(4):
            s=''
            if v[i] == 9:
                s+= r[0][i]+r[0][i-1]
                v[i] -= 9
            if v[i] >=5:
                s += r[1][i]
                v[i] -= 5
            if v[i] == 4 and i != 0:
                if i!=3:
                    s += r[0][i]+r[1][i]
                else:
                    s = 'IV'
                v[i]=0
            s+= r[0][i]*v[i]
            res+=s
        return res
    def from_roman(roman_num):
        print(roman_num)
        r = {'CM': 900, 'XC': 400, 'XL': 40, 'CD': 400, 'IX': 9, 'IV': 4, 'M': 1000, 'D': 500, 'C': 100, 'XC':90,  'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sum = 0
        for p in r:
            i = -1
            while True:
                i = roman_num.find(p, i + 1)
                if i == -1:
                    break
                sum+=r[p]
            roman_num = roman_num.replace(p,'')
        return sum
