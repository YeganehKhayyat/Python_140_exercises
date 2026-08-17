# Write a Python Program to calculate the natural logarithm of any number.

import math

num = float(input("\nEnter a number to calculate it's log : "))
while True :
    if num > 0 :
        break
    else:
        print("ERROR!!!")
        num = float(input("Enter a number to calculate it's log : "))

print(f"Natural logarithm of {num} is : {math.log(num)}")