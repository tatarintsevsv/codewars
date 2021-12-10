#https://www.codewars.com/kata/55983863da40caa2c900004e
def next_bigger(n):
    a = ['0']+list(str(n))
    for i in range(len(a)-2,0,-1):
        tail = [a[i]]+sorted(a[i+1:])
        for j in range(len(tail)):
            if tail[j]>tail[0]:
                tail[j], tail[0] = tail[0], tail[j]
                break
        x = int(''.join(a[:i]+tail))
        if x>n:
            return x
    return -1
