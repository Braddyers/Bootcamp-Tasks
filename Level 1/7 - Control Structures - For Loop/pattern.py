# Define range, 9 rows of pattern, 9 iterations/rows
for i in range(1, 10):

    # Pattern increases by 1 until 5th row
    if i <= 5:
        stars = i

        # Output star symbol multiplied by row
        print("*" * stars)

    # Patterns decrease by 1 after 5th row, no. of stars = (no. of rows + 1) - i
    else:
        stars = 10 - i

        # Output star symbol multiplied by (10 - row)
        print("*" * stars)