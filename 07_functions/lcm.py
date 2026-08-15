# Write a Python Program to Find LCM.

def lcm(num1, num2):
    if num1 > num2 :
        num1 , num2 = num2 , num1
    for i in range(num2, num1 * num2 + 1, num2):
        if i % num1 == 0 :
            return i
        
x = int(input("\nEnter the first number to calculate : "))
y = int(input("\nEnter the second number to calculate : "))
print(lcm(x , y))
