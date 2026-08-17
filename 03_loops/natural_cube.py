# Write a Python Program for cube sum of first n natural numbers

summation = 0 
num = int(input("\nEnter a number to calculate the cube summation : "))

for i in range(1 , num + 1):
    summation += i ** 3

print(f"The first {num} of cube summation : {summation}")

# You can write this program in a function !!! No limitation in coding :)