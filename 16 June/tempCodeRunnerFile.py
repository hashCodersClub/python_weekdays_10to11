def fact():
    num = int(input("Enter a num : "))#4
    factorial = 1
    for i in range(2,num+1):
        factorial = factorial * i 

    print(f"factorial of {num} is {factorial}")

fact()