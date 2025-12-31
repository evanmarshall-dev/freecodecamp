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
print(f"Lowercase: {phrase.lower()}") # Lowercase
print(f"Uppercase then check if uppercase: {phrase.upper().isupper()}") # Uppercase then check if uppercase
print(f"Length of the string: {len(phrase)}") # Length of the string
print(f"Is the string uppercase?: {phrase.isupper()}") # Is the string uppercase?
print(f"Find the index of a character: {phrase.index('a')}") # Find the index of a character
print(f"Access a character by index: {phrase[0]}") # Access a character by index
print(f"Access a substring by index range: {phrase[0:4]}") # Access a substring by index range
print(f"Access the last 4 characters of a string: {phrase[-4:]}") # Access the last 4 characters of a string
print(f"Access the last character of a string: {phrase[-1]}") # Access the last character of a string
print(f"Replace a substring with another substring: {phrase.replace('Evan', 'Tom')}") # Replace a substring with another substring
# Numbers.
print("\n#####################################")
print("Numbers")
print("#####################################")
print(f"Integer: {2}") # Integer
print(f"Float: {2.5}") # Float
print(f"Negative float: {-2.5}") # Negative float
print(f"Addition: {3 + 4.5}") # Addition
print(f"Subtraction: {3 - 4.5}") # Subtraction
print(f"Multiplication: {3 * 4.5}") # Multiplication
print(f"Division: {3 / 4.5}") # Division
print(f"Floor division: {3 // 4}") # Floor division
print(f"Modulus: {3 % 4}") # Modulus. 4 goes into 3 zero times with a remainder of 3.
print(f"Exponentiation: {3 ** 4}") # Exponentiation
print(f"Order of operations: {3 + 4 * 2}") # Order of operations
print(f"Order of operations with parentheses: {(3 + 4) * 2}") # Order of operations with parentheses
# You can also store numbers in variables.
my_num = 5
print(f"My number: {my_num}")
print(f"{my_num} is my favorite number.") # Convert number to string for concatenation
# There are also built-in number functions.
print(f"Absolute value of -5: {abs(-5)}") # Absolute value
print(f"3 to the power of 2: {pow(3, 2)}") # Power function
print(f"Maximum of 4 and 6: {max(4, 6)}") # Maximum of two numbers
print(f"Minimum of 4 and 6: {min(4, 6)}") # Minimum of two numbers
print(f"Round 3.7 to nearest integer: {round(3.7)}") # Round to nearest integer
print(f"Round 3.2 to nearest integer: {round(3.2)}") # Round to nearest integer
# Importing math module for more advanced functions.
print(f"Floor 3.7: {floor(3.7)}") # Floor function is imported from math module and removes decimal portion.
print(f"Ceil 3.2: {ceil(3.2)}") # Ceil function is imported from math module and rounds up to nearest integer.
print(f"Square root of 36: {sqrt(36)}") # Square root function is imported from math module.

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

# Build a Mad Libs game.
print("\n#####################################")
print("Mad Libs Game")
print("#####################################")

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print(f"Roses are {color}")
print(f"{plural_noun} are blue")
print(f"I love {celebrity}")

# LISTS
# Accessing elements in a list.
print("\n#####################################")
print("List Basics")
print("#####################################")
# A list is a collection of items in a particular order.
lucky_numbers = [4, 8, 15, 16, 23, 42]
print(f"Lucky numbers: {lucky_numbers}")
# Lists can hold different data types.
mixed_list = ["Apple", 3.14, True, 42]
print(f"Mixed list: {mixed_list}")
# Accessing elements in a list.
friends = ["Kevin", "Karen", "Jim", "Karen"]
print(f"Friends list: {friends}")
# Accessing elements in a list by index.
print(f"First element in friends: {friends[0]}") # First element
print(f"Second element in friends: {friends[1]}") # Second element
print(f"Third element in friends: {friends[2]}") # Third element
print(f"Last element in friends: {friends[-1]}") # Last element
print(f"Second to last element in friends: {friends[-2]}") # Second to last element
# Slicing a list to get a sublist.
print(f"First two elements in friends: {friends[0:2]}") # First two elements
print(f"From second element to end in friends: {friends[1:]}") # From second element to end
# Modifying elements in a list.
friends[1] = "Mike"
print(f"Modified friends list: {friends}")

# List Functions.
print("\n#####################################")
print("List Functions")
print("#####################################")
# Adding elements to a list.
friends.append("Oscar") # Add to end of list
print(f"Added Oscar to friends: {friends}")
friends.insert(1, "Kelly") # Insert at index 1
print(f"Inserted Kelly at index 1 in friends: {friends}")
# Removing elements from a list.
friends.remove("Jim") # Remove by value
print(f"Removed Jim from friends: {friends}")
# ? friends.clear() # Clear the list
# ? print(f"Cleared friends list: {friends}")
friends.pop() # Remove last element
print(f"Removed last element from friends: {friends}")
# Finding the index of an element in a list.
print(f"Index of Kevin in friends: {friends.index('Kevin')}")
# Checking if an element is in a list.
print(f"Is Kevin in friends: {'Kevin' in friends}")
print(f"Is Jim in friends: {'Jim' in friends}")
friends.count("Karen") # Count occurrences of an element
print(f"Number of times Karen appears in friends: {friends.count('Karen')}")
# Getting the length of a list.
print(f"Length of friends list: {len(friends)}")
# Sorting a list.
friends.sort()
print(f"Sorted friends list: {friends}")
# Reversing a list.
lucky_numbers.reverse()
print(f"Reversed lucky numbers list: {lucky_numbers}")
# Copying a list.
friends2 = friends.copy()
print(f"Copied friends list: {friends2}")
friends.extend(lucky_numbers) # Extend friends list with lucky_numbers list
print(f"Extended friends list with lucky numbers: {friends}")

# Tuples.
print("\n#####################################")
print("Tuple Basics")
print("#####################################")