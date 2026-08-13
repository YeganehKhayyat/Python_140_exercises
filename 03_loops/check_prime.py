# Write a Python program to Check Prime Number.

num = int(input("\nEnter a number to ckeck if It's Prime number or not : "))


for num in range(1 , num + 1):
    if num > 1 :
        
        for i in range (2 ,num ):
            if num % i == 0 :
                print(f"The {num} isn't a prime number.")
                break
        else:
            
            print(f"The {num} is a prime number.")
            break
    


                