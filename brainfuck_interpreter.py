# https://www.codewars.com/kata/526156943dfe7ce06200063e/train/python

mem = [0] * 30000
i = 0
inp = ''


def brain_luck(code, program_input):
    x = 0
    global i
    global inp
    if len(program_input)>0:
        inp = program_input
    output = ''
    while x < len(code):
        c = code[x]
        if c == '>':
            i += 1
        if c == '<':
            i -= 1
        if c == '+':
            mem[i] = (mem[i] + 1) if mem[i] < 255 else 0
        if c == '-':
            mem[i] = (mem[i] - 1) if mem[i] > 0 else 255
        if c == '.':
            output += chr(mem[i])
        if c == ',':
            mem[i] = ord(inp[0])
            inp = inp[1:]
        if c == '[':
            while mem[i] != 0:
                output += brain_luck(code[x+1:],'')
            n = 1
            while n > 0:
                x += 1
                n += 1 if code[x] == '[' else -1 if code[x] == ']' else 0
        if c == ']':
            return output
        x += 1
    return output

import codewars_test as test

# Echo until byte(255) encountered
test.assert_equals(
    brain_luck(',+[-.,+]', 'Codewars' + chr(255)),
    'Codewars'
);

# Echo until byte(0) encountered
test.assert_equals(
    brain_luck(',[.[-],]', 'Codewars' + chr(0)),
    'Codewars'
);

# Two numbers multiplier
test.assert_equals(
    brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),
    chr(72)
)
