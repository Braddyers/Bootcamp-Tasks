# Request user to input their name, age, house number and street name
# Store the inputs into their respective variables
name = input("Please enter your name: ")
age = input("Please enter your age: ")
house_number = input("Please enter your house number: ")
street_name = input("Please enter your street name: ")

# Output a string that states the user's name, age, house number and street name
print("You are {} and are {} years old. You live at house number {} on {}.".format(name, age, house_number, street_name))