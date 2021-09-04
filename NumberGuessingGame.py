import random

n = random.randint(0, 100)
# print(n)
while(True):
    num=int(input("Enter a number between 0 to 100"))
    if num==n:
        print("Hurray! You got it right")
        break
    elif num>n:
        print("You entered a greater number")
        continue
    elif num<n:
        print("You entered a smaller number")
        continue
    else:
        print("something wrong entered")
        continue