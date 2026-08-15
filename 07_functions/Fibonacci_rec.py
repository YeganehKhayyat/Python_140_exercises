# Write a Python Program to Display Fibonacci Sequence Using Recursion.

def fibonacci_rec(num):
    if num <2 :
        return num
    else:
        return (fibonacci_rec(num - 1) + fibonacci_rec(num - 2))
    
n = int(input("\nEnter a number to see it's Fibonacci Sequence : "))

while True :
    
    if n < 0 :
        print("Please enter a positive or 0 number.")
        n = int(input("\nEnter a number to see it's Fibonacci Sequence : "))
    else:
        break
    
print(fibonacci_rec(n))