#Create a new file called while.py.
#Write a program that always asks the user to enter a number.
#When the user enters -1, the program should stop requesting the user to enter a number,
#The program must then calculate the average of the numbers entered, excluding the -1.
#Make use of the while loop repetition structure to implement the program.
#Compile, save, and run your file.

# Initialise variables
total_user_num: float = 0
i: int = 0
user_num = 0

# Define what is not an integer

# Request input of intiger
user_num = input("Please enter an integer (-1 to stop): ")

# if it is an integer, covert to float
if user_num.lstrip('+-').replace('.', '', 1).isdigit():
    user_num = float(user_num)

    print(user_num)
    print(type(user_num))
    print(total_user_num)
    print(type(total_user_num))

# If not an integer, convert request another input
else:
    print("That is not a number.")
    user_num = input("Please enter another integer (-1 to stop): ")


# A check for input
print(user_num)
print(type(user_num))

# If = -1, end program
if user_num == -1:
    print("You have entered -1. The program will now end.")


# while user_num != -1:

#     #check if it is an integer
#     if user_num.isdigit():
#         user_num = float(user_num)


#     print("That is an integer")
#     user_num = input("Please enter an integer (-1 to stop): ")
    
# else:
#     print("You have entered -1. The program wil not end")