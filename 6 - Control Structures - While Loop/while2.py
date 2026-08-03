
#Create a new file called while.py.
#Write a program that always asks the user to enter a number.
#When the user enters -1, the program should stop requesting the user to enter a number,
#The program must then calculate the average of the numbers entered, excluding the -1.
#Make use of the while loop repetition structure to implement the program.
#Compile, save, and run your file.

total_user_num = 0
count = 0
user_num = 0

# Create an empty list to store the numbers
number_list = []

# Create a loop that will continue until the user enters 0 
while True:

    # Prompt the user to enter a positive number or 0 to stop
    number_input = input("Please enter a positive number or enter -1 to stop: ")
    
    # Check if the input is an integer, if so, convert it to an integer
    if number_input.isdigit():
        number_input = float(number_input)
        
        # Check if the input is 0, if so, break the loop
        if number_input != -1:
            print("You have entered -1. The program will now end.")
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

        # Account for when "+" is entered as input, eg. +6 rather than 6
        # It is still not counting as a positive number
            
    # If input is not a positive integer,
    # inform the user that their input is not a positive integer
    # Loop repeats
    else:
        print("You have not entered a positive number.")