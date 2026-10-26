# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name?\n")

# TODO: Ask the user for their age and store it in a variable
age = input("What is your age?\n")

# TODO: Print a greeting using the name and age variables
print("Hello, " + name + "! You are " + age + " years old!")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
rectLth = int(input("What is the length of a rectangle?\n"))

# TODO: Ask the user for the width of a rectangle and store it as an integer
rectWth = int(input("What is the width of a rectangle?\n"))

# TODO: Calculate the area of the rectangle
rectArea = rectLth * rectWth

# TODO: Print the result
print("Area: " + str(rectArea))

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
tempC = float(input("What is the temperature in Celsius?\n"))

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
tempF = (tempC * 9/5) + 32

# TODO: Print the result rounded to two decimal places
print(round(tempF, 2))
