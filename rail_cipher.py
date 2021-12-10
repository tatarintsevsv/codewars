#https://www.codewars.com/kata/58c5577d61aefcf3ff000081
def getset(res,string,n):
    d = 1
    s = 0
    retstr = ''
    for i in range(len(res[0])):
        if len(string)>0:
            res[s][i] = string[i]
        else:
            retstr+=res[s][i]
        if s in (0, n - 1) and i != 0:
            d *= -1
        s += d
    return retstr

def encode_rail_fence_cipher(string, n):
    try:
        if n==1:
            return string
        res = []
        for i in range(n):
            res.append(['' for j in range(len(string))])
        getset(res, string, n)
        return ''.join([''.join(res[i]) for i in range(n)])
    except Exception as e:
        print(f'Error with params: "{string}",{n}')


def decode_rail_fence_cipher(string, n):
    try:
        if n==1:
            return string
        res = []
        for i in range(n):
            res.append(['' for j in range(len(string))])
        getset(res, "X" * len(string), n)
        tmps = string
        for i in range(n):
            for j in range(len(string)):
                if res[i][j] == 'X':
                    res[i][j] = tmps[0]
                    tmps = tmps[1:]
        return getset(res, '', n)
    except Exception as e:
        print(f'Error with params: "{string}",{n}')
