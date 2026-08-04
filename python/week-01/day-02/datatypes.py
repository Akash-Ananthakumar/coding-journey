name = "Akash"      #string
age = 24            #integer
height = 174.5      #float
is_student = True   #boolean

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print(age)

age = 25

print(age)  #always uses the latest value of the variable

name = input("Enter your name: ")
print("Hello", name, "!") #user input

#input() function always returns a string. If you want to take an integer input, you need to convert it using int() function.
year = (input("Enter your birth year: "))
print(type(year)) #string
year = int(year) #converting string to integer
print(type(year))
print(year)

#converting between data types is called type casting. We can convert between data types using the following functions:
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean

#why converting between data types is important?
#1. To perform mathematical operations, we need to convert strings to numbers.

age = input("Enter your age: ")

#print(age + 5) #this will give an error because age is a string and we cannot add a string and an integer.

age = int(age) #converting string to integer 

print(age + 5) #this will now work correctly

#Multiple inputs in a single line
name, age = input("Enter your name and age: ").split() #split() function
age = int(age) #converting string to integer
print("Hello", name, "! You are", age, "years old.")

#split() function splits the input string into a list of strings based on the specified delimiter (default is space). In this case, we are splitting the input into two parts: name and age.

