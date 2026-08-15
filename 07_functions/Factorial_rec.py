# Write a Python Program to Find Factorial of Number Using Recursion.

def factorial_rec(num):
    if num == 1 :
        return num
    else:
        return(num * factorial_rec(num - 1))
    
n = int(input("\nEnter a number to calculate factorial : "))

while True :
    if n < 0 :
        print("Please enter a positive or 0 number.")
        n = int(input("\nEnter a number to calculate factorial : "))
    else:
        break
    
print(f"The factorial of {n} is : {factorial_rec(n)}")