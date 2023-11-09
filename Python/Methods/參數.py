def sum(a, b):
    return a + b


r1 = sum(10, 15)
r2 = sum(r1, 50)


def sum1(*args):  # 放進tople
    # print(args)
    # print(type(args))
    result = 0
    for i in range(0, len(args)):
        result += args[i]
        print("\n")
        print(args[i])
        print(f"now the result is {result}")
    return result


print(sum1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def myfunc(**kwargs):  # dict
    # print(kwargs)
    # print(type(kwargs))
    print("{} is now {} years old".format(kwargs["name"], kwargs["age"]))


myfunc(name="chad", age=25, address="home")


def fun(*args, **kwargs):  # * or ** 都可自定義
    print("I would like to eat {} {}".format(args[1], kwargs["food"]))


fun(14, 17, 23, "hello", food="eggs", name="chad")


# 1. normal orgument
# 2. default orgument
# 3. *args
# 4. **kwargs
def func(p1, p2, p3="three", *args, **kwargs):
    print("---------------")
    print(p1, p2, p3, args, kwargs)


func(1, 2, 3, 4, 5, x=1, y=3)
func(1, 2, 3, 4, 5, x=4)
func(1, 2, 3, 4, 5)
func(1, 2, 3, 4)
func(1, 2, 3)
func(1, 2)
