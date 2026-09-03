num1 = input("Enter an integer: ")
num2 = input("Enter another integer: ")
num3 = input("Enter the last integer: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

sum1 = num1 + num2 + num3

print(f"The sum of all numbers is {sum1}")

print(f"The first number minus the second number is {num1 - num2}")

print(f"The third number multiplied by the first number is {num3 * num1}")

print(f"The sum of all three numbers divided by the third number is {int(sum1 / num3)}")