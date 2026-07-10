# request the user to input their name and age
# request the user to input their house number and street name

# output a string that states the user's name, age, house number and street name

name = input("Please enter your name: ")
age = input("Please enter your age: ")
house_number = input("Please enter your house number: ")
street_name = input("Please enter your street name: ")

print("This is {} and they are {} years old. They live at house number {} on {}.".format(name, age, house_number, street_name))