def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]


def square(a):
    return a**2


applyToEach(testList, square)
print(testList)
