# 順序不重要的集合
mySet = set()
print(mySet)
mySet1 = set({1, 2, 3, 4, 5, 6})
print(mySet1)

myList = [1, 2, 3, 6, 7, 8, 4, 7, 9]
mySet = set(myList)
print(mySet)

s = set()
s.add(1)
print(s)
s.add(2)
s.add(3)
s.discard(1)
print(s)
s.clear()
print(s)
print("\n")

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a.difference(b))  # a-b
print(b.difference(a))  # b-a
print(a.intersection(b))  # 重複數字
print(b.intersection(a))
print(a.union(b))  # 聯集
print(b.union(a))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))
