#  for variable in iterable:
#      do somestiob hrer
for letter in "hello":
    print(letter)
    print(letter.upper())
    if letter == letter.upper():
        {print(letter)}

myList = [1, 3, 5, 7, 9]

for num in myList:
    {print(num**2)}

print("\n")

# tuple
for tuple in [(1, 2), (3, 5), (5, 7)]:
    print(tuple)

print("\n")

for a, b in [(1, 2), (3, 5), (5, 7)]:
    print(a, b)
    print(a + b)

# dict
myDict = {"name": "chad", "age": 25}
for item in myDict:
    print(item)


for item in myDict.values():
    print(item)

for item in myDict.items():
    print(item)

for key, value in myDict.items():
    print(f"The key is {key}")
    print(f"The value is {value}")

# set
for i in {1, 3, 5, 6, 7, 8}:
    print(i)

print("\n")

x = 0
while x < 5:
    print(x)
    x = x + 1

for i in "1234":
    for j in "ABCDEFG":
        print(i, j)

for i in "How are you?":
    pass
print("Hello")
print("\n")

for i in "Howareyou?":
    print(i)
    if i == "y":
        break
print("Hello")
print("\n")

for i in "12345678":
    for j in "abcdefg":
        if j == "c":
            break
        print(i, j)
print("\n")

for i in "12345678":
    for j in "abcdefg":
        if j == "c":
            continue
        print(i, j)
