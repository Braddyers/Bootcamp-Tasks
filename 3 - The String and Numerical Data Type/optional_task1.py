# Load in math module to import math functions
import math

# Request user input for lengths of the sides of a triangle
side1 = float(input("Enter the length of the first side of a triangle: "))
side2 = float(input("Enter the length of the second side of a triangle: "))
side3 = float(input("Enter the length of the third side of a triangle: "))

# Calculate the semi-perimeter (s)
s = (side1 + side2 + side3) / 2

# Calculate the area of the triangle
area1 = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Output the area of the triangle             
print(f"The area of the triangle is: {area1}")