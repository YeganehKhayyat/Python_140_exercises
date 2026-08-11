import math

print("Format of quadratic equation is : ax^2 + bx + c = 0\n")
a = float(input("Enter a amount: "))
b = float(input("Enter b amount: "))
c = float(input("Enter c amount: "))

while a == 0 :
    print("It's quadratic equation please give an a variable true amount:\n " )
    a = float(input("Enter a amount: "))
    
x1 = 0      # first root
x2 = 0      # second root

delta = (b ** 2 ) - (4 *( a * c))

if delta > 0 :
    x1 = ( -b + math.sqrt(delta)) / (2 * a)
    x2 = ( -b - math.sqrt(delta)) / (2 * a)
    print(f"First root is {x1} and second root is {x2}.")
elif delta == 0 :
    x1 = -b / (2 * a)
    print(f"The amount of root is {x1}")
else:
    print("This equation doesn't have any roots.")
