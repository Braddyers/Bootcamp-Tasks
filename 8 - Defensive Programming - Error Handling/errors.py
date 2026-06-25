# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")                                           # 1. Added parenthesis after print function (syntax error), parenthesis required around argument to execute.
print("\n")                                                                     # 1. Indentation error (syntax error). 2. Added parenthesis after print function (syntax error).

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                                                                  # 1. Indentation error (syntax error). 2. Removed "years old" (runtime error), letters cannot be coverted into an integer in line 10. 3. Removed an "=" (runtime error), == is an equality operator and does not assign a value to the variable.
age = int(age_Str)                                                              # 1. Indentation error (syntax error).
print(f"I'm {age} years old.")                                                  # 1. Indentation error (syntax error). 2. f-string method used to concatenate data types (runtime error), cannot concatenate two different data types.

# Variables declaring additional years and printing the total years of age
years_from_now = 3                                                              # 1. Indentation error (syntax error). 2. Cannot concatinate string and integer in line 15 (runtime error), removed quotation marks to solve issue.
total_years = age + years_from_now                                              # 1. Indentation error (syntax error).

print(f"The total number of years: {total_years}.")                             # 1. Added parenthesis after print function (syntax error). 2. Changed to "answer_years" to "total_years" (runtime error), "answer_years" is not defined. 3. f-string method used to concatenate (runtime error), cannot concatenate two different data types.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 + 6                                             # 1. Changed "total" to "total_years" (runtime error), "total" is not defined. 2. Added 6 to get to 330 (logic error).
print(f"In 3 years and 6 months, I'll be {total_months} months old.")           # 1. Added parenthesis after print function (syntax error). 2. f-string method used to concatenate (runtime error), cannot concatenate two different data types.

#HINT, 330 months is the correct answer

