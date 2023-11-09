x = [1, 2, 3, 4]
y = []
for i in x:
    y.append(i**2)

print(y)

# list comprehensions  python 特有寫法
# new list = [operation for variable in ortginal_list if condition]

z = [item**2 for item in x if item >= 2]
print(z)

# dictionary
# new dict = {key : value(operation) for variable in original_dict if condition}
a = {item: item**2 for item in x}
print(a)
a1 = {item: item**2 for item in x if item > 2}
print(a1)

# set
# new_set = {operation for variable in original_set if condition}
b = {item**2 for item in x if item > 2}
print(b)
b1 = {item**2 for item in x}
print(b1)


# generator
x_generator = (item**2 for item in x)
print(x_generator)

for i in x_generator:
    print(i)
