from itertools import permutations
from collections import defaultdict
d = defaultdict(list)


def print_arr(arr, clues, rewrite=True):
    if rewrite:
        print("\033[%d;%dH" % (0, 0))
        for i in range(10):
            print('                                                   ')
        print("\033[%d;%dH" % (0, 0))
    print('   '+' '.join([str(x) for x in clues[:6]]))
    for i in range(6):
        ss = ''.join([str(x) + ' ' for x in arr[i]])
        print(str(clues[23-i])+'  '+ss+'  '+str(clues[6+i]))
    l = '   '+' '.join([str(clues[17-x]) for x in range(6)])
    print(l,'                             \n')

def get_h(s):
    m, v, mr, vr = 0, 0, 0, 0
    for i in range(len(s)):
        if int(s[i]) > m:
            m = int(s[i])
            v += 1
        if int(s[len(s) - i - 1]) > mr:
            mr = int(s[len(s) - i - 1])
            vr += 1
    return str(v) + str(vr)

def gen_vars():
    for v in permutations('123456'):
        h = get_h(v)
        vstr = ''.join(v)
        d[h].append(vstr)
        d['0'+h[1]].append(vstr)
        d[h[0]+'0'].append(vstr)
        d['00'].append(vstr)

gen_vars()


def solve_puzzle (clues):
    def get_clue(i, is_row):
        return (str(clues[23 - i]) + str(str(clues[6 + i]))) if not is_row else (str(clues[i]) + str(str(clues[17 - i])))

    def check_clues():
        res = True
        for i in range(6):
            if ''.join([arr[x][i] for x in range(len(arr))]) not in d[get_clue(i,True)] or arr[i] not in d[get_clue(i,False)]:
                res = False
        return res

    def check():
        for i in range(6):
            for j in range(6):
                row = [arr[x][i] for x in range(len(arr))]
                if row.count(row[j]) > 1 and row[j] != '.':
                    return False
                if arr[i].count(arr[i][j]) > 1 and arr[i][j] != '.':
                    return False
        return True

    def get_max():
        max = -1
        max_clue = '00'
        is_row = False
        for i in range(6):
            if arr[i].count('.') == 0:
                continue
            idx = str(clues[23 - i]) + str(str(clues[6 + i]))
            if len(d[idx])<=len(d[max_clue]):
                    max, max_clue, is_row = i, idx, False
        for i in range(6):
            if [arr[x][i] for x in range(len(arr))].count('.') == 0:
                continue
            idxr = str(clues[i]) + str(str(clues[17 - i]))
            if len(d[idxr])<=len(d[max_clue]):
                    max, max_clue, is_row = i, idxr, True
        return max, is_row

    def set_val(idx, is_row, val, reset=False):
        if is_row:
            new_val = [val[x] if arr[x][idx] in (val[x],'.') else 'X' for x in range(len(arr))]
            old_val = [arr[x][idx] for x in range(len(arr))]
            if new_val.count('X')>0 and not reset:
                return []
            for i in range(len(arr)):
                arr[i] = arr[i][:idx]+val[i]+arr[i][idx+1:]
        else:
            new_val = [val[x] if arr[idx][x] in (val[x],'.') else 'X' for x in range(len(arr))]
            old_val = arr[idx]
            if new_val.count('X')>0 and not reset:
                return []
            arr[idx] = val
        return old_val

    def set_line(pos, arr,depth=1):
        i, is_row = pos
        old_val = '......'
        idx = get_clue(i, is_row)
        for v in d[idx]:
            old_val = ''.join(set_val(i, is_row, v))
            if len(old_val) == 0:
                continue
            if not check():
                set_val(i, is_row, old_val, reset=True)
                continue
            max = get_max()
            if max[0] != -1:
                set_line(max, arr,depth+1)
            if ''.join(arr).count('.') == 0:
                if check_clues():
                    return
            set_val(i, is_row, old_val,reset=True)
        if get_max()[0] == -1:
            return
        return
        #arr[i] = set_val(i, is_row, old_val)
    arr = ['.'*6]*6
    set_line(get_max(), arr)
    return tuple([tuple([int(y) for y in x]) for x in arr])
