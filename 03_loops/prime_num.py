# Write a python program to print all Prime Number is an interval of 1-10

a = 1
b = 10
list1 = []
for num in range(a , b + 1):
    if num > 1 :
        
        for i in range (2 ,num ):
            if num % i == 0 :
                break
        else:
            
            print(num)
        