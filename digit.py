# finding the amount of digits in a number with a loop

x = float(input("Enter any number that is not to big:"))
digit = 0
num = x

if num == 0:
    digit = 1
else:
    while num>0:
        num //=10
        digit+=1


print("The number", x, "has", digit, "digits")

