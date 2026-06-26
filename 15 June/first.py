# num1 -> 15, num2 -> 19, num3 -> 17
# if-elif-else

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if num1 < num2:
    if num3 < num2:
        print("num2 is largest")
    else:
        print("num3 is largest")
else:
    if num3 < num1:
        print("num1 is largest")
    else:
        print("num3 is largest")


