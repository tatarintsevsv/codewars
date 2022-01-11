def dbl_linear(n):
    line = {1}
    prev = 0
    while True:
        tmp = [2 * x + 1 for x in line]+[3 * x + 1 for x in line]
        line.update(set(tmp))
        if len(line)>n:
            res = sorted(list(line))
            if res[n] == prev:
                return prev
            prev = res[n]

    #for i in range(len(res)):
    #    print(f'{i}: {res[i]}',end='\n')
    return res[n]




import codewars_test as test
x = dbl_linear(300000)
print("\nx = ",x)
quit()

@test.describe("Twice linear")
def tests():
    def testing(actual, expected):
        test.assert_equals(actual, expected)

    @test.it("basic tests")
    def basics():
        testing(dbl_linear(10), 22)
        testing(dbl_linear(20), 57)
        testing(dbl_linear(30), 91)
        testing(dbl_linear(50), 175)


