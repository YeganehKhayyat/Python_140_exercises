# Write a Python Program to find sum of array

list1 = input("Enetr the numbers seprated by space : ").split()

summation  = 0
for item in list1:
    summation += float(item)
    
print(f"The summation of items in your list is : {summation}")
    
