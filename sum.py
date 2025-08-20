# finding the sum of numbers with the while loop
num = int(input("Enter the number of numbers to find the sum of"))
f = 1
sum = 0
while f<num:
    sum = sum + f
    f = f + 1
    
print("The sum of your numbers you entered is", sum)