# Write a python to display the multiplication table.

num = int(input("\nEnter a number to see It's multiplication table : "))

for i in range(0 , 11):
    print(f"{num} * {i} = {num * i}")