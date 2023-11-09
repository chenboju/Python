# immutable List
myTuple = (10, "100", "hello")
print(len(myTuple))
print(myTuple[0])
print(myTuple[0:2])
print(myTuple.count(10))
print(myTuple.index("hello"))
print("\n")

# Packing and Unpacking
x = 10, 15, 59, 100  # tuple packing
print(x)
print(type(x))

y = ("chad", 25)
print(y[0])
print(y[1])
name, age = y  # tuple Unpacking
print(name)
print(age)
print("\n")

a, b = (15, 100)
print(a)
print(b)
print("\n")

c = 25
d = 35
print(c)
print(d)
# c=35 d=25
# temp = c
# c = d
# d = temp
c, d = d, c  # tuple unpackong =

# tuple packing
print(c)
print(d)
print("\n")


a = ([1, 2, 3], "chad")
print(a)
a[0][1] = 100
print(a)
