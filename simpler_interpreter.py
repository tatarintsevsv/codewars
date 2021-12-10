#https://www.codewars.com/kata/53005a7b26d12be55c000243
import re
from collections import defaultdict

class Interpreter:
    def __init__(self):
        self.vars = defaultdict(int)

    def isIdentifer(self, s):
        return re.match('[A-Z\\_][\w]{0,}$', s.upper()).string == s.upper()

    def replaceVars(self,s):
        for v in self.vars:
            s = s.replace(v,str(self.vars[v]))
        return s
    def calc(self,s):
        if s=='':
            return 0
        i = s.find('(')
        while i!=-1:
            ic = 0
            ii = i
            while ii<len(s):
                if s[ii] == '(': ic += 1
                if s[ii] == ')': ic -= 1
                if ic==0:
                    break
                ii += 1
            subs = s[i:ii+1]
            if subs[0]=='(' and subs[-1]==')':
                r = self.calc(subs[1:-1])
                s = s.replace(subs,str(r))
            else:
                raise NameError('expression error')
            i = s.find('(')

        for op in ['+','-','*','/','%']:
            p = [x.lstrip().rstrip() for x in s.split(op)]
            if len(p) > 1:
                if len(p) == 1 and op == '-':
                    p.insert(0, '0')
                if op == '+': t = 0
                if op == '*': t = 1
                if op in ('-', '/', '%'): t = None
                for x in p:
                    if op == '+': t += self.calc(x)
                    if op == '-':
                        z = self.calc(x)
                        if t != None:
                            t -= z
                        else:
                            t = z
                    if op == '*': t *= self.calc(x)
                    if op in ('/','%'):
                        z = self.calc(x)
                        if t != None:
                            if op == '/': t /= z
                            if op == '%': t %= z
                        else:
                            t = z

                return int(t)
        return int(s)


    def input(self, expression):
        if expression.rstrip().lstrip()=='':
            return ''
        if expression.find('=') != -1:
            p = [x.lstrip().rstrip() for x in expression.split('=')]
            if len(p)!=2 or not self.isIdentifer(p[0]):
                raise NameError('expression error')
            try:
                res = self.calc(self.replaceVars(p[1]))
                self.vars[p[0]] = res
                return res
            except Exception as e:
                raise NameError('expression error')
        try:
            res = self.calc(self.replaceVars(expression))
            return res
        except Exception as e:
            raise NameError('expression error')
