#Program Starting 
print("Program Starting")

#What is your name
Name = input("What is your name")

#Enter a floating point number
First_number = float(input("Enter a floating point number"))

#Enter second floating number
Second_number = float(input("Enter second floating number"))

# John you gave numbers 3.1 and 5.3 
print(f"{Name} you gave numbers {First_number} and {Second_number}")

#Multiplying first and second number will result in product 16.43
Product = First_number * Second_number
print(f"Multiplying first and second number will result in product {round(Product, 2) }")

#Program ending
print("Program ending")