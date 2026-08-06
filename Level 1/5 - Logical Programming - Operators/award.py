# Ask the user to enter all three event times (in minutes), then convert them 
# into integers
swimming_t = int(input("Please enter the swimming event time (in minutes): "))
cycling_t = int(input("Please enter the cycling event time (in minutes): "))
running_t = int(input("Please enter the running event time (in minutes): "))

# check for negative input values
if swimming_t < 0 or cycling_t < 0 or running_t < 0:
    print("Please only enter positive numbers.")

else:
    # Calculate and display the total triathlon time
    totaltri_t = swimming_t + cycling_t + running_t
    print(f"Your total time from all of the events was {totaltri_t} minutes.")


    # Between and including 0 and 100, display Provincial Colours
    if 0 <= totaltri_t <= 100:
        print("Congratulations! You have been awarded Provincial Colours!")    


    # Between and including 101 and 105, display Provincial Half Colours
    elif 101 <= totaltri_t <= 105:
        print("Congratulations! You have been awarded Provincial Half Colours!")


    # Between and including 106 and 110, display Provincial Scroll
    elif 106 <= totaltri_t <= 110:
        print("Congratulations! You have been awarded a Provincial Scroll!")


    # More than and equal to 111, display no award.
    elif totaltri_t >= 111:
        print("Unfortunately you receive no award.")