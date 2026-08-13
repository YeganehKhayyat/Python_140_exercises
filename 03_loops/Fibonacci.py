# Write a python program to print the Fibonacci sequence.

num = int(input("\nEnter a number to calculate Fibonacci sequence : "))
if num == 0 or 1 :
    print("")
f1 = 0
print(f1)
f2 = 1
print(f2)

temp = f1 + f2
print(temp)

for i in range (4 , num + 1):
    
    f1 = f2
    f2 = temp
    temp = f1 + f2
    print(temp)
    
    
