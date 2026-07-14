# Request the user to input a string
# Store the string in a variable
str_manip = (input("What is the most famous monument in China? "))

# Calculate the length of the string
# Store the integer in a new variable
str_length = len(str_manip)

# Output the length of the string
print(f"The length of that sentence you entered is: {str_length}")

# Find the last letter of the string
last_letter = str_manip[-1]

# Replace every instance of the last letter with "@"
# Store the modified string in variable
str_manip = str_manip.replace(last_letter, "@")

# Output the modified string
print(f"Here is that sentence with every instance of replaced: {str_manip}")

# Find the last 3 characters of the string in reverse order
# Store the string in a new variable
last_3_inrev = str_manip[ :-4:-1]

# Output the last 3 characters of the string in reverse order
print(f"The last 3 characters of that sentence in reverse order: {last_3_inrev}")

# Find the first three letters of 
first_3_char = str_manip[:3]
last_2_char = str_manip[-2:]

five_letter_word = first_3_char + last_2_char
print(five_letter_word)