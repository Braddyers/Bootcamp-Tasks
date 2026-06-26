# Create a list called menu and two dictionaries; stock and price
menu = ["Sandwich", "Bagel", "Wrap", "Burger"]

# Number of items in stock
stock = {"Sandwich": 10,
         "Bagel": 7,
         "Wrap": 12,
         "Burger": 15}

# Price per item
price = {"Sandwich": 50,
         "Bagel": 65,
         "Wrap": 75,
         "Burger": 70}

# Initialize final result variable
total_stock = 0

# Calculate the total stock's worth
for items in menu:                                   # Loop through each item in the menu list
    item_value = stock[items] * price[items]         # Multiply stock value by price value of each item
    total_stock += item_value                        # Add item values together

# Print out the result
print(f"The total value of the stock in the cafe is: R{total_stock}")