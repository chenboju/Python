# Position and Key Arguments


def exponent(a, b):
    return a**b


# position
print(exponent(2, 3))  # 8
print(exponent(3, 2))  # 9

# key 順序可自行調整
print(exponent(a=10, b=2))
print(exponent(b=2, a=10))


myList = [4, 6, 3, 2, 1]
print(sorted(myList, reverse=False))
print(sorted(myList, reverse=True))
