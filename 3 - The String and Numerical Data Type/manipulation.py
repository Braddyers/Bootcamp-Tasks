# Request the user to input a string
# Store the string in a variable called str_manip 
str_manip = (input("What is the most famous monument in China? "))

# Calculate the length of the string
# Store the length in a variable called str_length
str_length = len(str_manip)

# Output the length of the string
print(f"The length of that sentence you entered is: {str_length}")

# Find the last letter of the string
last_letter = str_manip[-1]

# Replace every instance of the last letter with an "@" symbol
str_manip.replace(last_letter, "@")

# 
print(str_manip.replace(last_letter, "@"))

last_3_inrev = str_manip[ :-4:-1]
print(f"The last 3 characters of the name of the most famous monument in China backwards are: {last_3_inrev}")

first_3_char = str_manip[:3]
last_2_char = str_manip[-2:]

five_letter_word = first_3_char + last_2_char
print(five_letter_word)