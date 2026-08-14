# # Write a Python Program to Find Armstrong Number in an Interval.

a = int(input("\nEnter the lower limit: "))
b = int(input("Enter the upper limit: "))

for num in range (a , b + 1):

    p = len(str(num))
    temp = num
    s = 0

    while temp > 0:
        d = temp % 10
        s += d ** p
        temp //= 10
        
    if s == num :
        print(num)
        


    