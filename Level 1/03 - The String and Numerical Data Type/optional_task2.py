string_fav = input("Enter the name of your favourite restaurant: ")

int_fav = int(input("Enter your favourite number: "))

print(f"Your favourite restaurant is {string_fav}.")
print(f"Your favourite number is {int_fav}.")

print(int(string_fav))
# an error was returned as string_fav is a string made up of words (a string literal) with no numercal value and cannot be cast into an integer.