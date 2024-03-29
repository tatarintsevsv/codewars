# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

def pick_peaks(arr):
    print(arr)
    res = {"pos":[],"peaks":[]}
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i - 1]:
            pl = 0
            while arr[i + pl] == arr[i] and (i + pl) < len(arr) - 1:
                pl += 1
            if arr[i + pl] < arr[i]:
                res["pos"].append(i)
                res["peaks"].append(arr[i])

    return res


import codewars_test as test

#[-1, 17, 16, 8, 12, 15, 17, 2, 20, 17, -4, 8, 18, 1, 3, -1, 20, 10]
test.assert_equals(pick_peaks([-1, 17, 16, 8, 12, 15, 17, 2, 20, 17, -4, 8, 18, 1, 3, -1, 20, 10]), {'pos': [1, 6, 8, 12, 14, 16], 'peaks': [17, 17, 20, 18, 3, 20]})
quit()
test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
test.assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})
test.assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})