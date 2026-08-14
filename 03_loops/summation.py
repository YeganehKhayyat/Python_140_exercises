# Write a python program to find the sum of natural numbers.

_range = int(input("Enter a number to find the summation: "))
summation = 0

for i in range(1, _range + 1):
    summation += i
    
print(f"The summation of {_range} is: {summation} ")