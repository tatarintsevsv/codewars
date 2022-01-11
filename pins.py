# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

def get_pins(observed,res=[]):
    key_var = {
        '1': ('1', '2', '4'),
        '2': ('1', '2', '3', '5'),
        '3': ('2', '3', '6'),
        '4': ('1', '4', '7', '5'),
        '5': ('2', '4', '5', '6', '8'),
        '6': ('3', '5', '6', '9'),
        '7': ('4', '7', '8'),
        '8': ('5', '7', '8', '9', '0'),
        '9': ('6', '8', '9'),
        '0': ('8', '0')
    }
    if len(res)==0:
        res = [x for x in key_var[observed[0]]]
    else:
        res = [y+x for y in res for x in key_var[observed[0]]]
    if len(observed)>1:
        res = get_pins(observed[1:],res)
    return res



import codewars_test as test
test.describe('example tests')
expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

for tup in expectations:
  test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])