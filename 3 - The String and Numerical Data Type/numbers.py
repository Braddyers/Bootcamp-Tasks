# Request user to input three integers
num1 = input("Enter an integer: ")
num2 = input("Enter another integer: ")
num3 = input("Enter the last integer: ")

# Cast each input into an integer
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# Calulate the sum of all integers
sum1 = num1 + num2 + num3

# Data type check
print(type(sum1))

# Calculate the difference between the first and second integer
diff1 = num1 - num2

# Calculate the product of the third and first integer
prod1 = num3 * num1

# Calculate the sume of all three integers divided by the third integer.
new_sum = sum1 / num3

# Output the answers
print(f"The sum of all numbers is: {sum1}")
print(f"The first number minus the second number is: {diff1}")
print(f"The third number multiplied by the first number is: {prod1}")
print(f"The sum of all three numbers divided by the third number is: {new_sum}")