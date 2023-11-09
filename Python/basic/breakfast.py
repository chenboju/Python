name = input("Enter your name:")  # input -> string
# print("Your name is " + name)
money = input("Eeter your cash money:")
hungry = input("Are you hungry ? (Y/N)")

if hungry == "Y":
    if int(money) >= 30:
        {print(f"{name} should go eat breakfast")}
    else:
        {print(f"{name} is hungry but not have enough money")}
elif hungry == "N":
    if int(money) >= 30:
        {print(f"{name} 不想吃早餐")}
    else:
        {print(f"{name} 沒錢但不餓")}
else:
    {print("Please input Y or N")}
