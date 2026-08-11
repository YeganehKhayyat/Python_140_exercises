# Write a python program to do summation and division

from time import sleep

# Addition
print("===============\
        Addition\
       ===============")
num1 = float(input("Enter the first value: "))
num2 = float(input("Enter the second value: "))
summation = num1 + num2

print(f"Result: {num1} + {num2} = {summation}\n")


# Division
print("===============\
        Division\
       ===============")
num3 = float(input("Enter the first value: "))
num4 = float(input("Enter the second value: "))

condition = False
while True:
    
    if num4 != 0 :
        division = num3 / num4
        print(f"Result: {num3} / {num4} = {division}")
        break
    else:
        print("INVALID! Cannot devided to zero!!! \
please use valid number !!!")
        num4 = float(input("Enter the second value: "))
        


