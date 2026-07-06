# Scenario 1:

# An algorithm that asks a user to enter a positive number repeatedly
# until the user enters a zero value, then determines and outputs the
# largest of the numbers that were input.


# Name variable for input numbers and create a list to store number inputs
number_input = 0
number_list = []

# prompt user for user input 
number_input = int(input(print("Please enter a number > 0 or enter 0 to stop: ")))

# If user enters a number that is not zero
while number_input != 0:
    # add the number to the list
    number_list.append(number_input)
    # let user know the number has been added to the list
    print("")
    # prompt user again for user input 
    number_input = int(input(print("That number has been added to the list. Please enter another number > 0 or enter 0 to stop: ")))

else:
    print("You have entered zero and the program will now end.")