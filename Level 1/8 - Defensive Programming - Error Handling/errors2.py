# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"                                                                                    # 1. Added quotation marks (runtime error), Lion is not defined and should be a string.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."        # 1. Added "f" for f-string (logic error), program still executes but do not get desired result. 2. Swopped "animal_type" with "number_of_teeth" (logic error), sentence did not make sense.

print(full_spec)                                                                                   # 1. Added parenthesis (syntax error), cannot execute without parenthesis around argument.


