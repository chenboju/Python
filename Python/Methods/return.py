def myAddition(a, b):
    # print(a + b)
    return a + b


myAddition(26, 16)
myAddition(10, 18)
myAddition(15, 17)
print(myAddition(26, 16) + myAddition(10, 18) + myAddition(15, 17))


def myAddition1(a, b):
    result = a + b
    print(result)
    return result
    # print(result)


myAddition1(10, 14657)


def myAddition2(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return
            print(i, j)


myAddition2(5, 10)
print("\n")
print(myAddition2(5, 10))
