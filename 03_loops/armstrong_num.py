# Write a python program to check if input is an armstrong number or not

number = input("\nEnter a number to Check if It's armstrong or not: ")
answer = 0 

for num in number :
    answer += (int(num) ** len(number))
    
    
if answer == int(number) :
    print(f"\n{answer} is an armstrong number.")
else:
    print(f"\n{answer} isn't an armstrong number.")
    