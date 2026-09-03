#Establish row variable to use in iteration calculations
rows = 9

#Range will be number of rows + 1
for i in range(1, rows + 1):
    
    #First half of pattern until row 5 ("*" is added as iteration scales)
    if i <= 5:
        print("*" * i)
    
    #Second half of pattern from row 6 ("*" decreases in each subsequent iteration according to my calculated formula)
    else:
        print("*" * (rows - i + 1))