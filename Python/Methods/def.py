def hello():
    print("hello")


print(hello)
hello()


# addition(paramter參數)
def addition(x, y):
    print(x + y)


addition(10, 5)  # 10 5 are the arguments

a = 10
b = 100
addition(a, b)  # 10 5 are the arguments


# global variables  , local variables
a = 10  # global variables  全域變數


def f1():
    x = 2  # local variables 區域變數
    y = 3
    print(x, y, a)


f1()


def f2():
    x = 10  # local variables 區域變數
    y = 17
    print(x, y, a)


f2()


a = 10


def change(num):
    # num=a (copt by value) 先發生這行
    # num = 20

    global a
    a = 25


change(a)
print(a)

a1 = [1, 2, 3, 4]


def change1(list):
    list[0] = 100  # (copy by reference)


change1(a1)
print(a1)


def myaddition(a, b):
    """ "This fountion does addition for inputs a and b"""
    print(a + b)


help(myaddition)
