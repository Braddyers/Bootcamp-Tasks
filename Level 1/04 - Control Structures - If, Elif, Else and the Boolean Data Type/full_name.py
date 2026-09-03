# ask the user to enter their full name and remove any leading or trailing spaces.
full_name = input("Please enter your full name: ").strip()

# check if the user has not entered anything.
if not full_name:
    print("You haven't entered anything. Please enter your full name.")

# check if the full name is less than four characters long.
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

# check if the full name is more than twenty-five characters long.
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# check if there are no spaces within the full name.
elif " " not in full_name:
    print("Please make sure you have entered both your first name and your surname with a space in between them.")

# if all checks pass, thank the user for entering their name.
else:
    print("Thank you for entering your name.")