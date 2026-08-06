# Takes the user's name.
# Takes two numbers.
# Prints:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# Floor Division
# Power

name = input("Enter your name: ")

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

print(f"\nHello {name}!\n")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)