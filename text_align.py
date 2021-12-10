#https://www.codewars.com/kata/537e18b6147aa838f600001b
def justify(text, width):
    print(width,text)
    res = ''
    words = text.split(' ')
    while len(' '.join(words))>width:
        i = 1
        while len(' '.join(words[:i])) <= width and len(words) > i:
            i += 1
        if i > 2:
            line = words[:i - 1]
            words = words[i-1:]
            sc = 0
            while True:
                sc += 1
                if len(str(' '*sc).join(line))>=width:
                    sc -= 1
                    break
            if width > len(str(' '* sc).join(line)):
                for i in range(len(line)-1):
                    line[i] += ' '                    
                    if len(str(' '*sc).join(line))==width:
                        break
            res += str(' '*sc).join(line) + '\n'
        else:
            res += words[0]+'\n'
            words = words[1:]
    res+=' '.join(words)
    return res
