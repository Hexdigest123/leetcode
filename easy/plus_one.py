digits_arr = [1,2,3]


def plusOne(digits):
    a = ''.join([str(i) for i in digits])
    a = str(int(a) + 1)
    a = [int(i) for i in a]
    return a


plusOne(digits_arr)
