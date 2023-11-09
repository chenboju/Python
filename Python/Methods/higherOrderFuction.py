def higherOrder(fn):
    fn()


def smallfunc():
    print("hello from small function")


higherOrder(smallfunc)


def square(num):
    return num**2


myList = [-10, 3, 9, 8, 10]
print(map(square, myList))

for item in map(square, myList):
    print(item)


def even(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False


List = [235664, 1254568869, 24312415]

for item in filter(even, List):  # filter(true or false, List):
    print(item)
