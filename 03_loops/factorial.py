# Write a Python program to find the factorial of the number

num = int(input("Enter a number to calculate factorial of number : "))
answer = 1
for i in range(1 , num + 1):
     answer = answer * i
     
print(answer)