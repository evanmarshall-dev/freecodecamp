from math import *

# Basics.
print("#####################################")
print("Basics")
print("#####################################")
# Test.
print("Hello world!")

# Draw a triangle.
print("   /\\   ")
print("  /  \\  ")
print(" /    \\ ")
print("/______\\")

# Variables.
print("\n#####################################")
print("Variables")
print("#####################################")
# If we want to change the name or age later, we only have to do it in one place.
character_name = "Evan"
character_age = 39
# Can also store boolean values.
is_male = True
print("There once was a " + ("man" if is_male else "woman") + " named " + character_name + ".")
print("He was " + str(character_age) + " years old.")
# If you want to change the name halfway through, you can just reassign the variable.
character_name = "Tom"
print("He really liked the name " + character_name + ".")
print("But didn't like being " + str(character_age) + ".")

# Strings.
print("\n#####################################")
print("Strings")
print("#####################################")
# Anything after a backslash (or escape character) will be explicitly interpreted.
# A backslash followed by n means a new line.
# A backslash followed by " means to print a double quote.
# You can also store a string inside a variable.
phrase = "Evan is awesome!"
print(phrase + " But I am tired of typing that out.") # Concatenate strings with +
print("Evan\nis\n\"awesome.\"")
# There is also built in string functions and chains of functions.
print(phrase.lower()) # Lowercase
print(phrase.upper().isupper()) # Uppercase then check if uppercase
print(len(phrase)) # Length of the string
print(phrase.isupper()) # Is the string uppercase?
print(phrase.index("a")) # Find the index of a character
print(phrase[0]) # Access a character by index
print(phrase[0:4]) # Access a substring by index range
print(phrase[-4:]) # Access the last 4 characters of a string
print(phrase[-1]) # Access the last character of a string
print(phrase.replace("Evan", "Tom")) # Replace a substring with another substring

# Numbers.
print("\n#####################################")
print("Numbers")
print("#####################################")
print(2) # Integer
print(2.5) # Float
print(-2.5) # Negative float
print(3 + 4.5) # Addition
print(3 - 4.5) # Subtraction
print(3 * 4.5) # Multiplication
print(3 / 4.5) # Division
print(3 // 4) # Floor division
print(3 % 4) # Modulus. 4 goes into 3 zero times with a remainder of 3.
print(3 ** 4) # Exponentiation
print(3 + 4 * 2) # Order of operations
print((3 + 4) * 2) # Order of operations with parentheses
# You can also store numbers in variables.
my_num = 5
print(my_num)
print(str(my_num) + " is my favorite number.") # Convert number to string for concatenation
# There are also built-in number functions.
print(abs(-5)) # Absolute value
print(pow(3, 2)) # Power function
print(max(4, 6)) # Maximum of two numbers
print(min(4, 6)) # Minimum of two numbers
print(round(3.7)) # Round to nearest integer
print(round(3.2)) # Round to nearest integer
# Importing math module for more advanced functions.
print(floor(3.7)) # Floor function is imported from math module and removes decimal portion.
print(ceil(3.2)) # Ceil function is imported from math module and rounds up to nearest integer.
print(sqrt(36)) # Square root function is imported from math module.

# Numbers.
print("\n#####################################")
print("User Input")
print("#####################################")
# Take input from user and store in a variable.
name = input("Enter your name: ")
# Make it so that it only accepts age as a number.
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age.")
print("Hello " + name + "! You are " + str(age) + " years old.")
# Refactor the above to use template strings (f-strings).
print(f"Hello {name}! You are {age} years old.")

# Build a Basic Calculator.
print("\n#####################################")
print("Basic Calculator")
print("#####################################")
# Take input from user for two numbers.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = float(num1) + float(num2) # Convert input strings to floats and add them and ensures numerical addition and not string concatenation. Python by default treats input as strings. Could also use int() to convert to integers, but with int() you can't do decimal numbers.
print(f"{num1} + {num2} = {result}")
# ? print(f"{num1} - {num2} = {num1 - num2}")
# ? print(f"{num1} * {num2} = {num1 * num2}")
# ? print(f"{num1} / {num2} = {num1 / num2}")