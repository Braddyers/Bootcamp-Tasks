# Request the user to input a string
str_manip = (input("What is the ocean to the east of South Africa called? "))

# Calculate the length of the string
str_length = len(str_manip)

# Output the length of the string
print(f"The character length of your answer is: {str_length}")

# Find the last letter of the string
last_letter = str_manip[-1]

# Replace every occurance of that letter with @
str_manip = str_manip.replace(last_letter, "@")

# Output the modified string
print(f"Your answer with every occurrence of its last " + 
      f"letter replaced with @ is: {str_manip}")

# Find the last three characters of the string in reverse order
last_3_inrev = str_manip[ :-4:-1]

# Output the last three characters of the string in reverse order
print(f"The last three characters of your answer " +
      f"in reverse order is: {last_3_inrev}")

# Find the first three letters of the string
first_3_char = str_manip[:3]

# Find the last two letters of the string
last_2_char = str_manip[-2:]

# Concatinate the two variables to make a new string
five_letter_word = first_3_char + last_2_char

# Output the new string
print(f"The first three and last two characters of your " +
      f"answer combined is: {five_letter_word}")