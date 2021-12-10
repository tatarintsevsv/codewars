def simplify(poly):
    if poly[0] not in ['-','+']:
        poly = '+'+poly
    parts={}
    maxlen=0
    for p in poly.replace('-','.-').replace('+','.+').split('.')[1:]:
        if len(p.split('^'))>1:
            power = '^'+p.split('^')[1]
            p = p.split('^')[0]
        else:
            power = ''
        key = ''.join(sorted(filter(str.islower, p)))+power
        count = ''.join(filter(lambda x: x.isdigit() or x in ['-','+'], p))
        part = parts[key] if key in parts else {'count':0}
        if count in ['-','+']:
            count+='1'
        part['count'] = part['count']+int(count)
        parts[key] = part
        maxlen = max(maxlen,len(key))
    s_parts = {}
    for i in range(maxlen):
        keys = [x for x in parts if len(x)==i+1]
        for k in sorted(keys):
            s_parts[k] = parts[k]
    s = '.'.join((str(parts[x]['count']) if abs(parts[x]['count']) != 1 else ('-' if parts[x]['count'] == -1 else '')) +x for x in s_parts if s_parts[x]['count']!=0)
    s = s.replace('.-','-').replace('.','+')
    return s
