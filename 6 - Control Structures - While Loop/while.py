#Initialize variables
total_user_num = 0
count = 0
user_num = 0

#Ask the user to input a number
user_num = (input("Please enter a number (-1 to stop): "))

#To make sure the user inputs a valid number:
while not (user_num.replace('.', '', 1).isdigit() or (user_num.startswith('-') and user_num[1:].replace('.', '', 1).isdigit())):
        print("Invalid input. Please enter a valid number.")
        user_num = input("Please enter a number (-1 to stop): ")

#Convert valid input into a float
user_num = float(user_num)

#Need to repeat the loop until the user enters -1 (excludes -1 from the average calculation)
while user_num != -1:

    #Incrementing everytime another input is added
    total_user_num += user_num
    count += 1

    #Ask the user to input a valid number again
    user_num = (input("Please enter a number (-1 to stop): "))

    #To make sure that the user inputs a valid number again
    while not (user_num.replace('.', '', 1).isdigit() or (user_num.startswith('-') and user_num[1:].replace('.', '', 1).isdigit())):
        print("Invalid input. Please enter a valid number.")
        user_num = input("Please enter a number (-1 to stop): ")

    #Convert valid input into a float
    user_num = float(user_num)

    #To prevent division by zero
    if count > 0:
        average_user_num = total_user_num / count

#Display the average of inputs
print("The average of your inputs is: " + str(average_user_num))