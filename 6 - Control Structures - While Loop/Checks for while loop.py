#Create a new file called while.py.
#Write a program that always asks the user to enter a number.
#When the user enters -1, the program should stop requesting the user to enter a number,
#The program must then calculate the average of the numbers entered, excluding the -1.
#Make use of the while loop repetition structure to implement the program.
#Compile, save, and run your file.

# Initialise variables
total_user_num = 0
i = 0
user_num = 0

# Define what is not an integer

# Request input of a number, -1 to stop
user_num = input("Please enter a number (-1 to stop): ")

def is_integer(user_num):
    return user_num.lstrip('+-').replace('.', '', 1).isdigit()

# if it is an integer, covert to float
while True:

    if is_integer(user_num):
        user_num = float(user_num)
            
        print(user_num, type(user_num))
        print(total_user_num, type(total_user_num))


        if user_num != -1:
            print("You have entered a valid number. Number added")
            total_user_num += user_num
            i += 1

            print(user_num, type(user_num))
            print(total_user_num, type(total_user_num))
            print(i)

            user_num = input("Please enter another number(-1 to stop): ")

        if user_num == -1:
            print("You have entered -1. The program will now end.")
            print(f"The average of the numbers you have entered is: {total_user_num / i}")
            break
        
# If not an integer, convert request another input
    else:
        print("That is not a number.")
        user_num = input("Please enter a number (-1 to stop): ")


# A check for input
#print(user_num)
#print(type(user_num))

# If = -1, end program



# while user_num != -1:

#     #check if it is an integer
#     if user_num.isdigit():
#         user_num = float(user_num)


#     print("That is an integer")
#     user_num = input("Please enter an integer (-1 to stop): ")
    
# else:
#     print("You have entered -1. The program wil not end")