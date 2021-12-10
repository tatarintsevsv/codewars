#https://www.codewars.com/kata/52cf02cd825aef67070008fa
import string
from collections import defaultdict
def getChar(s, p):
    for c in alphabet:
        if alphabet[c][p] == s:
            return c
    return '_'
alphabet = defaultdict(str)
for i in range(67):
    for a in string.ascii_lowercase + string.ascii_uppercase + string.digits + ' ,.?!':
        alphabet[a]+=encode(' ' * i + a)[-1]
newalpha = defaultdict(str)
for a in alphabet:
    for i in range(len(alphabet)):
        newalpha[a] += getChar(a, i)
alphabet = newalpha

def decode(s):    
    res = ''    
    for i in range(len(s)):
        res += alphabet[s[i]][i%66] if s[i] in alphabet else s[i]
    return res
