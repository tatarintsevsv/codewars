from collections import defaultdict


def recoverSecret(triplets):
    chars = set(''.join(''.join(x) for x in triplets))
    d = {c:[] for c in chars}
    for t in triplets:
        d[t[0]].append(t[1])
        d[t[0]].append(t[2])
        d[t[1]].append(t[2])
        d[t[0]] = list(dict.fromkeys(d[t[0]]))
        d[t[1]] = list(dict.fromkeys(d[t[1]]))
    print(d)
    tail = ''
    while len(chars) > 0:
        m = ''
        for c in chars:
            if len(d[c])==0:
                tail = c + tail
                chars.remove(c)
                m = c
                break
        for k in d:
            if m in d[k]:
                d[k].remove(m)
    return ''.join(chars)+tail


import codewars_test as test

secret = "whatisup"
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

test.assert_equals(recoverSecret(triplets), secret)
