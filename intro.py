# function - use functions on the top - use def instead of function

def test():
    print("I am a function")


def separator():
    print("------------")


print("Hello, Python")

# single line comment
# how to declare a variable
name = "Mike"
last = "Sadler"
age = 36
found = False
total = 23.50
products = []  # arrays are called list in Python

print(name)
print(name + " " + last)
# Use this method to parse an integer with a string. Cannot add a str and an int together without this
print(name + str(age))

separator()  # calling the function

# Math operations - + / * %

# python code blocks start with : Must use one indent and there are no {}
# else if is elif in python

if(age < 80):
    print("You are still young!")
elif(age == 80):
    print("Else if you are still old!")
else:
    print("You are really old!")

separator()  # calling the function
