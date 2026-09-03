import math

side_1 = float(input("Enter the length of the first side of a triangle: "))
side_2 = float(input("Enter the length of the second side of a triangle: "))
side_3 = float(input("Enter the length of the third side of a triangle: "))

s = (side_1 + side_2 + side_3) / 2

tri_area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
# an error returned the first time I ran the area calculation: "name 'math' is not defined"
# I looked up the problem online and found that I first needed to import the 'math' module to provide the needed mathematical function
                     
print(f"The area of the triangle is: {tri_area}")