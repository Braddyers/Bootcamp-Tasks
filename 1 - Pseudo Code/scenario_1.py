# Scenario 1:

# An algorithm that asks a user to enter a positive number repeatedly
# until the user enters a zero value, then determines and outputs the
# largest of the numbers that were input.


# Create an empty list to store the numbers
number_list = []

# Create a loop that will continue until the user enters 0 
while True:

    # Prompt the user to enter a positive number or 0 to stop
    number_input = input("Please enter a number > 0 or enter 0 to stop: ")
    
    # Check if the input is an integer, if so, convert it to an integer
    if number_input.isdigit():
        number_input = int(number_input)
        
        # Check if the input is 0, if so, break the loop
        if number_input == 0:
            print("You have entered 0. The program will now end.")
            break
        
        # Check if the input is a positive integer, if so, add it to the list
        elif number_input > 0:
            number_list.append(number_input)
            
            # A check if the list is correctly storing the numbers 
            # print(number_list)
            
            # Inform the user that the positive integer has been added to the list
            print(f"'{number_input}' has been added to the list.")

            # Inform the user of the largest number in the list
            print(f"The largest number on the list is: {max(number_list)}.")
            
    # Inform the user that their input is not a positive integer and request another input
    else:
        print("You have not entered a positive number. Please try again.")