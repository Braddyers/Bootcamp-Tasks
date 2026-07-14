# Request the user to input a string
# Store the string in a variable
str_manip = (input("What is the most famous monument in China? "))

# Calculate the length of the string
# Store the integer in a new variable
str_length = len(str_manip)

# Output the length of the string
print(f"The character length of your answer is: {str_length}")

# Find the last letter of the string
last_letter = str_manip[-1]

# Replace every occurance of that letter with @
# Store the modified string in variable
str_manip = str_manip.replace(last_letter, "@")

# Output the modified string
print(f"Your answer with every occurrence of its last " + 
      f"letter replaced with @ is: {str_manip}")

# Find the last three characters of the string in reverse order
# Store the string in a new variable
last_3_inrev = str_manip[ :-4:-1]

# Output the last three characters of the string in reverse order
print(f"The last three characters of your answer " +
      f"in reverse order is: {last_3_inrev}")

# Find the first three letters of the string
# Store that new string in a new variable
first_3_char = str_manip[:3]

# Find the last two letters of the string
# Store that new string in a new variable
last_2_char = str_manip[-2:]

# Concatinate the two variables to make a new string
# Store the new string in a new variable 
five_letter_word = first_3_char + last_2_char

# Output the new string
print(f"The first three and last two characters of your answer combined is: {five_letter_word}")