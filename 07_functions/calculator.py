# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.

def summation(num1 , num2 , op):
    op = "+"
    return float (num1) + float(num2)

def subtract(num1 , num2 , op):
    op = "-"
    return float(num1) - float(num2)

def multiply(num1 ,num2 , op):
    op = "*"
    return float(num1) * float(num2)

def divide(num1 , num2 , op):
    op = "/"
    try :
        if num2 != 0 :
            return float(num1)/ float(num2) 
    except ZeroDivisionError :
        return "ERROR! divided by ZERO."
        
    
print("***Calculator***")
    
x , y , z = map(str, input().split())

while True :
    if y == "+":
        print(summation(x , z , y))
        break
    elif y == "-":
        print(subtract(x , z , y))
        break
    elif y == "*":
        print(multiply(x , z , y))
        break
    elif y == "/":
        print(divide(x , z , y))
        break
    else :
        print("Undefined sign!!!")
        x , y , z = map(str, input().split())




