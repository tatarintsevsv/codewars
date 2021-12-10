#https://www.codewars.com/kata/58e61f3d8ff24f774400002c
regs = {}
cmpres = 0
result = ''

def assembler_interpreter(program, line=0,begin=True):
    global result
    if begin:
        print(program)
        regs.clear()
        result = ''
    def mov(params):
        tmp = [x.strip() for x in params.strip().split(',')]
        if tmp[1].isnumeric():
            regs[tmp[0]] = int(tmp[1])
        else:
            if tmp[1] not in regs:
                regs[tmp[1]] = 0
            regs[tmp[0]] = regs[tmp[1]]

    def add(params, op):
        if op in ('inc','dec'):
            params += ',1'
            op = 'add' if op == 'inc' else 'sub'
        tmp = [x.strip() for x in params.strip().split(',')]
        arg = int(tmp[1]) if tmp[1].lstrip('+-').isnumeric() else regs[tmp[1]]
        if op in ('add','sub'):
            regs[tmp[0]] = regs[tmp[0]]+arg if op == 'add' else regs[tmp[0]]-arg
        if op in ('mul','div'):
            regs[tmp[0]] = regs[tmp[0]] * arg if op=='mul' else int(regs[tmp[0]] // arg)

    def cmp(params):
        tmp = [x.strip() for x in params.strip().split(',')]
        arg1 = int(tmp[0]) if tmp[0].lstrip('+-').isnumeric() else regs[tmp[0]]
        arg2 = int(tmp[1]) if tmp[1].lstrip('+-').isnumeric() else regs[tmp[1]]
        return arg1-arg2

    def get_label_line(lbl):
        line = -1
        lbl = lbl.strip()
        for i in range(len(commands)):
            if commands[i].strip()[:len(lbl)+1] == (lbl+':'):
                line = i
                break
        return line

    def jmp(cmd, lbl):
        #global cmpres
        line = get_label_line(lbl)
        retline = False
        if cmd == 'jmp'\
            or (cmd == 'jne' and cmpres != 0)\
            or (cmd == 'je' and cmpres == 0)\
            or (cmd == 'jge' and cmpres >= 0)\
            or (cmd == 'jg' and cmpres > 0)\
            or (cmd == 'jle' and cmpres <= 0)\
            or (cmd == 'jl' and cmpres < 0):
            return line
        return -1

    def msg(params):
        global result
        global regs
        quotes = False
        params = params.strip()+','
        p = ''
        for i in range(len(params)):
            if params[i] == '\'':
                quotes = not quotes
                if not quotes:
                    result += p
                    p=''
                continue
            if quotes:
                p+=params[i]
                continue
            if params[i] == ' ':
                continue
            if params[i] == ',':
                if p != '':
                    result += str(regs[p])
                p=''
                continue
            p+=params[i]


    def remove_comments(s):
        quotes = False
        for i in range(len(s)):
            if s[i]==';' and not quotes:
                return s[:i].strip()
            if s[i]=='\'':
                quotes = not quotes
        return s
    commands = program.split('\n')
    i = line
    while i<len(commands):
        cmd = remove_comments(commands[i]).strip().split(' ')
        params = ' '.join(cmd[1:]) if len(cmd)>1 else []
        i += 1
        if cmd[0] == '':
            continue
        #print(i-1, commands[i-1], regs)
        if cmd[0] == 'mov':
            mov(params)
            continue
        if cmd[0] in ('add', 'sub', 'inc', 'dec', 'mul', 'div'):
            add(params, cmd[0])
            continue
        if cmd[0] == 'cmp':
            cmpres = cmp(params)
            continue
        if cmd[0] in ('jmp','jne', 'je', 'jge', 'jg','jle', 'jl'):
            line = jmp(cmd[0],params)
            if line != -1:
                i = line
            continue
        if cmd[0] == 'call':
            line = get_label_line(params)
            if line != -1:
                if assembler_interpreter(program, line, begin=False) <= 0:
                    return -1
                continue
        if cmd[0] == 'msg':
            msg(params)
            continue
        if cmd[0] == 'ret':
            return 1
        if cmd[0] == 'end':
            return result
    return -1
