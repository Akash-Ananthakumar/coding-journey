# if condition
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")

# if-else condition
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else condition
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# nested if condition
age = int(input("Enter your age: "))
if age >= 18:
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

# logical operators
# and operator

age = int(input("Enter your age: "))
if age >= 18 and age < 65:
    print("You are an adult.")

# or operator
age = int(input("Enter your age: "))
if age < 13 or age >= 65:
    print("You are either a child or a senior citizen.")

# not operator
age = int(input("Enter your age: "))
if not (age < 18):
    print("You are an adult.")

# ternary operator
age = int(input("Enter your age: "))
status = "You are an adult." if age >= 18 else "You are not an adult."
print(status)

# Membership operators
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list.")
if "grape" not in fruits:
    print("Grape is not in the list.")

# the [] is used to create a list in Python. A list is a collection of items that can be of different data types, such as integers, strings, or even other lists. Lists are ordered, changeable (mutable), and allow duplicate values. You can access elements in a list using their index, which starts at 0 for the first element.

# Identity operators
x = 10
y = 10
if x is y:
    print("x and y are the same object.")

