# Asks for the user's name. Asks for their age. Asks for their favorite programming language.
name, age, program = input("Enter your name, age and you favorite programming language: ").split(",")

name = name.strip() # removing any leading/trailing whitespace
age = int(age.strip()) #converting string to integer and removing any leading/trailing whitespace
program = program.strip() # removing any leading/trailing whitespace

print("Your name is", name, ", Your age is", age, "and your favorite programming language is", program)