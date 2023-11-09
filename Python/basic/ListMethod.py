friends = ["chad", "Mike", "Bob", "Jimmy"]
friends.insert(2, "Aaeon")
print(friends)

friends.remove("chad")
print(friends)

# friends.clear()
# print(friends)

friends.sort()  # 直接更改記憶體位置
print(friends)

friends.reverse()
# friends=friends[::-1]
print(friends)

friends.append("chad")
number = 15, 30
friends.append(number)
print(friends)
muLost = friends.pop()
print(friends)
print(muLost)
print("\n")


# copy by reference  list dictionaries tuples sets
x = [1, 2, 3, 4, 5, 6, 7]
y = x  # y=[1,2,3,4,5,6,7]
# y[0] = 15
print(x)
print(y)

print("--------------")
# copy by value int float str bool  primitiue data type
a = 10
b = a
b = 15
print(a)
print(b)

print("\n")

y = x.copy()
print(y)
y[0] = 15
print(x)
print(y)

# List of List
z = [1, 2, [3, 4, 5], [6, 7, 8]]
print(z)
print(z[2][1])
print(z[len(z) - 1])
