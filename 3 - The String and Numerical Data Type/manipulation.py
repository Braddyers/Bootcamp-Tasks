str_manip = (input("What is the most famous monument in China? "))

str_length = len(str_manip)
print(f"The length of the entered sentence is: {str_length}")

last_letter = str_manip[-1]
str_manip.replace(last_letter, "@")
print(str_manip.replace(last_letter, "@"))

last_3_inrev = str_manip[ :-4:-1]
print(f"The last 3 characters of the name of the most famous monument in China backwards are: {last_3_inrev}")

first_3_char = str_manip[:3]
last_2_char = str_manip[-2:]

five_letter_word = first_3_char + last_2_char
print(five_letter_word)