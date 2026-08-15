# Write a Python Program to calculate your Body Mass Index

def body_mass_index(height , weight):
    
    b = weight / ((height) ** 2)
    return b

def description(b):
    
    if b < 18.5 :
        return "under weight"
    elif 18.5<= b <= 24.9 :
        return "normal weight"
    elif 25<= b <= 29.9:
        return "overweight"
    elif 30 <= b <= 39.9 :
        return "obesity"
    else:
        return "morbid obesity"

w = float(input("\nEnter your weight : "))
h = float(input("Enter your height : "))

bmi = body_mass_index(h , w)
print(f"\nYour body mass index is : {bmi:.3f}")
print(f"Description : {description(bmi)}")