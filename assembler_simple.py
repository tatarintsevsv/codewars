# https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python

def simple_assembler(program):
	def check_int(s):
		if s[0] in ('-', '+'):
			return s[1:].isdigit()
		return s.isdigit()

	i = 0
	regs = {}
	while i < len(program):
		cmd = program[i].split(' ')
		if cmd[0] == 'mov':
			regs[cmd[1]] = int(cmd[2]) if check_int(cmd[2]) else regs[cmd[2]]
		if cmd[0] == 'inc':
			regs[cmd[1]] += 1
		if cmd[0] == 'dec':
			regs[cmd[1]] -= 1
		if cmd[0] == 'jnz':
			if (int(cmd[1]) if check_int(cmd[1]) else regs[cmd[1]]) != 0:
				i += int(cmd[2]) if check_int(cmd[2]) else regs[cmd[2]]
				continue
		i += 1
	return regs


import codewars_test as test


@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
        test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})

        code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
        test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})