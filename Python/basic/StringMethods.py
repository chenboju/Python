print(len(""))

print(int("200"))
# print(int("two hundred"))
# print(int("30.5"))
print("\n")


name = "chAd"
print(name.upper())  # 全大寫
print(name.lower())  # 全小寫
print("\n")

print(name.isupper())
print(name.upper().isupper())
print(name.islower())
print("\n")

print(name.index("d"))


print(name.replace("d", "A"))

sentence = "Today is a good"
print(sentence.split(" "))
print(sentence.split("a"))

print(list(sentence))
print("\n")

# sent = "I have a string {}".format("here it is")
# sent = "I have a string {}".format("15")
sent = "I have a string {}".format("[a,b,c,a,ed,f]")
print(sent)
print("{},{},{}".format(20, "here is another string", 3.14))
print("{2},{1},{0}".format(20, "here is another string", 3.14))
print("{2},{1},{3}".format(20, "here is another string", 3.14, 50))
print("{h1},{h2},{address}".format(h1="chad", h2=20, address="infotmation management"))
print("\n")

myName = "chad"
Age = 25
# f-string
print(f"hello my name is {myName}, I am {Age} years old")
print("\n")

string = "Good day is a good day"
print(string.count("good"))
print(string.lower().count("good"))
print(string.find("to"))  # 找不出來不會跑出error
print(string.find("day"))
print("\n")


print(name.startswith("C"))
print(name.endswith("d"))
print(name.endswith("ad"))
print("\n")

name1 = "Sam Donaldson"
name1 = "P" + name1[1:]
print(name1)
print("\n")


print("chad\n" * 10)  # 只能乘整數
