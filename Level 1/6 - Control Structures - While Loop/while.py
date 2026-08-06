# Initialise variables
total_user_num = 0
input_count = 0
user_num = 0

# Request input of a number, -1 to stop program
user_num = input("Please enter a number (-1 to stop): ")

# Initiate while loop
while True:

    # If input is a digit, convert to float
    if user_num.lstrip('+-').replace('.', '', 1).isdigit():
        user_num = float(user_num)

        # if input is not -1
        if user_num != -1:

            # Output to user that the input was a valid number
            print("You have entered a valid number.")

            # Add input to total and increase the count
            total_user_num += user_num
            input_count += 1

            # Prompt for another input
            user_num = input("Please enter another number (-1 to stop): ")

        # If input = -1
        if user_num == -1:

            # Output to user that the program will end 
            print("You have entered -1. The program will now end.")

            # Calculate and output average of input numbers 
            # excluding the -1 input
            print("The average of the numbers you have entered " +
                  f"is: {total_user_num / input_count}")
            break

# If not an integer, convert request another input
    else:
        print("That is not a number.")
        user_num = input("Please enter a number (-1 to stop): ")