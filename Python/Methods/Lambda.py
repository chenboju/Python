# lambda variable :operation

result = (lambda x: x**2)(5)
print(result)

myTuple = (lambda x, y: (x + y, x - y))(15, 30)
print(myTuple[0])
print(myTuple[1])


for item in map(lambda x: x**2, [12, 10, 5]):
    print(item)

for item in filter(lambda x: x % 2 == 0, [12, 10, 5]):
    print(item)
