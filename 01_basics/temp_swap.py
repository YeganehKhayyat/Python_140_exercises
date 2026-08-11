# Write a python program to swap two variable with temp.
print("Let's swap two variables !!!\n")

num1 = float(input("enter your first number : "))
num2 = float(input("enter your second number : "))

temp = 0
temp = num1
num1 = num2
num2 = temp

print(f"Now the first value is {num1} and the second value is {num2}.")