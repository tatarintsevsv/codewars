#https://www.codewars.com/kata/52742f58faf5485cae000b9a
def format_duration(seconds):
    if seconds==0:
        return 'now'
    sec = seconds % 60
    seconds = seconds // 60
    min = seconds % 60
    seconds = seconds // 60
    hour = seconds % 24
    seconds = seconds // 24
    day = seconds % 365
    seconds = seconds // 365
    year=seconds
    res=[]
    if sec != 0:
        res.append(str(sec) + (' second' if sec==1 else ' seconds'))
    if min != 0:
        res.append(str(min) + (' minute' if min == 1 else ' minutes'))
    if hour != 0:
        res.append(str(hour) + (' hour' if hour == 1 else ' hours'))
    if day != 0:
        res.append(str(day) + (' day' if day == 1 else ' days'))
    if year != 0:
        res.append(str(year) + (' year' if year == 1 else ' years'))
    return ('{} and {}'.format(', '.join(res[::-1][:-1]),res[0])) if len(res)>1 else res[0]
