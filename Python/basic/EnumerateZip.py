counter = 0
# enumerate
for letter in "How are you today":
    if counter < 10:
        print(letter)
    counter += 1
print("\n")

for item in enumerate("How are you today"):
    print(item)  # 組成tuple
print("\n")

for counter, char in enumerate("How are you today"):
    if counter < 10:
        print(char)

# zip
x = [1, 2, 3]
y = ["A", "b", "C"]
z = [9, 6, "Z", "s"]
for tuple in zip(x, y):  # 組成tuple
    print(tuple)
print("\n")

for tuple in zip(x, y, z):  # 組成tuple
    print(tuple)
