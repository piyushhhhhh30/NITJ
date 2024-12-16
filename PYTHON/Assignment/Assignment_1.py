#1. Write a program to calculate the distance between two points.
import math

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Input points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate and display the distance
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between the points is: {distance}")
print("-----------------------------------------------------------------")

# -------- Write a program to calculate the area of a triangle using Heron's formula.-------- #
def calculate_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Input sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if the inputs can form a valid triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    # Calculate and display the area
    area = calculate_area(a, b, c)
    print(f"The area of the triangle is: {area}")
else:
    print("The input values cannot form a valid triangle.")
print("-----------------------------------------------------------------")

# Given two variables, a = 7 and b = 3, write a Program to swap their values without using a temporary variable. What will be the values of a and b after the swap?

# Initial values
a = 7
b = 3

# Swapping values without using a temporary variable
a, b = b, a

# Display the values after swapping
print(f"After swapping: a = {a}, b = {b}")

print("-----------------------------------------------------------------")

# Given a list of numbers = [10, 20, 30, 40, 50], write a Python code to calculate the average of these numbers using arithmetic operators.
# Given list of numbers
numbers = [10, 20, 30, 40, 50]

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Calculate the count of numbers
count = len(numbers)

# Calculate the average
average = total_sum / count

# Print the average
print(f"The average of the numbers is: {average}")

print("-----------------------------------------------------------------")

# Write a simple basic calculator program in python
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4): ")

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")