#A user is asked to input answers to some python programming questions.
#When the user makes a mistake on the first two questions, they get asked a bonus question.
#If they get the first two questions right, they do not get asked if they would like a bonus question.

#Initialise score counting variable
score = 0

# Question 1
answer = input("What data type is the value 6.3 (integer or float)? ")

if answer == "float":
    score += 1
    print("You got it!")

elif answer == "integer":
    print("Oops. Integers do not have decimal points. The correct answer is: float.")

else:
    print("Sorry. The correct answer is: float.")

# Question 2 - Logic error                                
answer = float(input("What does 10 / 2.0 equate to? "))
  
if answer == 5.0:
    score += 1
    print("You got it!")
    
elif answer == "5":                                                                          #This condition will never evaluate to True, causing confusion during debugging or while testing edge cases.
    print("In Python, division by a float results in a float. The correct answer is: 5.0.")  #The elif condition checks if answer == "5" (a string), even though answer is converted to a float previous.
                                                                                             #Solution would be remove float function in line 22 and to put quotation marks around 5.0 in line 24.
else:                                                                                        
    print("Sorry. The correct answer is: 5.0.")

# Bonus Question
if score == 2:
    print("Well done. You answered both questions correctly!")
    
else:
    bonus_question = input("Would you like to answer another question (yes or no)? ")
    
    if bonus_question == "yes":
        answer = input("What does 20.0 * 10.0 equate to? ")
        
        if answer == "200.0":                                                                #Inputs are automatically stored as strings, this can allow for only the correct answers to be input. 
            score += 1
            print("You got it!")

        elif answer == "200":
            print("In Python, multiplication by a float results in a float. The correct answer is: 200.0.")

        else:
            print("Sorry. The correct answer is: 200.0.")

print(f"Your final score is: {score}")