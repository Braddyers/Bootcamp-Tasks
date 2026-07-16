# Request the user input the name of their favourite restaurant
string_fav = input("Enter the name of your favourite restaurant: ")

# Request the user input the name of their favourite number
# Cast it into and integer
int_fav = int(input("Enter your favourite number: "))

# Output the inputs
print(f"Your favourite restaurant is {string_fav}.")
print(f"Your favourite number is {int_fav}.")

# Cast string_fav into an integer then output the results
print(int(string_fav))

# An error was returned as string_fav is a string made up of words (string 
# literals) with no numercal value and cannot be cast into an integer