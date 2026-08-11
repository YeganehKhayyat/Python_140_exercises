# Write a python program to swap two variables.


var1 = float(input("Enter the first variable : "))
var2 = float(input("Enter the second variable : "))

print(f"First variable = {var1}, Second variable = {var2}")
print("\nlet's swap the variables !!!")

var2 , var1 = var1 , var2

print(f"\nFirst variable = {var1}, Second variable = {var2}")
