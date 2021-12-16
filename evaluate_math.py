# https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python
import re


class Node:
    verbose = False

    def __str__(self):
        return f'{self.desc}'

    def _can_break_brackets(self,value):
        if (value[0] != '(' and value[:2] != '-(') or value[len(value) - 1] != ')':
            return False
        brackets=0
        for i in range(len(value)):
            if value[i] == '(':
                brackets += 1
            if value[i] == ')':
                brackets -= 1
                if brackets == 0 and i<len(value)-1:
                    return False
        return True

    def __init__(self,value, prefix=''):
        self.desc = value
        if self._can_break_brackets(value) and value[0]=='(':
            self.value = "+"
            self.left = Node("0")
            self.right = Node(value[1:-1], prefix+'  ')
            return
        if self._can_break_brackets(value) and value[:2] == '-(':
            self.value = "-"
            self.left = Node("0")
            self.right = Node(value[2:-1], prefix+'  ')
            return
        brackets = 0
        right=''
        for i in range(len(value)-1, 0, -1):
            if value[i] == ')':
                brackets += 1
            if value[i] == '(':
                brackets -= 1
            if value[i] in ('+', '-') and brackets == 0 and right != '' and value[i-1] not in ('-','+','*','/'):
                self.value = value[i]
                if self.verbose:
                    print(f'{prefix}|create node "{value}"')
                    print(f'{prefix}|value: "{value[i]}"')
                    print(f'{prefix}|with left: "{value[:i]}"')
                    print(f'{prefix}|and right: "{right}"')
                self.left = Node(value[:i],prefix+'  ')
                self.right = Node(right,prefix+'  ')
                return
            right = value[i]+right
        right = ''
        brackets = 0
        for i in range(len(value)-1, 0, -1):
            if value[i] == ')':
                brackets += 1
            if value[i] == '(':
                brackets -= 1
            if value[i] in ('*', '/') and brackets == 0:
                self.value = value[i]
                if self.verbose:
                    print(f'{prefix}|create node "{value}"')
                    print(f'{prefix}|value: "{value[i]}"')
                    print(f'{prefix}|with left: "{value[:i]}"')
                    print(f'{prefix}|and right: "{right}"')
                self.left = Node(value[:i], prefix+'  ')
                self.right = Node(right, prefix+'  ')
                return
            right = value[i]+right

        if self.verbose:
            print(f'{prefix}|create node "{value}"')
        self.value = value
        return


def DFS(node):
    #if hasattr(node,"left"):
    #    print(f'calc="{node.left}" {node.value} "{node.right}"')
    if node.value == "/":
        return DFS(node.left)/DFS(node.right)
    if node.value == "*":
        return DFS(node.left)*DFS(node.right)
    if node.value == "+":
        return DFS(node.left)+DFS(node.right)
    if node.value == "-":
        return DFS(node.left)-DFS(node.right)
    return float(node.value)


def calc(expression):
    print(expression)
    if len(re.findall('[\\+\\-\\*\\/]\\s*- [\\d(]', expression)) > 0:
        print('err')
        return 0
    expression = expression.replace(' ','')
    root = Node(expression)
    res = DFS(root)
    return float(res)


print(calc("(-2) / (-3 + 65 / (79)) / (35 - (((-(71 * -70)))) * 87)"))
quit()

import codewars_test as test

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        cases = (
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14),
            ("93 + -91 / 4 + -73 / -56 - 53 - 23 + 17", 5.3)
        )

        for x, y in cases:
            test.assert_equals(calc(x), y)
            print('==========')

x = (-2) / (-3 + 65 / (79)) / (35 - (((-(71 * -70)))) * 87)