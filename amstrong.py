# finding if a number is an armstrong number

num = int(input("Enter a number"))
sum = 0

x = num 
while x>0:
    digit = x % 10
    sum += digit**3
    x //=10

if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")