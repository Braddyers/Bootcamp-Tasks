# Scenario 1:

# An algorithm that asks a user to enter a positive number repeatedly
# until the user enters a zero value, then determines and outputs the
# largest of the numbers that were input.

number_list = []


while True:
    number_input = input("Please enter a number > 0 or enter 0 to stop: ")
    
    
    if number_input.isdigit():
        number_input = int(number_input)
        
        
        if number_input == 0:
            print("You have entered 0. The program will now end.")
            break
        
        
        elif number_input > 0:
            number_list.append(number_input)
            
            
            print(number_list)
            
            
            print(f"'{number_input}' has been added to the list.")

            
            print(f"The largest number on the list currently is: {max(number_list)}.")
            
    
    else:
        print("You have not entered a positive number. Please try again.")