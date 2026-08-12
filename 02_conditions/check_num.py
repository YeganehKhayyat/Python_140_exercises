# Write a python program to check if a number is +, - or 0.

num = float(input("\nEnter a number to guess the type: "))

if num > 0 :
    print("\n Positive number !!!")
elif num == 0 :
    print("\n Zero !!!")
else:
    print("\n negative number !!!")