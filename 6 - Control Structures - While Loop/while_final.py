# Initialize variables
total_user_num = 0
count = 0
user_num = 0

# Ask the user to input a number
user_num = (input("Please enter a number (-1 to stop): "))

while True:
    user_num = (input("Please enter a number (-1 to stop): "))

    if user_num.isdigit and user_num.startswith('-') and user_num[1:].isdigit():
        print(user_num)
        print("yes it is an integer")

    else:
        print(user_num)
        print("No that is not an integer")